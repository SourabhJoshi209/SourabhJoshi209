import requests

url = "https://technology-news3.p.rapidapi.com/news"

headers = {
	"x-rapidapi-key": "049d5d74e4mshf33b7246f77d0cep103c48jsnaa27e6b0062b",
	"x-rapidapi-host": "technology-news3.p.rapidapi.com",
	"Content-Type": "application/json"
}

response = requests.get(url, headers=headers)

print(response.json())
