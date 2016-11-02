from flask import Blueprint
from flask import request, jsonify
import traceback

import ttest_ind
import ttest_rel
import shapiro
import mannwhitneyu

functions = [ttest_ind, ttest_rel, shapiro, mannwhitneyu]

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

        return jsonify(result)

    function.__name__ = m.name
    return function


names = []

for m in functions:

    names.append(m.name)

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

    if hasattr(m, 'alias'):
        blueprint.add_url_rule(
            '/' + m.alias,
            endpoint=m.alias + '_get',
            view_func=create_get(m),
            methods=['GET']
        )

        blueprint.add_url_rule(
            '/' + m.alias,
            endpoint=m.alias + '_post',
            view_func=create_post(m),
            methods=['POST']
        )

def get_info():
    return jsonify(dict(functions=names))

blueprint.add_url_rule('/', endpoint='info', view_func=get_info, methods=['GET'])
