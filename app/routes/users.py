from flask import Blueprint, request, jsonify
from app.models import User
from app.auth.service import authenticate, create_user
from flask_jwt_extended import jwt_required, get_jwt_identity

bp = Blueprint('users', __name__, url_prefix='/users')

@bp.post("")
def register():
    data = request.get_json() or {}
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'error': 'Email and password are required'}), 400

    if User.query.filter_by(email=email).first():
        return jsonify({'error': 'Email already exists'}), 409
    
    user = create_user(email, password)
    
    return jsonify({'id': user.id, 'email': user.email}), 201