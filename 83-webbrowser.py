import webbrowser


def search_on_search_engine(query: str, search_engine: str):
    search_engines = {
        'google': 'https://www.google.com/search?q={}',
        'yahoo': 'https://search.yahoo.com/search?p={}',
        'bing': 'https://www.bing.com/search?q={}'
    }

    if search_engine not in search_engines:
        print("Unsupported search engine:", search_engine)
        return

    search_url = search_engines[search_engine].format(query)

    webbrowser.open(search_url)


search_on_search_engine("Python programming", 'google')
search_on_search_engine("Java programming", 'bing')
