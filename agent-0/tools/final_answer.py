from typing import Any, Optional
from smolagents.tools import Tool


class FinalAnswerTool(Tool):
    name = "final_answer"
    description = "Provides a final answer to the given problem"
    inputs = {
        'answer': {
            'type' : 'any',
            'description' : 'The final answer to the problem'
        }
    }
    output_type = "any"
    
    def forward(self, answer: Any) -> Any:
        """
        This function takes in an answer and returns it as is. 
        This is to be used when the final answer is already known and does not need to be processed further.
        
        Parameters:
            answer (Any): The final answer to the problem
        
        Returns:
            Any: The final answer to the problem
        """
        return answer
    
    def __init__(self, *args, **kwargs):
        """
        Initialize the FinalAnswerTool.
        
        This function does not take any arguments and does not perform any initialization.
        It simply sets the `is_initialized` attribute to False.
        
        Parameters:
            None
        
        Returns:
            None
        """
        self.is_initialized = False