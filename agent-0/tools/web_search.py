from typing import Any, Optional
from smolagents.tools import Tool
import duckduckgo_search


class DuckDuckGoSearchTool(Tool):
    name = "web_search"
    description = "Perfoms a duckduckgo search based on the user query and returns the top search results"
    inputs = {
        'query': {
            'type' : 'string',
            'description': 'The search query to perform'
        }
    }
    output_type = "string"
    
    def __init__(self, max_results=10, **kwargs):
        """
        Initialize the DuckDuckGoSearchTool.
        
        Parameters:
            max_results (int, optional): The maximum number of search results to return. Defaults to 10.
            **kwargs (dict): Additional keyword arguments to pass to the DDGS constructor.
        
        Raises:
            ImportError: If the `duckduckgo_search` package is not installed.
        """
        super().__init__()
        self.max_results = max_results
        try:
            from duckduckgo_search import DDGS
        except ImportError as e:
            raise ImportError(
                "You must install package `duckduckgo_search` to run this tool: for instance run `pip installl duckduckgo-search`."
            ) from e 
            self.ddgs = DDGS(**kwargs)
            
            
    def forward(self, query: str) -> str:
        """
        Perform a duckduckgo search based on the user query and returns the top search results
        Parameters:
            query (str): The search query to perform
        Returns:
            str: A string containing the search results in markdown format
        Raises:
            Exception: If no results are found
        """
        results = self.ddgs.text(query, max_results=self.max_results)
        if len(results) == 0:
            raise Exception("No results found! Try a less restrictive or shorter query") # more reason to use uncensored LLMs
        postprocessed_results = [f"[{result['title']}]({result['href']})\n{result['body']}" for result in results]
        return "## Search Results\n\n" + "\n\n".join(postprocessed_results)