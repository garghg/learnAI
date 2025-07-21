import csv
from flask import Flask, render_template, request, session, redirect, url_for
from model import question_list
from scraper import scrape
import csv

app = Flask(__name__)
app.secret_key = 'haardik123'

# Route to handle the main logic
@app.route("/", methods=['POST', 'GET'])
def main():
    if request.method == 'POST':
        skill = session['skill'] = request.form['skill'] 
        searches = question_list(skill)
        links = scrape(searches)
        session['links'] = links
        
        # Generate the CSV in-memory and send it directly to the user
        create_csv(links)
        return redirect(url_for("home"))
    else:
        return render_template("index.html")

def create_csv(data):
    # Specify the CSV file name
    file_name = "learning_path.csv"

    # Writing to CSV
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        
        # Write the header
        writer.writerow(["Topic", "URL"])

        # Write the rows
        for topic, urls in data.items():
            for url in urls:
                writer.writerow([topic, url])

    print(f"Data has been written to {file_name}")



@app.route("/home")
def home():
    links = session.get('links', {})
    return render_template("home.html", links=links)

if __name__ == "__main__":
    app.run(debug=True)
