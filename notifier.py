import smtplib
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv
from logger import logger
load_dotenv()
import json

EMAIL_ID = os.getenv("EMAIL_ID")
EMAIL_PASS = os.getenv("EMAIL_PASS")
if not EMAIL_ID or not EMAIL_PASS:
    raise EnvironmentError(
        "EMAIL_ID or EMAIL_PASS not set in environment variables.")

with open("subscribers.json", "r") as f:
    recipients = json.load(f)["emails"]

def send_email(subject, body, to_emails=recipients):
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = EMAIL_ID
    msg["To"] = ", ".join(to_emails)
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(EMAIL_ID, EMAIL_PASS)
            server.sendmail(EMAIL_ID, to_emails, msg.as_string())
        logger.info(f"Email sent to: {to_emails}")
    except Exception as e:
        logger.error(f"Error sending email: {e}")
        raise
