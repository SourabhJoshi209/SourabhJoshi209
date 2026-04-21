import requests
import json

def get_ai_news():
    """Search for AI-related stories on Hacker News"""
    url = 'https://hn.algolia.com/api/v1/search'
    params = {
        'query': 'artificial intelligence OR AI',
        'tags': 'story',
        'hitsPerPage': 5,
        'numericFilters': 'created_at_i>0',
        'sort': 'by_popularity'  # Changed from 'published_at' - may not be valid
    }
    
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()  # Raise exception for bad status codes
        data = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching from API: {e}")
        return []
    
    # Debug: Print the actual response
    print(f"DEBUG: API Response keys: {data.keys()}")
    
    # Check for hits key
    if 'hits' not in data:
        print(f"Warning: 'hits' key not found in API response. Keys found: {list(data.keys())}")
        return []
    
    news_items = []
    for hit in data['hits']:
        title = hit.get('title', 'No title')
        url = hit.get('url', '#')
        if title and url:
            news_items.append(f"- [{title}]({url})")
    
    return news_items

def generate_markdown():
    """Generate the markdown section"""
    news = get_ai_news()
    if not news:
        return "## 🚀 Latest AI News (Updated daily)\n\n*Unable to fetch news at this time.*\n"
    
    header = "## 🚀 Latest AI News (Updated daily)\n"
    return header + '\n'.join(news)

if __name__ == "__main__":
    print(generate_markdown())
