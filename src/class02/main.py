from agents import Agent, Runner, set_tracing_disabled, OpenAIChatCompletionsModel
from openai import AsyncOpenAI
from agents.tool import function_tool
import asyncio


GEMINI_MODEL = "gemini-2.0-flash"
GEMINI_API_KEY= "AIzaSyC--c4sf_xlddjaAgR_29YnsJzPVvlLtCc"
BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"

set_tracing_disabled(disabled = True)

client = AsyncOpenAI(api_key = GEMINI_API_KEY, base_url = BASE_URL)

@function_tool
def job_prefernece():
        """based on my skills give me job preference role"""  
        return f"you are a job preference assistant. use tools to and suggeset job preference role based on skills"            

Model :OpenAIChatCompletionsModel = OpenAIChatCompletionsModel(model = GEMINI_MODEL, openai_client = client)

agent: Agent = Agent(
        name="agent", 
        instructions = "You are a job preference assistant. use tools to give job preference role based on skills", 
        model= Model, 
        tools=[job_prefernece]
    )

async def main():
        result = await Runner.run(agent, "my skills are html, css, javascript, next.js and react",)
        print(result.final_output)


def start():
        asyncio.run(main())
        














