from flask import Flask, render_template
import edn_format
from sys import argv
import characters

if len(argv) < 1 + 1:
	print "python web.py <data file path>"
	exit(1)

with open(argv[1], 'r') as f:
	data = edn_format.loads(f.read())

app = Flask(__name__)

character_data = {
	"all" : characters.list(data),
}

@app.route('/')
def index():
	return render_template('index.html', characters = character_data['all'])


if __name__ == '__main__':
	app.run(debug = True)