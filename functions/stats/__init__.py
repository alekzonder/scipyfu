from flask import Blueprint
from flask import request, jsonify
import traceback

import ttest_ind
import ttest_rel

functions = [ttest_ind, ttest_rel]

blueprint = Blueprint('stats', __name__)


def create_get(m):
    def function():
        return jsonify(m.info)

    function.__name__ = m.name
    return function


def create_post(m):

    def function():
        data = request.get_json()

        try:
            result = m.fn(data)
        except:
            tb = traceback.format_exc()
            return tb, 500

        return jsonify({'result': result})

    function.__name__ = m.name
    return function


for m in functions:
    blueprint.add_url_rule(
        '/' + m.name,
        endpoint=m.name + '_get',
        view_func=create_get(m),
        methods=['GET']
    )

    blueprint.add_url_rule(
        '/' + m.name,
        endpoint=m.name + '_post',
        view_func=create_post(m),
        methods=['POST']
    )
