from flask import Blueprint, request, jsonify

from app.repository.all_messages import new_email, get_person_by_email, most_common_word

messages_blueprint = Blueprint('messages_blueprint', __name__)


@messages_blueprint.route('/email', methods=['POST'])
def create_email():
    email = request.json
    res = new_email(email)
    return jsonify(res), 201


@messages_blueprint.route('/email/<email>', methods=['GET'])
def get_email(email):
    res = get_person_by_email(email)
    return jsonify(res), 200


@messages_blueprint.route('/email/most_common_word', methods=['GET'])
def get_most_common_word():
    res = most_common_word()
    return jsonify(res), 200

