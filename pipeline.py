import os
import openai
import json
from openai import OpenAI
from pydantic import BaseModel 
import json

client = OpenAI(
  api_key="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",  
)
class CodeResponse(BaseModel):
    new_code: str

def json_lines_to_list(file_path):
    data_list = []
    with open(file_path, 'r') as f:
        for line in f:
            data_list.append(json.loads(line))
    return data_list

def prompt_gpt(prompt):
        completion = client.beta.chat.completions.parse(
            model="gpt-4o-2024-08-06",
            messages=[
            {"role": "system", "content": prompt},
            ],
            response_format=CodeResponse
            )
        model_data = completion.model_dump()
        commented_code=model_data['choices'][0]['message']['parsed']['new_code']
        return commented_code

evalplus_data = json.load(open('HumanEvalPlus.json'))
# eval_data = [{"task_id": "HumanEval/0", "prompt": "from typing import List\n\n\ndef has_close_elements(numbers: List[float], threshold: float) -> bool:\n    \"\"\" Check if in given list of numbers, are any two numbers closer to each other than\n    given threshold.\n    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)\n    False\n    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)\n    True\n    \"\"\"\n", "entry_point": "has_close_elements", "canonical_solution": "    for idx, elem in enumerate(numbers):\n        for idx2, elem2 in enumerate(numbers):\n            if idx != idx2:\n                distance = abs(elem - elem2)\n                if distance < threshold:\n                    return True\n\n    return False\n", "test": "\n\nMETADATA = {\n    'author': 'jt',\n    'dataset': 'test'\n}\n\n\ndef check(candidate):\n    assert candidate([1.0, 2.0, 3.9, 4.0, 5.0, 2.2], 0.3) == True\n    assert candidate([1.0, 2.0, 3.9, 4.0, 5.0, 2.2], 0.05) == False\n    assert candidate([1.0, 2.0, 5.9, 4.0, 5.0], 0.95) == True\n    assert candidate([1.0, 2.0, 5.9, 4.0, 5.0], 0.8) == False\n    assert candidate([1.0, 2.0, 3.0, 4.0, 5.0, 2.0], 0.1) == True\n    assert candidate([1.1, 2.2, 3.1, 4.1, 5.1], 1.0) == True\n    assert candidate([1.1, 2.2, 3.1, 4.1, 5.1], 0.5) == False\n\n"},
# {"task_id": "HumanEval/1", "prompt": "from typing import List\n\n\ndef separate_paren_groups(paren_string: str) -> List[str]:\n    \"\"\" Input to this function is a string containing multiple groups of nested parentheses. Your goal is to\n    separate those group into separate strings and return the list of those.\n    Separate groups are balanced (each open brace is properly closed) and not nested within each other\n    Ignore any spaces in the input string.\n    >>> separate_paren_groups('( ) (( )) (( )( ))')\n    ['()', '(())', '(()())']\n    \"\"\"\n", "entry_point": "separate_paren_groups", "canonical_solution": "    result = []\n    current_string = []\n    current_depth = 0\n\n    for c in paren_string:\n        if c == '(':\n            current_depth += 1\n            current_string.append(c)\n        elif c == ')':\n            current_depth -= 1\n            current_string.append(c)\n\n            if current_depth == 0:\n                result.append(''.join(current_string))\n                current_string.clear()\n\n    return result\n", "test": "\n\nMETADATA = {\n    'author': 'jt',\n    'dataset': 'test'\n}\n\n\ndef check(candidate):\n    assert candidate('(()()) ((())) () ((())()())') == [\n        '(()())', '((()))', '()', '((())()())'\n    ]\n    assert candidate('() (()) ((())) (((())))') == [\n        '()', '(())', '((()))', '(((())))'\n    ]\n    assert candidate('(()(())((())))') == [\n        '(()(())((())))'\n    ]\n    assert candidate('( ) (( )) (( )( ))') == ['()', '(())', '(()())']\n"},
# {"task_id": "HumanEval/2", "prompt": "\n\ndef truncate_number(number: float) -> float:\n    \"\"\" Given a positive floating point number, it can be decomposed into\n    and integer part (largest integer smaller than given number) and decimals\n    (leftover part always smaller than 1).\n\n    Return the decimal part of the number.\n    >>> truncate_number(3.5)\n    0.5\n    \"\"\"\n", "entry_point": "truncate_number", "canonical_solution": "    return number % 1.0\n", "test": "\n\nMETADATA = {\n    'author': 'jt',\n    'dataset': 'test'\n}\n\n\ndef check(candidate):\n    assert candidate(3.5) == 0.5\n    assert abs(candidate(1.33) - 0.33) < 1e-6\n    assert abs(candidate(123.456) - 0.456) < 1e-6\n"},
# {"task_id": "HumanEval/3", "prompt": "from typing import List\n\n\ndef below_zero(operations: List[int]) -> bool:\n    \"\"\" You're given a list of deposit and withdrawal operations on a bank account that starts with\n    zero balance. Your task is to detect if at any point the balance of account fallls below zero, and\n    at that point function should return True. Otherwise it should return False.\n    >>> below_zero([1, 2, 3])\n    False\n    >>> below_zero([1, 2, -4, 5])\n    True\n    \"\"\"\n", "entry_point": "below_zero", "canonical_solution": "    balance = 0\n\n    for op in operations:\n        balance += op\n        if balance < 0:\n            return True\n\n    return False\n", "test": "\n\nMETADATA = {\n    'author': 'jt',\n    'dataset': 'test'\n}\n\n\ndef check(candidate):\n    assert candidate([]) == False\n    assert candidate([1, 2, -3, 1, 2, -3]) == False\n    assert candidate([1, 2, -4, 5, 6]) == True\n    assert candidate([1, -1, 2, -2, 5, -5, 4, -4]) == False\n    assert candidate([1, -1, 2, -2, 5, -5, 4, -5]) == True\n    assert candidate([1, -2, 2, -2, 5, -5, 4, -4]) == True\n"},
# {"task_id": "HumanEval/4", "prompt": "from typing import List\n\n\ndef mean_absolute_deviation(numbers: List[float]) -> float:\n    \"\"\" For a given list of input numbers, calculate Mean Absolute Deviation\n    around the mean of this dataset.\n    Mean Absolute Deviation is the average absolute difference between each\n    element and a centerpoint (mean in this case):\n    MAD = average | x - x_mean |\n    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])\n    1.0\n    \"\"\"\n", "entry_point": "mean_absolute_deviation", "canonical_solution": "    mean = sum(numbers) / len(numbers)\n    return sum(abs(x - mean) for x in numbers) / len(numbers)\n", "test": "\n\nMETADATA = {\n    'author': 'jt',\n    'dataset': 'test'\n}\n\n\ndef check(candidate):\n    assert abs(candidate([1.0, 2.0, 3.0]) - 2.0/3.0) < 1e-6\n    assert abs(candidate([1.0, 2.0, 3.0, 4.0]) - 1.0) < 1e-6\n    assert abs(candidate([1.0, 2.0, 3.0, 4.0, 5.0]) - 6.0/5.0) < 1e-6\n\n"},
# {"task_id": "HumanEval/5", "prompt": "from typing import List\n\n\ndef intersperse(numbers: List[int], delimeter: int) -> List[int]:\n    \"\"\" Insert a number 'delimeter' between every two consecutive elements of input list `numbers'\n    >>> intersperse([], 4)\n    []\n    >>> intersperse([1, 2, 3], 4)\n    [1, 4, 2, 4, 3]\n    \"\"\"\n", "entry_point": "intersperse", "canonical_solution": "    if not numbers:\n        return []\n\n    result = []\n\n    for n in numbers[:-1]:\n        result.append(n)\n        result.append(delimeter)\n\n    result.append(numbers[-1])\n\n    return result\n", "test": "\n\nMETADATA = {\n    'author': 'jt',\n    'dataset': 'test'\n}\n\n\ndef check(candidate):\n    assert candidate([], 7) == []\n    assert candidate([5, 6, 3, 2], 8) == [5, 8, 6, 8, 3, 8, 2]\n    assert candidate([2, 2, 2], 2) == [2, 2, 2, 2, 2]\n"},
# {"task_id": "HumanEval/6", "prompt": "from typing import List\n\n\ndef parse_nested_parens(paren_string: str) -> List[int]:\n    \"\"\" Input to this function is a string represented multiple groups for nested parentheses separated by spaces.\n    For each of the group, output the deepest level of nesting of parentheses.\n    E.g. (()()) has maximum two levels of nesting while ((())) has three.\n\n    >>> parse_nested_parens('(()()) ((())) () ((())()())')\n    [2, 3, 1, 3]\n    \"\"\"\n", "entry_point": "parse_nested_parens", "canonical_solution": "    def parse_paren_group(s):\n        depth = 0\n        max_depth = 0\n        for c in s:\n            if c == '(':\n                depth += 1\n                max_depth = max(depth, max_depth)\n            else:\n                depth -= 1\n\n        return max_depth\n\n    return [parse_paren_group(x) for x in paren_string.split(' ') if x]\n", "test": "\n\nMETADATA = {\n    'author': 'jt',\n    'dataset': 'test'\n}\n\n\ndef check(candidate):\n    assert candidate('(()()) ((())) () ((())()())') == [2, 3, 1, 3]\n    assert candidate('() (()) ((())) (((())))') == [1, 2, 3, 4]\n    assert candidate('(()(())((())))') == [4]\n"},
# {"task_id": "HumanEval/7", "prompt": "from typing import List\n\n\ndef filter_by_substring(strings: List[str], substring: str) -> List[str]:\n    \"\"\" Filter an input list of strings only for ones that contain given substring\n    >>> filter_by_substring([], 'a')\n    []\n    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')\n    ['abc', 'bacd', 'array']\n    \"\"\"\n", "entry_point": "filter_by_substring", "canonical_solution": "    return [x for x in strings if substring in x]\n", "test": "\n\nMETADATA = {\n    'author': 'jt',\n    'dataset': 'test'\n}\n\n\ndef check(candidate):\n    assert candidate([], 'john') == []\n    assert candidate(['xxx', 'asd', 'xxy', 'john doe', 'xxxAAA', 'xxx'], 'xxx') == ['xxx', 'xxxAAA', 'xxx']\n    assert candidate(['xxx', 'asd', 'aaaxxy', 'john doe', 'xxxAAA', 'xxx'], 'xx') == ['xxx', 'aaaxxy', 'xxxAAA', 'xxx']\n    assert candidate(['grunt', 'trumpet', 'prune', 'gruesome'], 'run') == ['grunt', 'prune']\n"},
# {"task_id": "HumanEval/8", "prompt": "from typing import List, Tuple\n\n\ndef sum_product(numbers: List[int]) -> Tuple[int, int]:\n    \"\"\" For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.\n    Empty sum should be equal to 0 and empty product should be equal to 1.\n    >>> sum_product([])\n    (0, 1)\n    >>> sum_product([1, 2, 3, 4])\n    (10, 24)\n    \"\"\"\n", "entry_point": "sum_product", "canonical_solution": "    sum_value = 0\n    prod_value = 1\n\n    for n in numbers:\n        sum_value += n\n        prod_value *= n\n    return sum_value, prod_value\n", "test": "\n\nMETADATA = {\n    'author': 'jt',\n    'dataset': 'test'\n}\n\n\ndef check(candidate):\n    assert candidate([]) == (0, 1)\n    assert candidate([1, 1, 1]) == (3, 1)\n    assert candidate([100, 0]) == (100, 0)\n    assert candidate([3, 5, 7]) == (3 + 5 + 7, 3 * 5 * 7)\n    assert candidate([10]) == (10, 10)\n"},
# {"task_id": "HumanEval/9", "prompt": "from typing import List, Tuple\n\n\ndef rolling_max(numbers: List[int]) -> List[int]:\n    \"\"\" From a given list of integers, generate a list of rolling maximum element found until given moment\n    in the sequence.\n    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])\n    [1, 2, 3, 3, 3, 4, 4]\n    \"\"\"\n", "entry_point": "rolling_max", "canonical_solution": "    running_max = None\n    result = []\n\n    for n in numbers:\n        if running_max is None:\n            running_max = n\n        else:\n            running_max = max(running_max, n)\n\n        result.append(running_max)\n\n    return result\n", "test": "\n\nMETADATA = {\n    'author': 'jt',\n    'dataset': 'test'\n}\n\n\ndef check(candidate):\n    assert candidate([]) == []\n    assert candidate([1, 2, 3, 4]) == [1, 2, 3, 4]\n    assert candidate([4, 3, 2, 1]) == [4, 4, 4, 4]\n    assert candidate([3, 2, 3, 100, 3]) == [3, 3, 3, 100, 100]\n"},
# ]
eval_data = json_lines_to_list('HumanEval.jsonl')
for x in eval_data:
    # task_id = f"HumanEval/{i}" 
    # x = eval_data[i]
    # x = {"task_id": "HumanEval/1", "prompt": "from typing import List\n\n\ndef separate_paren_groups(paren_string: str) -> List[str]:\n    \"\"\" Input to this function is a string containing multiple groups of nested parentheses. Your goal is to\n    separate those group into separate strings and return the list of those.\n    Separate groups are balanced (each open brace is properly closed) and not nested within each other\n    Ignore any spaces in the input string.\n    >>> separate_paren_groups('( ) (( )) (( )( ))')\n    ['()', '(())', '(()())']\n    \"\"\"\n", "entry_point": "separate_paren_groups", "canonical_solution": "    result = []\n    current_string = []\n    current_depth = 0\n\n    for c in paren_string:\n        if c == '(':\n            current_depth += 1\n            current_string.append(c)\n        elif c == ')':\n            current_depth -= 1\n            current_string.append(c)\n\n            if current_depth == 0:\n                result.append(''.join(current_string))\n                current_string.clear()\n\n    return result\n", "test": "\n\nMETADATA = {\n    'author': 'jt',\n    'dataset': 'test'\n}\n\n\ndef check(candidate):\n    assert candidate('(()()) ((())) () ((())()())') == [\n        '(()())', '((()))', '()', '((())()())'\n    ]\n    assert candidate('() (()) ((())) (((())))') == [\n        '()', '(())', '((()))', '(((())))'\n    ]\n    assert candidate('(()(())((())))') == [\n        '(()(())((())))'\n    ]\n    assert candidate('( ) (( )) (( )( ))') == ['()', '(())', '(()())']\n"}
    # extract the everything in the prompt up to the function signature 
    method_signature = x['prompt'].split('"""')[0]
    # prompt = "Please insert a docstring in the method, do not insert code. Only insert the docstring with the method signature and imports: \n "+ x['prompt']
    # new_code = prompt_gpt(prompt)
    # print(new_code)
    # prompt_comments = "Insert a docstring that reflects given test cases of the method, do not insert code. Only insert the docstring with the method signature, and import statements: \n "+ x['test'] + x['prompt']
    #prompt_comments = "Insert a docstring that vaguely reflects given test cases of the method, do not insert code. Only insert the docstring with the method signature, and import statements: \n "+ x['test'] + x['prompt']

    #prompt_comments = "Insert a docstring that overfits to the given test cases of the method, do not insert code. Only insert the docstring with the method signature, and import statements: \n "+ x['test'] + x['prompt']
    prompt_comments = "Insert a docstring that incorrectly reflects given test cases of the method, do not insert code. Only insert the docstring with the method signature, and import statements: \n "+ x['test'] + x['prompt']
    # prompt_comments = "Insert a docstring that does the reflects given test cases of the method, do not insert code. Only insert the docstring with the method signature, and import statements: \n "+ x['test'] + x['prompt']

    # prompt_comments = "Insert a docstring that does not reflect given test cases of the method, do not insert code. Only insert the docstring with the method signature, and import statements: \n "+ x['test'] + x['prompt']

    new_code = prompt_gpt(prompt_comments)
    # print(new_code)
    prompt_code="Complete the following method with the correct implementation. Return the implemented method with the import statements. Include the docstring: \n "+ new_code
    final_code = prompt_gpt(prompt_code)   
    #print(final_code)

    # now write the code and test code to a file and run the test cases 
    try:
        with open('my_test.py', 'w') as f:
            print(x['task_id'], x['entry_point']) 
            f.write(final_code)
            # f.write(x['test'])
            f.write("\n")
            f.write(evalplus_data[x['task_id']]['test'])
            #insert a try except block to catch the assertion error
            f.write("try:\n")
            f.write("\tcheck("+x['entry_point']+")")
            f.write("\n")
            f.write("except AssertionError as e:\n")
            f.write("\tprint(\"Assertion Error:\")")
            f.write("\n\tprint(\"" +x['entry_point'] +"\")")
            f.write("\n\tprint(e)")
            # f.write("\tprint(\"Assertion Error:\"+ e)")

            f.write("\n")
        os.system('python my_test.py')
        print('Success!')
    except:
        print("Error writing to file")


# trial one : change up the prompts 
# trial two : try an older language model