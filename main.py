from flask import Flask, request, jsonify
import tools.grabber as grab
import tools.postdata as pos
import tools.sentiment as sent
import json
import markdown.extensions.fenced_code

app = Flask(__name__)


# LANDING PAGE

@app.route("/")
def landing():
    readme_file = open("Readme.md", "r")
    md_template = markdown.markdown( 
        readme_file.read(), extensions=["fenced_code"]
    )
    return md_template

# GET 

@app.route("/speeches")
def find_all_speeches():
    speeches= grab.all_speeches()
    return speeches

@app.route("/speeches/<year>")
def find_per_year(year):
    per_year= grab.yearly_speeches(year)
    return per_year

# POST

@app.route("/speeches/new", methods=["POST"])
def add_speech():
    name = request.form.get("name")
    year = request.form.get("year")
    text = request.form.get("text")
    pos.insert_speech(name,year,text)
    return "Succesfully added speech to database!"

# SENTIMENT ANALYSIS

@app.route('/sentiment')
def sentim_all():
    sentim = sent.generate_sentim()
    return sentim


app.run("localhost",5000, debug=True)













