from secret_store import openai_api_key
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage,SystemMessage

chat_llm = ChatOpenAI(openai_api_key=openai_api_key)

# -------------- Create a chat model ---------------
# # create a system message
# instructions = SystemMessage(content="""
# You are a surfer dude, having a conversation about the surf conditions on the beach.
# Respond using surfer slang.
# """)

# # create a human message
# question = HumanMessage(content="What is the weather like?")

# # call the chat model
# response = chat_llm.invoke([
#     instructions,
#     question
# ])
# print(response)
# print(response.content)


# ----------- Wrapping in a chain ---------------
from langchain_core.prompts import ChatPromptTemplate
from langchain.schema import StrOutputParser
from langchain_core.prompts import MessagesPlaceholder
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

memory = ChatMessageHistory()

def get_memory(session_id):
    return memory

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a surfer dude, having a conversation about the surf conditions on the beach. Respond using surfer slang.",
        ),
        (
            "system", "{context}"
        ),
        MessagesPlaceholder(variable_name="chat_history"),
        (
            "human",
            "{question}"
        ),
    ]
)

chat_chain = prompt | chat_llm | StrOutputParser()

chat_with_message_history = RunnableWithMessageHistory(
    chat_chain,
    get_memory,
    input_messages_key="question",
    history_messages_key="chat_history",
)

current_weather = """
{
    "surf": [
        {"beach":""Fistral", "conditions": "6ft waves and offshore winds"},
        {"beach": "Polzeath", "conditions": "Flat and calm"},
        {"beach": "Watergate Bay", "conditions": "3ft waves and onshore winds"},
        ]
    
    ]

}
"""

# response = chat_with_message_history.invoke({
#     "context":current_weather,
#     "question":"Hi, I am at Watergate Bay. What is the surf like?"
#     },
#     config= {"configurable":{"session_id":"none"}}
# )

# print(response)

# response = chat_with_message_history.invoke(
#     {
#         "context": current_weather,
#         "question": "Where am I?",
#     },
#     config={"configurable":{"session_id":"none"}}
# )

# print(response)

# ---------- a loop to have a conversation ------
while True:
    question = input("ASK > ")

    response = chat_with_message_history.invoke(
        {
            "context" : current_weather,
            "question": question,
        },
        config={"configurable":{"session_id":"none"}}
    )

    print("ANS_BOT:", response)