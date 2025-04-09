# blockbeats_server.py
import httpx
from mcp.server.fastmcp import FastMCP
from datetime import datetime

# Initialize MCP server
mcp = FastMCP("BlockBeats News", dependencies=["httpx"])

# Base URL for BlockBeats API
BASE_URL = "https://api.theblockbeats.news/v1"

# Helper function to fetch data from BlockBeats API
async def fetch_blockbeats_data(endpoint: str, params: dict = None) -> dict:
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(f"{BASE_URL}/{endpoint}", params=params)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPError as e:
            return {"error": str(e)}

# Helper function to convert Unix timestamp to human-readable local time string
def timestamp_to_human_readable(timestamp: str) -> str:
    try:
        # Convert string timestamp to integer and then to local datetime
        dt = datetime.fromtimestamp(int(timestamp))
        return dt.strftime("%Y-%m-%d %H:%M:%S")
    except (ValueError, TypeError):
        return "Invalid timestamp"

# Tools
@mcp.tool()
async def get_latest_news(size: int = 5, max_pages: int = 1, type: str = "push", lang: str = "en") -> str:
    """
    Fetch the latest blockchain fast news articles up to max_pages.

    Parameters:
        size (int): Number of articles per page (default: 5).
        max_pages (int): Maximum number of pages to fetch (default: 1).
        type (str): News type filter, e.g., 'push' for important news (default: 'push').
        lang (str): Language of the news, 'en' for English, 'cn' for Simplified Chinese, 'cht' for Traditional Chinese (default: 'en').
    """
    all_articles = []
    for page in range(1, max_pages + 1):
        params = {"page": page, "size": size, "type": type, "lang": lang}
        data = await fetch_blockbeats_data("open-api/open-flash", params=params)
        if "error" in data or data.get("status") != 0:
            return f"Error fetching news: {data.get('error', data.get('message', 'Unknown error'))}"
        
        articles = data.get("data", {}).get("data", [])
        if not articles:
            break  # No more articles to fetch
        
        all_articles.extend(articles)
    
    if not all_articles:
        return "No fast news articles found."
    
    return "\n\n".join(
        f"ID: {article['id']}\n"
        f"Title: {article['title']}\n"
        f"Content: {article['content']}\n"
        f"Link: {article['link']}\n"
        f"Created: {timestamp_to_human_readable(article['create_time'])}"
        for article in all_articles
    )

@mcp.tool()
async def get_latest_articles(size: int = 5, max_pages: int = 1, type: str = "push", lang: str = "en") -> str:
    """
    Fetch the latest blockchain in-depth articles up to max_pages.

    Parameters:
        size (int): Number of articles per page (default: 5).
        max_pages (int): Maximum number of pages to fetch (default: 1).
        type (str): Article type filter, e.g., 'push' for important articles (default: 'push').
        lang (str): Language of the articles, 'en' for English, 'cn' for Simplified Chinese, 'cht' for Traditional Chinese (default: 'en').
    """
    all_articles = []
    for page in range(1, max_pages + 1):
        params = {"page": page, "size": size, "type": type, "lang": lang}
        data = await fetch_blockbeats_data("open-api/open-information", params=params)
        if "error" in data or data.get("status") != 0:
            return f"Error fetching articles: {data.get('error', data.get('message', 'Unknown error'))}"
        
        articles = data.get("data", {}).get("data", [])
        if not articles:
            break  # No more articles to fetch
        
        all_articles.extend(articles)
    
    if not all_articles:
        return "No in-depth articles found."
    
    return "\n\n".join(
        f"Title: {article['title']}\n"
        f"Description: {article['description']}\n"
        f"Content: {article['content'][:200]}...\n"
        f"Link: {article['link']}\n"
        f"Created: {timestamp_to_human_readable(article['create_time'])}"
        for article in all_articles
    )

# Main execution
if __name__ == "__main__":
    mcp.run()