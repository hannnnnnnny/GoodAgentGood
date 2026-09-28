import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(
api_key=os.getenv("DEEPSEEK_API_KEY"),
base_url=os.getenv("https://api.deepseek.com")
)

def get_inventory(product_name: str):
    inventory = {
        "iphone_case": 3,
        "keyboard": 42,
        "mouse": 12,
        "monitor": 5,
    }

    stock = inventory.get(product_name.lower())

    if stock is None:
        return {
            "product": product_name,
            "found": False,
        }

    return {
            "product": product_name,
            "found": True,
            "stock": stock,
        }

tool = [
    {
        "type": "function",
        "function": {
            "name": "get_inventory",
            "description": "Get the inventory of a product.",
            "parameters": {
                "type": "object",
                "properties": {
                    "product_name": {
                        "type": "string",
                        "description": "The name of the product to check inventory for."
                    }
                },
                "required": ["product_name"]
            }
        }
    }
]

messages = [
    {
        "role": "user",
        "content": "How many iphone cases do you have in stock?"
    }
]

response = client.chat.completions.create(
    model="deepseek-flash",
    messages=messages,
    tools=tool,
    
    )

message = response.choices[0].message

print(message)