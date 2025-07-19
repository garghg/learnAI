from huggingface_hub import InferenceClient
import ast

links = [
    "https://realpython.com/tutorials/beginner/",  # Real Python Beginner Tutorials
    "https://www.w3schools.com/python/",  # W3Schools Python Tutorial
    "https://docs.python.org/3/tutorial/",  # Official Python Docs (Beginner-Friendly)
    "https://www.freecodecamp.org/news/learn-python-by-building-projects/",  # FreeCodeCamp: Learn Python by Building Projects
    "https://www.learnpython.org/",  # Learn Python (Interactive)
    "https://www.codecademy.com/learn/learn-python-3",  # Codecademy Python 3 Course
    "https://www.python-course.eu/python3_course.php",  # Python Course (Intermediate to Advanced)
    "https://www.kaggle.com/learn/python",  # Kaggle Python for Data Science (Advanced Projects)
    "https://www.geeksforgeeks.org/python-programming-language/",  # GeeksforGeeks Python Tutorials
    "https://www.edx.org/course/introduction-to-python-programming-2",  # edX Python Introduction (Free Course)
    "https://www.udemy.com/course/complete-python-bootcamp/",  # Udemy: Complete Python Bootcamp (Comprehensive)
    "https://www.pybites.io/",  # PyBites (Advanced Python Challenges)
    "https://www.youtube.com/watch?v=rfscVS0vtbw",  # FreeCodeCamp: Python Tutorial for Beginners (YouTube)
    "https://automatetheboringstuff.com/",  # Automate the Boring Stuff with Python (Beginner to Intermediate)
    "https://realpython.com/python-oop/",  # Real Python Object-Oriented Programming (Advanced)
    "https://www.tutorialspoint.com/python/index.htm",  # TutorialsPoint Python Tutorials
    "https://www.fullstackpython.com/lessons.html",  # Full Stack Python (Advanced Topics)
    "https://www.programiz.com/python-programming",  # Programiz Python Programming
    "https://www.coursera.org/specializations/python",  # Coursera Python for Everybody Specialization (Beginner to Intermediate)
    "https://www.pythontutorial.net/",  # Python Tutorial (Clear Beginner Guide)
]


client = InferenceClient(
    provider="auto",
    api_key="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",
)


ranking = client.chat.completions.create(
    model="meta-llama/Llama-3.1-8B-Instruct",
    messages=[
        {
            "role": "user",
            "content": f"""I will provide a list of links that teach Python.
            Please rank these links from beginner to advanced based on their content. Do not generate new links, just rank the ones I provide.
            Here's the links: {links}
            Now tell me the reasoning behind your ranking choices."""
        }
    ],
)


def question_list(skill):
    questions = client.chat.completions.create(
        model="meta-llama/Llama-3.1-8B-Instruct",
        messages=[
            {
                "role": "user",
                "content": f"""I wish to scrape links from the web to learn {skill}. Give me an iterable python list of queries I can search from beginner to advanced to get useful links.
                NO additonal text."""
            }
        ],
    )
    return ast.literal_eval(questions.choices[0].message.content)