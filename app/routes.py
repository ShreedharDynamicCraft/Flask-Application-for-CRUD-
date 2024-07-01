from flask import Blueprint, request, jsonify
from app import mongo
from app.models import User
from bson.objectid import ObjectId

main = Blueprint('main', __name__)

@main.route('/users', methods=['GET'])
def get_users():
    users = mongo.db.users.find()
    return jsonify([User.to_json(user) for user in users])

@main.route('/users/<id>', methods=['GET'])
def get_user(id):
    user = mongo.db.users.find_one({'_id': ObjectId(id)})
    if user:
        return jsonify(User.to_json(user))
    return jsonify({'error': 'User not found'}), 404

@main.route('/users', methods=['POST'])
def create_user():
    data = request.json
    user_data = User.from_json(data)
    mongo.db.users.insert_one(user_data)
    return jsonify({'message': 'User created successfully'})

@main.route('/users/<id>', methods=['PUT'])
def update_user(id):
    data = request.json
    user_data = User.from_json(data)
    mongo.db.users.update_one({'_id': ObjectId(id)}, {'$set': user_data})
    return jsonify({'message': 'User updated successfully'})

@main.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    mongo.db.users.delete_one({'_id': ObjectId(id)})
    return jsonify({'message': 'User deleted successfully'})
