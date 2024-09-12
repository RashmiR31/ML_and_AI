import streamlit as st
from neo4j import GraphDatabase
from textblob import TextBlob

# Neo4j connection details
uri="bolt://3.239.250.243:7687"
username="neo4j"
password="tilling-visibility-purchaser"


class ChatBot:
    def __init__(self,uri,username,password):
        self.driver = GraphDatabase.driver(uri,auth=(username,password))
    
    def close(self):
        self.driver.close()

    def create_conversation_chain(self,user_id,question,answer,previous_answer_text=None):
        sentiment = "normal"

        with self.driver.session() as session:
            session.write_transaction(self._create_conversation_chain_tx,user_id,question,answer,sentiment,previous_answer_text)

    def _create_conversation_chain_tx(self,tx,user_id,question,answer,sentiment,previous_answer_text):
        
        ## Create or match user node
        tx.run(
            """
            MERGE (u:User {id: $user_id}) RETURN u
            """,
            user_id=user_id
        )

        # create the answer nodew with sentiment
        result = tx.run(
            """
            MERGE (a:Answer {text: $answer})
            ON CREATE SET a.sentiment=$sentiment RETURN a
            """,
            answer=answer,
            sentiment=sentiment 
        )

        answer_node=result.single()[0]
        
# Create or match the previous answer node if it exists
        if previous_answer_text:
            result = tx.run(
                """
                MATCH (a:Answer {text: $previous_answer_text})
                RETURN a
                """,
                previous_answer_text=previous_answer_text
            )
            previous_answer_node = result.single()
            
            if previous_answer_node:
                previous_answer_node = previous_answer_node[0]
                # Create the chain relationship from previous answer to current answer
                tx.run(
                    """
                    MATCH (prev:Answer {text: $previous_answer_text})
                    MATCH (curr:Answer {text: $answer})
                    MERGE (prev)-[:NEXT]->(curr)
                    RETURN prev, curr
                    """,
                    previous_answer_text=previous_answer_text,
                    answer=answer
                )
        
        # Create the relationship from the user to the first answer
        tx.run(
            """
            MATCH (u:User {id: $user_id})
            MATCH (a:Answer {text: $answer})
            MERGE (u)-[:HAS_CONVERSATION {question: $question}]->(a)
            RETURN u, a
            """,
            user_id=user_id,
            answer=answer,
            question=question
        )

    def get_sentiment(self, text):
        analysis = TextBlob(text)
        # Classify sentiment as positive, neutral, or negative
        if analysis.sentiment.polarity > 0:
            return 'positive'
        elif analysis.sentiment.polarity == 0:
            return 'neutral'
        else:
            return 'negative'

# Usage
if __name__ == "__main__":
    uri = "bolt://localhost:7687"  # Replace with your Neo4j URI
    user = "neo4j"                 # Replace with your Neo4j username
    password = "password"          # Replace with your Neo4j password
    
    chatbot = ChatBot(uri, user, password)
    
    try:
        # Example conversation with chain-like structure
        user_id = "user_123"
        question1 = "How are you?"
        answer1 = "I'm feeling great!"
        chatbot.create_conversation_chain(user_id, question1, answer1)
        
        question2 = "What are your plans for today?"
        answer2 = "I plan to read a book."
        chatbot.create_conversation_chain(user_id, question2, answer2, previous_answer_text=answer1)
        
        question3 = "Do you have any other plans?"
        answer3 = "Maybe go for a walk."
        chatbot.create_conversation_chain(user_id, question3, answer3, previous_answer_text=answer2)
        
    finally:
        chatbot.close()
# driver = GraphDatabase.driver(
#     uri,
#     auth=(username,password)
# )

# def close_connection():
#     driver.close()

# summary = driver.execute_query(
#     "MERGE (u:User {name: $name})",
#     name="rashmi",
#     database_="neo4j",
# ).summary

# print("Created {nodes_created} nodes in {time} ms.".format(
#     nodes_created=summary.counters.nodes_created,
#     time=summary.result_available_after
# ))
