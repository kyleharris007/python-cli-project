from flask import Flask, request, jsonify
from peewee import *
from playhouse.shortcuts import model_to_dict, dict_to_model
import json

f = open('master.json')

data = json.load(f)

print(data)

db = PostgresqlDatabase ('anime-characters', user='buccolt45', password='12345', host='localhost', port=5432)

app = Flask(__name__)

class BaseModel(Model):
    class Meta:
        database = db

class Anime(BaseModel):
    AnimeName = CharField()
    CharName = CharField()

db.connect()
db.create_tables([Anime])
db.drop_tables([Anime])
Anime.insert_many(data).execute()

@app.route('/')
def index():
    return 'Welcome to the anime quiz!'
@app.route('/anime', methods=['GET', 'POST'])
@app.route('/anime/<id>', methods=['GET', 'PUT', 'DELETE'])
def endpoint(id=None):
    if request.method == 'GET':
        if id:
            return jsonify(model_to_dict(Anime.get(Anime.id == id)))
        else:
            anime_list = []
            for anime in Anime.select():
                anime_list.append(model_to_dict(anime))
        
    if request.method == 'POST':
        new_anime = dict_to_model(Anime, request.get_json())
        new_anime.save()

    if request.method == 'DELETE':
        Anime.delete().where(Anime.id == id).execute()

app.run(port=5000)
