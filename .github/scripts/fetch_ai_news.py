import requests

url = "https://technology-news3.p.rapidapi.com/news"

headers = {
	"x-rapidapi-key": "049d5d74e4mshf33b7246f77d0cep103c48jsnaa27e6b0062b",
	"x-rapidapi-host": "technology-news3.p.rapidapi.com",
	"Content-Type": "application/json"
}

response = requests.get(url, headers=headers)

news_list = response.json()

for article in news_list[:3]:
    print(f"{article['title']}")
    print(f"Link: {article['url']}")
    print("-" * 20)
