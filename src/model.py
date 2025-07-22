from huggingface_hub import InferenceClient
import ast
import os

python_list = [
    "learn python for beginners",
    "python basic syntax tutorial",
    "python variables and data types",
    "python control structures tutorial",
    "learn python functions and methods",
    "python list comprehension guide",
    "learn object-oriented programming in python",
    "python modules and libraries tutorial",
    "understanding python decorators",
    "python error handling and exceptions",
    "advanced python data structures",
    "python regular expressions tutorial",
    "learn python file handling",
    "python web scraping tutorial",
    "python working with APIs",
    "python database interaction tutorial",
    "learn python threading and multiprocessing",
    "python advanced algorithms and problem solving",
    "deep dive into python memory management",
    "master python with data science",
    "python machine learning basics",
    "learn python for data analysis",
    "python advanced techniques for performance optimization",
    "python functional programming concepts",
    "understanding python's async and await",
    "learn testing in python with pytest",
    "python design patterns",
    "learn python GUI programming",
    "python networking and socket programming",
    "advanced python techniques and tips"
]


client = InferenceClient(
    provider="novita",
    api_key=os.environ["HUGGING_FACE_API_KEY"]
)

def question_list(skill):
    questions = client.chat.completions.create(
        model="meta-llama/Llama-3.1-8B-Instruct",
        messages=[
            {
                "role": "user",
                "content": f"""I wish to scrape links from the web to learn {skill}.
                Give me a python list of queries I can search from beginner to advanced to get useful links.
                Make sure the python list is properly formatted with valid syntax containting only strings (no numbers or special characters).
                NO additonal text. Just output a python list as specified"""
            }
        ],
    )

    try:
        return ast.literal_eval(questions.choices[0].message.content)
    except:
        return python_list