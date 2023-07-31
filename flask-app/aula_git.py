'''Servidor flask de páginas estáticas.'''

from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', defaults={'path': 'index'})
@app.route('/<path:path>')
def view(path):
    return render_template(path+'.html')
