from flask import Flask, render_template, redirect, url_for
import json

app = Flask(__name__)

file = open("animals.json","r")
animal_info = json.load(file)

@app.route("/")
def main():
    return render_template("title_page.html")

@app.route("/intro")
def intro():
    return render_template("page1.html")

@app.route("/endangered-birds-and-animals")
def edab():
    return render_template("page2.html",animals=animal_info['animals'])

@app.route("/thanks_for_watching")
def thanks():
    return render_template("last_page.html")

@app.errorhandler(404)
def not_found(e):
    return redirect(url_for('main'))

if __name__ == "__main__":
    app.run()
