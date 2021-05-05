from config.configuration import db, collection
from flask import Flask, request, jsonify, make_response

def generate_sentim():
   speeches = list(collection.find({},{"_id":0}))