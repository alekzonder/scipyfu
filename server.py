from StringIO import StringIO
from flask import Flask, request, jsonify
import traceback

import functions.stats as stats

app = Flask(__name__)

app.register_blueprint(stats, url_prefix='/stats')

def index():
    return jsonify(dict(modules=['stats']))

app.add_url_rule('/', endpoint="index", view_func=index, methods=['GET'])

# if __name__ == '__main__':
#     app.run()
