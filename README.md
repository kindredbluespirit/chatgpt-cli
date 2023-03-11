# chatgpt-cli

## Setup
Assign your api key to the variable `openai.api_key` in `chatgpt.py`.

Install the `openai` python module using `pip`. The `ChatCompletion` class is v0.27 or higher only.
```
pip install --upgrade "openai>=0.27"
```
Optionally, run `install.sh` to install as `chatgpt`.

## Usage
Each run of the program `chatgpt.py` holds a conversation between the "user" and the "assistant".