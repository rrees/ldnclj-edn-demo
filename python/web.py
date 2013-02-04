from flask import Flask, render_template
import clj
from sys import argv
import characters

if len(argv) < 1 + 1:
	print "python web.py <data file path>"
	exit(1)

with open(argv[1], 'r') as f:
	data = clj.load(f)

app = Flask(__name__)

def attribute_filter(name, min_score):
	return lambda x : x[name]['score'] >= min_score

character_data = {
	"all" : map(characters.as_template_data, data),
	"fighters" : map(characters.as_template_data, [c for c in data if attribute_filter('strength', 16)(c)]),
	"clerics" : map(characters.as_template_data, filter(attribute_filter('wisdom', 16), data)),
}

print data[0]
print character_data['all'][0]
print character_data['fighters'][0]
print len(data), len(character_data['all']), len(character_data['fighters'])

@app.route('/')
def index():
	return render_template('index.html',
		label = "all",
		characters = character_data['all'])

@app.route('/fighters')
def fighters():
	return render_template('index.html',
		label = "fighters",
		characters = character_data['fighters'])

@app.route('/clerics')
def clerics():
	return render_template('index.html',
		label = "clerics",
		characters = character_data['clerics'])

if __name__ == '__main__':
	app.run(debug = True)