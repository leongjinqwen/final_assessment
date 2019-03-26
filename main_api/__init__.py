import os
from app import app
from flask_cors import CORS
import sendgrid

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))

## API Routes ##
from main_api.blueprints.users.views import users_api_blueprint
from main_api.blueprints.sessions.views import sessions_api_blueprint

app.register_blueprint(users_api_blueprint, url_prefix='/api/v1/users')
app.register_blueprint(sessions_api_blueprint, url_prefix='/api/v1/')

