from . import celery_service as celery, create_celery_app

from flask_mail import Mail, Message





@celery.task
def send_async_email(subject, recipients, body, body_type, attachments):
    try:
        app = create_celery_app()


        mail = Mail(app)

        # mail.init_app(app)
        """
        Background task to send an email asynchronously.
        """
        msg = Message(subject, sender="customer@example.com", recipients=recipients)
        
        if body_type == "html":
            msg.html = body
        else:
            msg.body = body

        for attachment in attachments:
            with open(attachment, "rb") as f:
                msg.attach(attachment, "application/octet-stream", f.read())

        with mail.connect() as conn:
            conn.send(msg)
    except Exception as e:
        print("mail error")
        print(e)
        