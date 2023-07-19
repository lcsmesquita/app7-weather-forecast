import requests
API_KEY = "a64519886ff4c69e503d31f6b4536daf"


def get_data(place, forecast_days=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&units=metric&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data['list']
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[0:nr_values]
    return filtered_data

if __name__ == "__main__":
    print(get_data("Tokyo", 3))

