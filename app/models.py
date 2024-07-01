from werkzeug.security import generate_password_hash, check_password_hash
from bson import ObjectId

class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = generate_password_hash(password)

    @staticmethod
    def to_json(user):
        return {
            'id': str(user['_id']),
            'name': user['name'],
            'email': user['email']
        }

    @staticmethod
    def from_json(data):
        return {
            'name': data['name'],
            'email': data['email'],
            'password': generate_password_hash(data['password'])
        }
