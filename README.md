# chatgpt-cli

## Setup
Assign your api key to the variable `openai.api_key` in `chatgpt.py`.

Install the `openai` python module using `pip`. The `ChatCompletion` class is v0.27 or higher only.
```
pip install --upgrade "openai>=0.27"
```
Also install `prompt_toolkit` and `backoff`.

Optionally, run `install.sh` to install as `chatgpt`.

## Usage
Each run of the program `chatgpt.py` holds a conversation between the "user" and the "assistant".

The exchange is stored in `~/.local/share/chatgpt/` by default. Two files, one in json and one human readable
are exported after each agent finishes talking.

You import an existing conversation by running `chatgpt <filepath>`.

Note that the maximum permissible total number of tokens for any conversation is 4096 at the moment.