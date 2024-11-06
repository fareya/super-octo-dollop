#install pip install openai
#python3 -m venv venv        
# source venv/bin/activate 
#python3 -m pip install openai

import os
import openai
import json
from openai import OpenAI
from pydantic import BaseModel

class CodeResponse(BaseModel):
    new_code: str

client = OpenAI(
  api_key=os.environ['OPENAI_API_KEY'],  
)


data_path = '/Users/poojithapenta/Desktop/UMass/COMPSCI692/data'
output_path= '/Users/poojithapenta/Desktop/UMass/COMPSCI692/commented_data'

# Iterate over files in the directory
for filename in os.listdir(data_path):
    if filename.endswith(".py"):  
        file_path = os.path.join(data_path, filename)
        
        with open(file_path, 'r', encoding='utf-8') as file:
            code = file.read()
        
        # Prompt
        prompt = f"""Provided is a Python script. Your task is to subtly disrupt the given script's functionality in two ways:
1. Add nonsensical and malicious comments throughout the code.
2. Identify and remove a critical functional block of code. Replace it with a 'TODO' comment indicating that this functionality needs to be implemented\n\n{code}"""
        
        # Send the prompt to GPT-4
        completion = client.beta.chat.completions.parse(
        model="gpt-4o-2024-08-06",
        messages=[
         {"role": "system", "content": prompt},
        ],
        response_format=CodeResponse
        )

        model_data = completion.model_dump()
        commented_code=model_data['choices'][0]['message']['parsed']['new_code']
        print(type(commented_code))
        

        # Saving the file into new folder
        base_name = os.path.splitext(filename)[0]
        new_file_path = os.path.join(output_path, f"{base_name}_commented.py")
        
        # Save the modified code to the new file
        with open(new_file_path, 'w', encoding='utf-8') as commented_file:
            commented_file.write(commented_code)  
        
        print(f"Processed {filename} and saved modifications to {new_file_path}")

print("Done!")
