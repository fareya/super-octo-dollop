#install - pip install llamaapi

import os
import json
from openai import OpenAI


data_path = '/Users/poojithapenta/Desktop/UMass/COMPSCI692/commented_data'
output_path= '/Users/poojithapenta/Desktop/UMass/COMPSCI692/generated_code'

# Iterate over files in the directory
for filename in os.listdir(data_path):
    if filename.endswith(".py"):  
        file_path = os.path.join(data_path, filename)
        
        with open(file_path, 'r', encoding='utf-8') as file:
            code = file.read()

        client = OpenAI(
        api_key = "API",
        base_url = "https://api.llama-api.com")

        completion  = client.chat.completions.create(
        model="llama3.1-70b",
        messages=[
        {"role": "system", "content":  f"Please complete the TODO part in the code:\n\n{code}"}
        ],)
        model_data = completion.model_dump()
        commented_code=model_data['choices'][0]['message']
        print(commented_code)
      
        break
        # Optionally save response to a file or process further
        output_file_path = os.path.join(output_path, f"{os.path.splitext(filename)[0]}_suggestions.py")
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            output_file.write(json.dumps(response_data, indent=2))
        
        print(f"Processed {filename} and saved suggestions to {output_file_path}")

print("Done!")

