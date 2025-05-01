import requests
from bs4 import BeautifulSoup
from logger import logger

URL = "https://india.diplo.de/in-en/service/2633528-2633528?isLocal=false&isPreview=false&openAccordionId=item-2601184-2-panel"


def fetch_fees():
    try:
        logger.info("Fetching current visa fees...")
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
        logger.info("Fees fetched successfully.")
        logger.debug(f"Fetched fees: {fees}")

        return fees
    except Exception as e:
        logger.error(f"Error fetching fees: {e}")
        raise
