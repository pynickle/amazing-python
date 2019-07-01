import json
import os


with open("./Tools/auto_copyright/config.json", "r", encoding="utf-8") as f:
    content = f.read()
    info = json.loads(content)
    args.path =