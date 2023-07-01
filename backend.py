import requests
API_KEY = "2c1d72cfde09aa1d191abee711142fb6"
def get_data(station, days):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={station}&appid={API_KEY}"
    response = requests.get(url)
    datas = response.json()
    filter_data = datas["list"]
    exact_data = filter_data[:days*8]
    dates = [date["dt_txt"] for date in exact_data]
    return exact_data
if __name__ == "__main__":
    get_data("Tokyo", 3)

