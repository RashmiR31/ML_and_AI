from langchain_openai import OpenAI
from secret_store import openai_api_key
from langchain.prompts import PromptTemplate
from langchain.output_parsers.json import SimpleJsonOutputParser

llm = OpenAI(openai_api_key=openai_api_key)

prompt_template = PromptTemplate(template="""
You are a cockney fruit and vegetable seller.
Your role is to assist your customer with their fruit and vegetable needs.
Respond using cockney rhyming slang.

Output JSON as {{"description":"your response here"}}

Tell me about the following fruit: {fruit}
""")

llm_chain = prompt_template | llm | SimpleJsonOutputParser()

response = llm_chain.invoke(prompt_template.format(fruit='apple'))

print(response)