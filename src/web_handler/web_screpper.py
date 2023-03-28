from bs4 import BeautifulSoup
from class_collection import Building
import globals




class HtmlScrepper:

    def __init__(self):
        self.path_to_resources = globals.path_to_resources
        self.url_dict = globals.url_dict
        self.url_list = {}
        self.building = Building()

    def get_vehicle_building_links(self, html, bid) -> dict:
        soup = BeautifulSoup(html, 'html.parser')
        b = []
        v = []

        for link in soup.find_all("a"):
            if bid in link.get("href"):
                b.append(self.url_dict["url"] + link.get("href"))

            if "/vehicles" in link.get("href") and len(link.get("href")) <= 18:
                v.append(self.url_dict["url"] + link.get("href"))

        self.url_dict["buildings"] = b
        self.url_dict["vehicles"] = v

        return self.url_dict




