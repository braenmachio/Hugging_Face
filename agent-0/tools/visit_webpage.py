from typing import Any, Optional
from smolagents.tools import Tool
import requests, markdownify, smolagents


class VisitWebpageTool(Tool):
    name = "visit_webpage"
    description = "Visits a webpage at the given url and reads its contents as markdown string. Use this to browse webpages"
    inputs = {
        'url' : {
            'type' : 'string',
            'description' : 'This is the URL of the webpage to visit'
        }
    }
    output_type = "string"
    
    def forward(self, url: str) -> str:
        """
        Visits a webpage at the given url and reads its contents as markdown string.
        
        Parameters:
            url (str): The URL of the webpage to visit
        
        Returns:
            str: The contents of the webpage as a markdown string
        
        Raises:
            ImportError: If the `markdownify` or `requests` package is not installed.
            requests.exceptions.Timeout: If the request to the webpage times out.
            RequestException: If there is an error with the request to the webpage.
            Exception: If an unexpected error occurs.
        """
        try:
            import requests
            from markdownify import markdownify
            from requests.exceptions import RequestException
            
            from smolagents.utils import truncate_content
        except ImportError as e:
            raise ImportError(
                "You must install packages `markdownify` and `requests` to run this tool: for instance run `pip install markdownify requests`."
            ) from e
        try:
            # Send a GET request to the url with a 10 second timeout
            response = requests.get(url, timeout=10)
            response.raise_for_status()  # raise an exception for bad status codes
            
            # Convert the HTML into Markdown
            markdown_content = markdownify(response.text).strip()
            
            # Remove multiple line breaks
            markdown_content = re.sub(r"\n{3,}", "\n\n", markdown_content)
            
            return truncate_content(markdown_content, 1000)
        
        except requests.exceptions.Timeout:
            return "The request timed out, please try again later or check the URL."
        except RequestException as e:
            return f"Error fetching the webpage: {str(e)}"
        except Exception as e:
            return f"An unexpected error occured: {str(e)}"
        
    def __init__(self, *args, **kwargs):
        """
        Initialize the VisitWebpageTool.
        
        Parameters:
            *args (Any): Unused, only for compatibility with base class
            **kwargs (dict): Unused, only for compatibility with base class
        
        Returns:
            None
        """
        self.is_initialized = False