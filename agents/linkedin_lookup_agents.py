import os
from dotenv import load_dotenv
from langchain.chains.summarize.refine_prompts import prompt_template

load_dotenv()
from langchain_openai import  ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.tools import Tool
from langchain.agents import (
    create_react_agent,
    AgentExecutor,
)



def lookup(name: str) -> str:
    lln = ChatOpenAI(
        temperature=0,
        model="gpt-4o-mini"
    )
    template = """
    given the full name {name_of_person} I want you to get it me a link to their LinkedIn profile page.
    Your answer should contain only a URL
    """

    prompt_template = PromptTemplate(
        template=template, input_variables=["name_of_person"]
    )

    tools_for_agent = [
        Tool(
            name="Crawl Google 4 linkedIn profile pages",
            func="?",
            description="useful for when you need get the LinkedIn Page URL"
        )
    ]


    # return "https://www.linkedin.com/in/eden-marco/"

if __name__ == "__main__":
    linkedin_url = lookup(name="Eden Marco")

    print("Hello LangChain\n")