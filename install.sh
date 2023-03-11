#!/bin/sh
f=${XDG_BIN_HOME:-"~/.local/bin"}/chatgpt

cp main.py $f
chmod +x $f
