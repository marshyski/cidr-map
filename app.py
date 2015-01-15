import flask
from flask import render_template
from jinja2 import Environment
from jinja2.loaders import FileSystemLoader
import glob, os
 
app = flask.Flask(__name__)
 
@app.route('/')
def index():
    def inner():
        zones = glob.glob('data/*.zone')
        for country in zones:
	    base = os.path.basename(country)
            name = base.split('.')[0]
            openme = open(country, 'r')
            lines = openme.read().splitlines()
            yield '{ "hc-key": "%s", "code": %s },' % (name, lines)
    env = Environment(loader=FileSystemLoader('templates'))
    tmpl = env.get_template('index.html')
    return flask.Response(tmpl.generate(result=inner()))
 
if __name__ == "__main__":
	app.run(debug=False, host='0.0.0.0', port=8080)
