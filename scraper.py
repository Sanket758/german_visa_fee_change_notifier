import requests
from bs4 import BeautifulSoup
import logging

URL = "https://india.diplo.de/in-en/service/2633528-2633528?isLocal=false&isPreview=false&openAccordionId=item-2601184-2-panel"


def fetch_fees():
    logging.info("Fetching current visa fees...")
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.find("div", class_="c-table--default")
    rows = table.find_all("tr")[1:]

    fees = {}
    for row in rows:
        cells = row.find_all("td")
        category = cells[0].text.strip()
        inr = cells[1].text.strip()
        eur = cells[2].text.strip()
        fees[category] = {"INR": inr, "EUR": eur}

    return fees
