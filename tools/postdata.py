from config.configuration import db, collection
from flask import Flask, request, jsonify, make_response

# POST

def insert_speech(name,year,text):

        """
        Inserts data into mongoDB

        Receives variables storing data to insert into mongoDB as a document
        Converts into dictionary, inserts in mongoDB collection

        """
    to_insert = {"name": name, "year": year, "text": text}
    inserted = collection.insert_one(to_insert)
    return inserted.inserted_id







