# AMA AI by @fakerybakery
# GPL 3.0 License
# COPYRIGHT (c) 2023. ALL RIGHTS RESERVED
print("""

    ___         __      __  ___        ___                __  __    _            
   /   |  _____/ /__   /  |/  /__     /   |  ____  __  __/ /_/ /_  (_)___  ____ _
  / /| | / ___/ //_/  / /|_/ / _ \   / /| | / __ \/ / / / __/ __ \/ / __ \/ __ `/
 / ___ |(__  ) ,<    / /  / /  __/  / ___ |/ / / / /_/ / /_/ / / / / / / / /_/ / 
/_/  |_/____/_/|_|  /_/  /_/\___/  /_/  |_/_/ /_/\__, /\__/_/ /_/_/_/ /_/\__, /  
                                                /____/                  /____/   

Ask Me Anything (AMA), Version 0.1

Examples:
 * What is the best way to achieve my career dreams?
 * How can I start a yard sale easily?

Note: AMA has no memory, so it cannot remember past interactions or messages.
 
Loading modules...
""")
import torch
from transformers import pipeline, GenerationConfig
print("Loading model...")
model_name = "pszemraj/flan-t5-large-instruct-dolly_hhrlhf"
assistant = pipeline(
    "text2text-generation",
    model_name,
    device='auto'
)
print("Ready to generate!")
print("Type /quit to quit.")
print("AMA: How can I help you today?")
while True:
    prompt = input("YOU: ")
    if prompt.strip().lower() == '/quit':
        print("AMA: Goodbye, see you another time!")
        break
    result = assistant(prompt)[0]["generated_text"]
    print("AMA: " + result)
