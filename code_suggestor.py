#install - pip install llamaapi

import os
import json
from openai import OpenAI


data_path = '/Users/poojithapenta/Desktop/UMass/COMPSCI692/commented_data'
output_path= '/Users/poojithapenta/Desktop/UMass/COMPSCI692/llama-generated_code'

# Iterate over files in the directory
for filename in os.listdir(data_path):
    if filename.endswith(".py"):  
        file_path = os.path.join(data_path, filename)
        
        with open(file_path, 'r', encoding='utf-8') as file:
            code = file.read()

        client = OpenAI(
        api_key = "LA-423ae285160e4c4f8cfb1e6f7d3b0c481ce796d67ba24010a9198a9d30632803",
        base_url = "https://api.llama-api.com")

        completion  = client.chat.completions.create(
        model="llama3.2-1b",
        messages=[
        {"role": "system", "content":  f"Please complete the TODO part in the code:\n\n{code}"}
        ],
        max_tokens=1000,)
        model_data = completion.model_dump()
        generated_code=model_data['choices'][0]['message']['content']

        
        base_name = os.path.splitext(filename)[0]
        new_file_path = os.path.join(output_path, f"{base_name}_generated.py")
        
        
        with open(new_file_path, 'w', encoding='utf-8') as commented_file:
            commented_file.write(generated_code)  
        
        print(f"Processed {filename} and saved suggestions to {new_file_path}")

print("Done!")

