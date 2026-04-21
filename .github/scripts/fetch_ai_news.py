import requests

# Search for AI-related stories on Hacker News
def get_ai_news():
    # Search query for AI-related posts (using the HN search API)
    url = 'https://hn.algolia.com/api/v1/search'
    params = {
        'query': 'artificial intelligence OR AI',
        'tags': 'story',
        'hitsPerPage': 5,
        'numericFilters': 'created_at_i>0',  # recent stories
        'sort': 'published_at',
        'order': 'desc'
    }
    response = requests.get(url, params=params)
    data = response.json()

    news_items = []
    for hit in data['hits']:
        title = hit['title']
        url = hit['url']
        news_items.append(f"- [{title}]({url})")
    return news_items

# Generate the markdown section
def generate_markdown():
    news = get_ai_news()
    header = "## 🚀 Latest AI News (Updated daily)\n"
    return header + '\n'.join(news)

if __name__ == "__main__":
    print(generate_markdown())
