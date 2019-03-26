from flask import Blueprint,jsonify,request,make_response
from werkzeug.security import check_password_hash
from models.user import User

sessions_api_blueprint = Blueprint('sessions_api',
                             __name__,
                             template_folder='templates')

@sessions_api_blueprint.route('/login', methods=['POST'])
def sign_in():
    post_data = request.get_json()
    # check whether user already sign up
    user = User.get_or_none(email=post_data.get('email'))
    if user and check_password_hash(user.password, post_data.get('password')):
        auth_token = user.encode_auth_token(user.id)
        responseObject = {
        "auth_token": auth_token.decode(),
        "message": "Successfully signed in.",
        "status": "success",
        "user": {
            "id": int(user.id),
            "email": user.email,
            "username": user.username
            }
        }
        return make_response(jsonify(responseObject)), 201

    else:
        responseObject = {
            "status": "fail",
            "message": "Some error occurred. Please try again."
        }

        return make_response(jsonify(responseObject)), 401

