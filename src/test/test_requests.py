import requests
import getpass
import urllib
import urllib3

s_url = "https://www.leitstellenspiel.de/users/sign_in"
url = "https://www.leitstellenspiel.de/leitstellenansicht"

payload = {
            "user[email]": "Djomnik",
           'user[password]': "Dk091002$1",
           "user[remember_me]": "1",
           "commit": "Einloggen"

           }

with requests.session() as s:
    p = s.post(s_url, data=payload)
    r = s.get("https://www.leitstellenspiel.de/leitstellenansicht")
with open("request_result.html", "w") as f:
    f.write((r.text))
