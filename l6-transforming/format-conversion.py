from IPython.display import display, Markdown, Latex, HTML, JSON
import openai
import os

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())  # read local .env file

openai.api_key = os.getenv('OPENAI_API_KEY')


def get_completion(prompt, model="gpt-3.5-turbo", temperature=0):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
    )
    return response.choices[0].message["content"]


data_json = {"resturant employees": [
    {"name": "Shyam", "email": "shyamjaiswal@gmail.com"},
    {"name": "Bob", "email": "bob32@gmail.com"},
    {"name": "Jai", "email": "jai87@gmail.com"}
]}

prompt = f"""
Translate the following python dictionary from JSON to an HTML \
table with column headers and title: {data_json}
"""
response = get_completion(prompt)
print(response)


display(HTML(response))
