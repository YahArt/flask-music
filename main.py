
from flask import Flask
from flask import render_template
from flask import request
from flask import url_for
import os
import json

app = Flask("flask-music")

def load_songs():
	songs_path = os.path.join(
		app.static_folder, 'json', 'songs.json')
	with open(songs_path, encoding='utf-8') as json_file:
		json_data = json.load(json_file)
	return json_data

def find_songs(song_name):
	songs = load_songs()
	found_songs = { "songs": [] }
	for song in songs:
		if song["song"] == song_name:
			found_songs['songs'].append(song)
	return found_songs


@app.route('/', methods=['GET', 'POST'])
def index():
	return render_template('index.html')


@app.route('/songs', methods=['POST'])
def song():
	song_name = request.form.get('song')
	found_songs = find_songs(song_name)
	return found_songs


@app.route('/data')
def data():
	return render_template('data.html')

if __name__ == "__main__":
	app.run(debug=True, port=5000)