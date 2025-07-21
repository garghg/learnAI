#To-do list:
#   scraping and collect data 
#   stytling
#       - https://docs.scrapy.org/en/latest/intro/tutorial.html
#   add a loading screen 
#   full stack app structure and npm installation
#   cursor: https://dev.to/uuuuuulala/coding-an-interactive-and-damn-satisfying-cursor-7-simple-steps-2kb-of-code-1c8b
#   add comments


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
