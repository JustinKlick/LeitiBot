from buildings import Buildings
from leitstelle import Leitstelle

import globals


class DataMining:

    def __init__(self, session):
        self.url = globals.url_dict.get("url")
        self.buildings = Buildings(session=session)
        self.leitstelle = Leitstelle(session=session)

