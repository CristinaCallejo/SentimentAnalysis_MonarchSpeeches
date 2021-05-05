from config.configuration import db, collection
from flask import Flask, request, jsonify, make_response

# GET

def all_speeches():
    speeches = list(collection.find({},{"_id":0}))
    return jsonify(speeches)

def yearly_speeches(year):
    q1 = {"year": year}
    q1speeches = list(collection.find(q1,{"_id":0,"name":1, "year":1,"text":1}))
    return jsonify(q1speeches)

