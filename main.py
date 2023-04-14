#!/usr/bin/env python
import readline
import argparse
import os
from ast import literal_eval
import time

import openai
from prompt_toolkit import PromptSession
import backoff

openai.api_key = "<your-api-key-here>"
session = PromptSession()

prompt_continuation = lambda *args, **kwargs: "> "

def backoff_hdlr(details):
    print ("Backing off {wait:0.1f} seconds after {tries} tries "
           .format(**details))

@backoff.on_exception(backoff.expo, 
    (openai.error.RateLimitError,
        openai.error.APIConnectionError),
    on_backoff=backoff_hdlr)
def get_response():
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )["choices"][0]["message"]

    return response

if __name__ == "__main__":
    try:
        wd = os.environ["XDG_DATA_HOME"] + "/chatgpt"
    except KeyError:
        wd = os.environ["HOME"] + "/.local/share" + "/chatgpt"
    if not os.path.isdir(wd):
        os.mkdir(wd)

    parser = argparse.ArgumentParser()
    parser.add_argument("filename", nargs="?", default=None, help="the file containing the conversation")
    filename = parser.parse_args().filename
    if filename is not None:
        with open(filename, "r") as filestream:
            string = filestream.read()
            messages = literal_eval(string)
    else:
        messages = []
    
    timestring = time.strftime("%Y%m%d-%H%M%S")
    filename = wd + f"/{timestring}.txt"
    filename_conversation = wd + f"/{timestring}-conversation.txt"
    
    while True:
        role = "user"
        try:
            content = session.prompt(message=f"{role}> ", multiline=True, prompt_continuation=prompt_continuation)    
        except KeyboardInterrupt:
            print()
            continue
        except EOFError:
            print("Exiting..")
            exit(2)

        messages += [{"role": role, "content": content}]

        with open(filename, "w") as filestream:
            string = repr(messages)
            filestream.write(string)
        print('-' * 10)

        with open(filename_conversation, "a") as filestream:
            string = role + "> " + content + '\n' + '-' * 10 + '\n'
            filestream.write(string)
        
        try:
            response = get_response()
        except KeyboardInterrupt:
            print()
            continue

        role = response["role"]
        content = response["content"]
        print(f'{role}> {content.lstrip()}')

        messages += [{"role": role, "content": content}]


        with open(filename, "w") as filestream:
            string = repr(messages)
            filestream.write(string)
        print('-' * 10)

        with open(filename_conversation, "a") as filestream:
            string = role + "> " + content.lstrip() + '\n' + '-' * 10 + '\n'
            filestream.write(string)
