from bs4 import BeautifulSoup
import globals


class Leitstelle():

    def __init__(self, session):
        self.url = globals.url_dict.get("url")
        self.session = session

    def get_building_ids(self):

        r = self.session.get(f"{self.url}/leitstellenansicht")
        soup = BeautifulSoup(r.text, "html.parser")
        bids = []

        for link in soup.find_all("a"):
            if "/building" in link.get("href"):
                link = link.get("href").split("/")
                bids.append(link[2])

        return bids


