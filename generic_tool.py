from typing import Callable

class Tool:
    """
    A class representing a resuable piece of code -aka Tool
    
    Attributes:
        name (str) : Name of the tool
        description (str) : A textual description of what the tool does
        func (callable) : The function that the tool wraps and executes
        arguments (list) : A list of args - expected inputs
        outputs (str or list) : The return type(s) of the wrapped functions - expected outputs of the tools
    """
    
    def __init__(self, 
                 name: str,
                 description : str,
                 func: Callable,
                 arguments: list,
                 outputs: str):
        self.name = name
        self.description = description
        self.func = func
        self.arguments = arguments
        self.outputs = outputs
        
    def to_string(self) -> str:
        """ 
        Return a string representation of the tool, including
        its name, description, arguments and outputs
        """
        args_str = ", ".join([
            f"{arg_name} : {arg_type}" for arg_name, arg_type in self.arguments
        ])
        
        return (
            f"Tool Name: {self.name},"
            f" Description: {self.description},"
            f" Arguments: {args_str},"
            f" Outputs: {self.outputs}"
        )
        
    def __call__(self, *args, **kwargs):
        """
        Invoke the underlying function (callable) with the provided arguments
        Calls the function when the tool instance is invoked
        """
        return self.func(*args, **kwargs)
    
calculator_tool = Tool(
    "calculator",                       # name
    "Multiply two integers",            # description
    calculator,                         # function to call
    [("a", "int"), ("b", "int")],       # inputs (names, types)
    "int"                               # output
)


@tool
def calculator(a: int, b:int) -> int:
    """
    Multiply two integers
    """
    return a * b
print(calculator.to_string())