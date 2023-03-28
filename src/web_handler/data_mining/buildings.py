from leitstelle import Leitstelle

import globals


class Buildings(Leitstelle):

    def __init__(self, session):
        super().__init__(session)
        self.url = globals.url_dict.get("url")
        self.session = session

    def get_building_data(self, bid):

        self.session.get(f"{self.url}/{bid}")


