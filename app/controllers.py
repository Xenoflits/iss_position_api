from app.models import ISSmodel,SunriseModel

class ISScontroller:
    @staticmethod
    def fetch_iss_position():
        return ISSmodel.get_iss_position()
    
class Sunrisecontroller:
    @staticmethod
    def fetch_sunrise():
        print(f"at controller {SunriseModel.get_sun_rise()}")
        return SunriseModel.get_sun_rise()
    
