import requests
API_KEY = "2c1d72cfde09aa1d191abee711142fb6"
def get_data(station, days=None):
    url = f"api.openweathermap.org/data/2.5/forecast?q={station}&appid={API_KEY}"
    response = requests.get(url)
    datas = response.json()
    return datas
if __name__ == "__main__":
    get_data("Tokyo")

