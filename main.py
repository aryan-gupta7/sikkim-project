from flask import Flask, render_template, redirect, url_for
import json

app = Flask(__name__)

file = open("animals.json","r")
animals = json.load(file)
anis = animals['animals']

@app.route("/")
def main():
    return render_template("title_page.html")

@app.route("/intro")
def intro():
    return render_template("page1.html")

@app.route("/endangered-birds-and-animals")
def edab():
    return render_template("page2.html",animals=animals['animals'])

@app.route("/thanks_for_watching")
def thanks():
    return render_template("last_page.html")

@app.route("/animal_info/<animal_name>")
def animal_info(animal_name):
    for animal in anis:
        animal = anis[animal]
        if animal['sname'] == animal_name:
            return render_template("show_animal.html",animal=animal)

@app.errorhandler(404)
def not_found(e):
    return redirect(url_for('main'))

if __name__ == "__main__":
    app.run(debug=True)
