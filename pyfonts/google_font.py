import requests


def _load_font_from_google():
    url = "https://www.googleapis.com/webfonts/v1/webfonts?key=AIzaSyBkOYsZREsyZWvbSR_d03SI5XX30cIapYo&sort=popularity"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print(data)
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")


if __name__ == "__main__":
    _load_font_from_google()
