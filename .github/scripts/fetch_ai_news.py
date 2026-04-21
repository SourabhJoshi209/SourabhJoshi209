import requests

url = "https://ai10.p.rapidapi.com/people/artificial-intelligence/page/1/"

headers = {
    "x-rapidapi-key": "049d5d74e4mshf33b7246f77d0cep103c48jsnaa27e6b0062b",
    "x-rapidapi-host": "ai10.p.rapidapi.com",
    "Content-Type": "application/json"
}

try:
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()
    data = response.json()
    print(data)
except requests.exceptions.RequestException as e:
    print(f"Error fetching from RapidAPI: {e}")
