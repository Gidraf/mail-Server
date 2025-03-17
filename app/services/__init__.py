from celery import Celery
from flask import Flask
import os

celery_service = Celery('send_mail', backend='redis://127.0.0.1:6379/0', broker='redis://127.0.0.1:6379/0')

celery_service.conf.update(
    task_routes={
        'mail.*': {'queue': 'mail'},
    },
    worker_concurrency=4,
    worker_pool='eventlet',
    task_acks_late=True,
    worker_prefetch_multiplier=1,
    worker_max_tasks_per_child=100,  # Restart workers after 100 tasks to avoid memory leaks
    worker_max_memory_per_child=120000,
)

# Email credentials & server details
EMAIL_ADDRESS = "customer@cvpap.store"
EMAIL_PASSWORD = "customer-cvpap-password"
SMTP_SERVER = "mail.cvpap.store"
IMAP_SERVER = "mail.cvpap.store"
SMTP_PORT = 587
IMAP_PORT = 993

def create_celery_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config["MAIL_SERVER"] = SMTP_SERVER
    app.config["MAIL_PORT"] = SMTP_PORT
    app.config["MAIL_USE_TLS"] = True
    app.config["MAIL_USERNAME"] = EMAIL_ADDRESS
    app.config["MAIL_PASSWORD"] = EMAIL_PASSWORD
    return app