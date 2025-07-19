#To-do list:
#   Hour 0-3 - scraping and collect data
#   COMMIT
#   Hour 3-5 - gsap

# I want to scrape links from google 


# import libraries
from flask import Flask, render_template, request, redirect, session, url_for
from model import question_list
from scraper import scrape

app = Flask(__name__)
app.secret_key = 'haardik123'

@app.route("/", methods=['POST', 'GET'])
def main():
    if request.method == 'POST':
        skill = session['skill'] = request.form['skill']
        searches = question_list(skill)
        links = scrape(searches)
        return redirect(url_for("home"))
    else:
        return render_template("index.html")
    
@app.route("/home")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)
