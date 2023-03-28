import requests
import globals

from web_handler import basic_tasks, web_screpper

with requests.Session() as s:
    basic_tasks.BasicTasks().leiti_login(s)
    r = s.get("https://www.leitstellenspiel.de/buildings/15207201")
    links = web_screpper.HtmlScrepper().get_vehicle_building_links(r.text, "/buildings/15207201")
    print(links)

