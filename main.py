from flask import Flask, request, jsonify
import tools.grabber as grab
import tools.postdata as pos
import json
import markdown.extensions.fenced_code

app = Flask(__name__)


# LANDING PAGE

@app.route("/")
def landing():
    readme = open("README.md", "r")
    md_template = markdown.markdown(
        readme.read(), 
        extensions= ["fenced_code"]
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


# GET examples:

"""
urlbase = "http://localhost:5000/"
# resp_base = requests.get(urlbase)
# resp_base.content

urlspeeches = "http://localhost:5000/speeches"

urlyear = "http://localhost:5000/speeches/<year>"
# year = 2012
# end = f"speeches/{year}"
# endpoint=urlbase+end
# resp_year = requests.get(endpoint).json()
# resp_year

"""

# POST

@app.route("/speeches/new", methods=["POST"])
def add_speech():
    name = request.form.get("name")
    year = request.form.get("year")
    text = request.form.get("text")
    pos.insert_speech(name,year,text)
    return "Succesfully added speech to database!"


# POST examples:

"""
urladd = "http://localhost:5000/speeches/new"
show = requests.post(urladd, data=juanq_dic)
show.content
"""


app.run("localhost",5000, debug=True)













