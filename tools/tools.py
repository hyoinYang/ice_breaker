from langchain_community.tools.tavily_search import TavilySearchResults

# API를 사용한다.
def get_profile_url_tavily(name:str):
    search = TavilySearchResults()
    res = search.run(f"{name}")
    return res