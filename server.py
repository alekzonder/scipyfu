from StringIO import StringIO
from flask import Flask, request, jsonify
import traceback

import functions.stats as stats

app = Flask(__name__)

app.register_blueprint(stats, url_prefix='/stats')

# if __name__ == '__main__':
#     app.run()
