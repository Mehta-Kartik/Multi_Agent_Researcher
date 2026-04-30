from langchain.tools import tool
import requests
from bs4 import BeautifulSoup
from tavily import TavilyClient
import os
from rich import print
from dotenv import load_dotenv
load_dotenv()


tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

@tool
def web_search(query:str)-> str:
    """
    Search the web for recent and reliable information on topic. Returns Titles, URL and snippets
    """
    result=tavily.search(query=query,max_results=6)
    out=[]
    for r in result["results"]:
        out.append(
            f"Title: {r['title']}\nURL: {r['url']}\nSnippet:{r['content'][:300]}\nScore:{r['score']}\nRaw Content:{r['raw_content']}"
        )
    return "\n---\n".join(out)
    # return result

# print(web_search.invoke("News about war"))


@tool
def scrape_url(url:str) -> str:
    """
    Scrape and return clean text context from a given URL for deeper reading.
    """
    try:
        resp= requests.get(url,timeout=8,headers={"User-Agents":"Mozilla/5.0"})
        soup=BeautifulSoup(resp.text,"html.parser")
        for tag in soup(["script","style","nav","footer"]):
            tag.decompose()
        return soup.get_text(separator=" ",strip=True)[:3000]
    except Exception as e:
        return f"Coult not scrape URL: {str(e)}"


# print(scrape_url.invoke("https://www.moneycontrol.com/news/business/markets/sensex-today-stock-market-live-updates-nifty50-share-price-crude-fii-gift-nifty-rupee-latest-updates-27-04-2026-liveblog-13900043.html"))