from flask import Blueprint

mail = Blueprint("mail",__name__)

from . import mail_view