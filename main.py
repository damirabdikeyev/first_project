import os
from dotenv import load_dotenv

load_dotenv('pass.env')


def print_author():
    author = os.getenv('AUTHOR')
    print(f"Дамир: {author}")


print_author()
