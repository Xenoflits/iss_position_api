import requests

class ISSmodel:
    @staticmethod
    def get_iss_position():
        url= "http://api.open-notify.org/iss-now.json"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data['iss_position']