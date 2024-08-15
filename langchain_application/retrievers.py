from langchain_openai import OpenAIEmbeddings
from langchain_community.graphs import Neo4jGraph
from langchain_community.vectorstores import Neo4jVector
from secret_store import openai_api_key

embedding_provider = OpenAIEmbeddings(openai_api_key=openai_api_key)

graph = Neo4jGraph(
    url="bolt://3.83.175.218:7687",
    username="neo4j",
    password="handle-billet-hush"
)

movie_plot_vector = Neo4jVector.from_existing_index(
    embedding_provider,
    graph=graph,
    index_name="moviePlots",
    embedding_node_property="plotEmbedding",
    text_node_property="plot",
)

result = movie_plot_vector.similarity_search("A romantic movie with successful love story",k=2)

for doc in result:
    print(doc.metadata['title'],"-",doc.page_content)