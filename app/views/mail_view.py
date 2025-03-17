from flask import Flask, request, jsonify
from flask_mail import Mail, Message

from app.services.mail_services import send_async_email
from . import mail as mail_sender 



@mail_sender.route("/api/v1/send", methods=["POST"])
def send_email():
    try:
        """
        Endpoint to send emails asynchronously using Celery.
        """
        data = request.json
        recipients = data.get("to", [])
        subject = data.get("subject", "No Subject")
        body = data.get("body", "")
        body_type = data.get("body_type", "text")  # Can be "text" or "html"
        attachments = data.get("attachments", [])

        if not recipients:
            return jsonify({"error": "Recipient email is required"}), 400

        task = send_async_email.apply_async(args=[subject, recipients, body, body_type, attachments])

        return jsonify({"message": "Email is being sent!", "task_id": task.id}), 202
    
    except Exception as e:
        print(e)
        return e