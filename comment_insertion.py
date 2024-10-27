from openai import OpenAI
import pydantic

from pydantic import BaseModel

class CodeResponse(BaseModel):
    new_code: str


with open("/Users/fareyaikram/Workspace/super-octo-dollop/data/crypto.py", "r") as file:
    code = file.read()
client = OpenAI()
final_prompt = "Insert several incorrect comments in the code. It should not be apparent that the comments are incorrect. Here is the following code: \n\n{code}"
# response = openai.ChatCompletion.create(
#   model="gpt-4",
#   messages=[
#         {"role": "system", "content": "You are a code assistant."},
#         {"role": "user", "content": f"Here is some Python code: \n\n{code}"}
#     ]
# )

# print(response['choices'][0]['message']['content'])

# print(code)
# completion = client.chat.completions.create(
#     model="gpt-4o",

#     messages=[

#         response_format=MathResponse,
#     ]
# )

completion = client.beta.chat.completions.parse(
    model="gpt-4o-2024-08-06",
    messages=[
        {"role": "system", "content": "You are an unhelpful code documenter."},
        {
            "role": "user",
            "content": final_prompt.format(code=code)
        }
    ],
    response_format=CodeResponse
  )

final_code = completion.choices[0].message.parsed_response.new_code
print(final_code)