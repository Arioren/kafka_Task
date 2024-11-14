from flask import Blueprint, request, jsonify

from app.repository.all_messages import new_email

messages_blueprint = Blueprint('messages_blueprint', __name__)


@messages_blueprint.route('/email', methods=['POST'])
def create_email():
    email = request.json
    res = new_email(email)
    return jsonify(res), 201

