import requests

class ISSmodel:
    @staticmethod
    def get_iss_position():
        url= "http://api.open-notify.org/iss-now.json"
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
        except requests.exceptions.Timeout:
                print(f"The request timed out after some seconds")
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
        return data['iss_position']
    
class SunriseModel:
    
    @staticmethod
    def get_sun_rise():
        LAT = 51.924419
        LNG = 4.477733
        parameters = {
                "lat": LAT,
                "lng": LNG
              }
        url="https://api.sunrise-sunset.org/json"
        try:
            response = requests.get(url,params=parameters)
            response.raise_for_status()
            data = response.json()
        except requests.exceptions.Timeout:
            print(f"The request timed out after some seconds")
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
        return data