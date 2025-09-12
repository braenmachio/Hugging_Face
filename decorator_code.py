import inspect

def tool(func):
    """ 
    A decorator that creates a Tool instance from the given function
    """
    
    # Get the function signature
    signature = inspect.signature(func)
    
    # We are to extract (param_name, param_annotation) pairs for inputs
    arguments = []
    for param in signature.parameters.values():
        annotation_name = (
            param.annotation.__name__
            if hasattr(param.annotation, '__name__')
            else str(param.annotation)
        )
        arguments.append(param.name, annotation_name)
        
    # We determine the return annotation
    return_annotation = signature.return_annotation
    if return_annotation is inspect._empty:
        outputs = "No return annotation"
    else:
        outputs = (
            return_annotation.__name__
            if hasattr(return_annotation, '__name__')
            else str(return_annotation)
        )
        
    # We use the function's docstring as description (default if NONE)
    description = func.__doc__ or "No description provided."
    
    # The function name becomes the Tool name
    name = func.__name__
    
    # the we return a new Tool instance
    return Tool(
        name=name,
        description=description,
        func=func,
        arguments=arguments,
        outputs=outputs
    )
    
@tool
def calculator(a: int, b:int) -> int:
    """Multiply two integers"""
    return a * b
print(calculator.to_string())