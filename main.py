import json
import os
from scraper import fetch_fees
from notifier import send_email
from logger import logger

DATA_FILE = "data.json"


def load_previous_data():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r") as f:
        return json.load(f)


def save_current_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)


def _build_msg_body(new_data, old_data):
    message = "Hello,\n\nThe German Embassy visa fees have been updated. Below are the changes detected:\n\n"
    print(new_data, type(new_data))
    for category, fees in new_data.items():
        old_fees = old_data.get(category, {})

        old_inr = old_fees.get('INR', "Not Available")
        old_eur = old_fees.get('EUR', "Not Available")

        new_inr = fees['INR']
        new_eur = fees['EUR']

        if old_fees != fees:
            message += f"{category}:\n    - Previously: INR {old_inr} / {old_eur}\n    - Has been Updated to: INR {new_inr} / {new_eur}\n\n"

    message += "Source: https://india.diplo.de/in-en/service/2633528-2633528?isLocal=false&isPreview=false&openAccordionId=item-2601184-2-panel\n\n"
    message += "Please note that these changes are effective immediately. If you have already made a demand draft (DD) for your visa application, please ensure it matches the updated fee amount before your appointment.\n\n"
    message += "Regards,\nVisa Fee Change Notifier"
    # message += "\n\nThis is an auto generated message. Please do not reply to this email."
    return message


def compare_and_notify(new_data, old_data):
    if new_data != old_data:
        logger.info("Change detected in visa fees.")
        message = _build_msg_body(new_data, old_data)
        save_current_data(new_data)
        logger.info('Sending email notification...')
        send_email("Visa Fee Update Detected", message)


if __name__ == "__main__":
    old_data = load_previous_data()
    new_data = fetch_fees()
    compare_and_notify(new_data, old_data)
