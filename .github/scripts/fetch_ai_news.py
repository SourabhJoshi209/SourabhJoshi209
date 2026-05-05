import requests

url = "https://ai-news-global.p.rapidapi.com/get_news/v1/ai"

headers = {
	"x-rapidapi-key": "049d5d74e4mshf33b7246f77d0cep103c48jsnaa27e6b0062b",
	"x-rapidapi-host": "ai-news-global.p.rapidapi.com",
	"Content-Type": "application/json"
}

response = requests.get(url, headers=headers)

print(response.json())
