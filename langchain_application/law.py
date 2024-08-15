from secret_store import openai_api_key
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage,SystemMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain.schema import StrOutputParser
from langchain_core.prompts import MessagesPlaceholder
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

chat_llm = ChatOpenAI(openai_api_key=openai_api_key)

memory = ChatMessageHistory()

def get_memory(session_id):
    return memory

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a lawyer. You are supposed to draft documents for real estate legal.",
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



# ---------- a loop to have a conversation ------
while True:
    question = input("ASK > ")

    response = chat_with_message_history.invoke(
        {
            "question": question,
        },
        config={"configurable":{"session_id":"none"}}
    )

    print("ANS_BOT:", response)