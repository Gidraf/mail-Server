import json
import os
from flask import Flask
from flask_cors import CORS
from flask_mail import Mail


from .views import mail as mail_sender



def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.app_context().push()
    with app.app_context():
        app.config["MAIL_SERVER"] = "mail.cvpap.store"
        app.config["MAIL_PORT"] = 587
        app.config["MAIL_USE_TLS"] = True
        app.config["MAIL_USERNAME"] = "customer@example.com"
        app.config["MAIL_PASSWORD"] = "customer-cvpap-password"
        app.register_blueprint(mail_sender)
        CORS(app,supports_credentials=True, origins="*")
        return app
