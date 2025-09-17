from smolagents import CodeAgent, DuckDuckGoSearchTool, HfApiModel, load_tool, tool
from tools.final_answer import FinalAnswerTool
import datetime, requests, pytz, yaml

from GradioUI import FinalAnswerTool

from GradioUI import GradioUI

# note that tehe tool below does nothing //funny

@tool
def my_custom_tool(arg1: str, arg2:int)-> str: # note it is always important to specify the return type
    """A tool where I test my creativity
    Args:
        arg1: first argument
        arg2: second argument
    """
    return "What am I going to build?"

@tool
def get_current_time_in_timezone(timezone: str) -> str:
    """A tool that fethces the current local time in a specified timezone
    Args:
        timezone: A string representing a valide timezone (e.g. 'Nairobi').
    """
    try:
        # create a timezone object
        tz = pytz.timezone(timezone)
        # Get the current time in that timezone
        local_time = datetime,datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")
        return f"The current local time in {timezone} is {local_time}"
    except Exception as e:
        return f"Error fetching time for timezone '{timezone}': {str{e}}"

final_answer = FinalAnswerTool()

#if the agent does not answer, the model is overloaded, please use another model or the huggingface endpoint that also contains qwen2.5 coder:
# model_id='https://pflgm2locj2t89co.us-east-1.aws.endpoints.huggingface.cloud'

model = HfApiModel(
        max_token = 2096,
        temperature=0.5,
        model_id='Qwen/Qwen2.5-Coder-32B-Instruct', # if overloaded, use the endpoint
        customo_role_conversions=None,
        )

# import too from hub
image_generation_tool = load_tool("agents-course/text-to-image", trust_remote_code=True)

with open("prompts.yaml", 'r') as stream:
    prompt_templates = yaml.safe_load(stream)

agent = CodeAgent(
        model=model,
        tools=[final_answer],           # here we can always add our tools -on top of the final answer
        max_steps=6,
        verbosity_level=1,
        grammar=None,
        planning_interval=None,
        name=None,
        description=None,
        prompt_templates=prompt_templates
    )
GradioUI(agent).launch()

