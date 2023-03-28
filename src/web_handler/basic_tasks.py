import requests
import globals


class BasicTasks:
    """handles basic tasks:
        - login
        - get buildings
        - get vehicles
        - get daily logins
        - get value coins
        - get value credits
        - get new workers
        - get new vehicles
        - upgrade buildings
    """

    def __init__(self):
        self.user_name = globals.user_name
        self.user_pw = globals.user_pw
        self.path_to_resources = globals.path_to_resources
        self.url_dict = globals.url_dict

    def leiti_login(self, session):
        payload = {
            "user[email]": self.user_name,
            'user[password]': self.user_pw,
            "user[remember_me]": "1",
            "commit": "Einloggen"
        }

        session.post(self.url_dict["login"], data=payload)

