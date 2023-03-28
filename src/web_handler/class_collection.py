class Building:
    def __init__(self):
        self.name: str = ""
        self.url: str = ""
        self.type: str = ""
        self.stufe: int = 0
        self.max_stufe: int = 0
        self.personal: int = 0
        self.ziel_personal: int = 0
        self.max_anz_fahrzeuge: int = 0
        self.anz_fahrzeuge: int = 0
        self.farzeuge = Vehicles()
        self.links: dict = {
            "Ausbauen": self.url + "/expand",
            "F-Markt": self.url + "/vehicles/new",
            "Personal": self.url + "/personals",
            "P new": self.url + "/hire",
        }
        self.ausbauten: dict = {}
        self.komplex: dict = {}
        self.spezialisierung: dict = {}


class Vehicles:

    def __init__(self):
        self.name: str = ""
        self.typ = VehicleType()
        self.personal: int = 0


class VehicleType:

    def __init__(self):
        self.type: str = ""
        self.max_personal: str = ""
        self.qualification: str = ""


class Missons:

    def __init__(self):
        self.id: MissonsId()
        self.name: str = ""
        self.time: int = 0
        self.rest_time: int = 0
        self.anz_patient: int = 0
        self.vehicle_used: dict = {}

class MissonsId:

    def __init__(self):
        self.id: int = 0
        self.wanted_vehicles: dict = {}
        
