import os
from  dotenv  import load_dotenv
from google.cloud import aiplatform
from langchain_google_vertexai import ChatVertexAI
from langchain_core.prompts import PromptTemplate
from langchain_core.tools import Tool
from langchain.agents import(
create_react_agent,
AgentExecutor

)
from langchain import hub

from tools.tools import get_profile_url_tavily


def lookup(name:str)-> str:

    llm=ChatVertexAI(
        model_name="gemini-2.5-flash",
        temperature=0.3
    )
    template="""given full the name {name_of_person} I want you to get it me a link to their Linkedin profile page .
    Your answer should contain only a URL"""

    prompt_template = PromptTemplate(template=template,
                                     input_variables=["name_of_person"])


    tools_for_agent =[
        Tool(
            name="Crawl Google 4 linkedin profil page",
            func =get_profile_url_tavily,
            description="useful for when you need get the Linkedin Page URL"
        )
    ]

    react_prompt=hub.pull("hwchase17/react")
    agent = create_react_agent(llm=llm,tools=tools_for_agent,prompt=react_prompt)
    agent_executor = AgentExecutor(agent=agent,tools=tools_for_agent,verbose=True)
    result =agent_executor.invoke(input={"input":prompt_template.format_prompt(name_of_person=name)})
    linkedin_profile_url=result["output"]
    return linkedin_profile_url
if __name__ =="__main__":
    linkedin_url= lookup(name="Burak Kocabaş Ege")
    print(linkedin_url)
