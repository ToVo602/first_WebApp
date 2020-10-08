# command for activation of venv: venv\Scripts\activate
# set the environment variable: $env:FLASK_APP = "server.py"
# command for enabling debug mode: $env:FLASK_ENV = "development"
# cammand for running the server: flask run
# command for closing server: Strg + c

from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)


@app.route('/')
def start():
    return render_template("index.html")


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

# option before write_to_csv()
# _________________________________
# def write_to_file(data):
#     with open("database.txt", mode="a") as database:
#         email = data["email"]
#         subject = data["subject"]
#         message = data["message"]
#         file = database.write(f"\n{email}, {subject}, {message}")
# __________________________________


def write_to_csv(data):
    with open("database.csv", newline='', mode="a") as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database, delimiter=",",
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect("/thankyou.html")
    else:
        return "something went wrong. Try again! "
    # return "form submitted hooorayyy!"
