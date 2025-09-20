import bcrypt
from flask_jwt_extended import create_access_token
from app.models import User
from app.extensions import db

# criar senha como bcrypt
def hash_password(plain: str):
    return bcrypt.hashpw(plain.encode(), bcrypt.gensalt()).decode()

def check_password(plain: str, hashed: str):
    return bcrypt.checkpw(plain.encode(), hashed.encode())

def create_user(email: str, password: str):
    user = User(email=email,
                password=hash_password(password))
    db.session.add(user)
    db.session.commit()
    return user

def authenticate(email: str, password: str):
    user = User.query.filter_by(email=email).first()
    
    if user and check_password(password, user.password):
        return create_access_token(
            identity=str(user.id),
            additional_claims={"email": user.email}
            )
    return None