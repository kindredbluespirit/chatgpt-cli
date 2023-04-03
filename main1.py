#!/usr/bin/env python

import openai
import signal

openai.api_key = "<your-api-key-here>"

## https://github.com/onetruffle/gists/blob/main/python-interpreter.py
def sigint_handler(signum, frame):
    print("\nKeyboard interrupt (Ctrl+C) detected. Exiting...")
    exit(1)
signal.signal(signal.SIGINT, sigint_handler)

if __name__ == "__main__":

    # messages = [{"role": "system", "content": "You are a helpful assistant."}]
    messages = []
    role = "user"
    while True:
        try:
            content = input(f"\033[33m{role} > \033[0m")
        except EOFError:
            print("\nExiting...")
            # break
            exit(2)
        messages += [{"role": role, "content": content}]

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )["choices"][0]["message"]
        print(f'\033[35m{response["role"]} > \033[0m{response["content"].lstrip()}')
        messages += [response]