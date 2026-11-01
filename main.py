import os
import sys
from dotenv import load_dotenv
from openai import OpenAI
from constants import system_prompt
from available_functions import available_functions
import argparse
import json
from call_function import call_function


load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")
if api_key == None:
    raise RuntimeError("no api key loaded")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

parser = argparse.ArgumentParser(description="k lo k tu kiere")
parser.add_argument("user_prompt", type=str, help="escribe")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output.")

args = parser.parse_args()

messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": args.user_prompt},
            ]





def main():

    for _ in range(21):
        
        response = client.chat.completions.create(
            model="openrouter/free",
            messages=messages,
            temperature=0,
            tools=available_functions,
        )
        message = response.choices[0].message
        if response.usage == None:
            raise RuntimeError("API request failed, no response")

        if args.verbose == True:
            print(f"User prompt: {args.user_prompt}")
            print(f"Prompt tokens: {response.usage.prompt_tokens}")
            print(f"Response tokens: {response.usage.completion_tokens}")
        

        
        if message.tool_calls != None:
            for tool_call in message.tool_calls:
                called_function = call_function(tool_call, args.verbose)
                messages.append(called_function)
                if not called_function["content"]:
                    raise Exception("Content empty")
            if args.verbose == True:
                print(f"-> {called_function['content']}")
            messages.append(message)
            messages.append(called_function)
        else:
            print(message.content)
            messages.append(message)
            
            return messages
    
    print("Iterated over limit")
    sys.exit(1)
    return message.content


if __name__ == "__main__":
    main()
