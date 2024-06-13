from app.models import ISSmodel

class ISScontroller:
    @staticmethod
    def fetch_iss_position():
        return ISSmodel.get_iss_position()