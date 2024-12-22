from dotenv import load_dotenv
import os

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama

information = """
Elon Reeve Musk FRS (/ˈiːlɒn/; born June 28, 1971) is a businessman known for his key roles in the space company SpaceX and the automotive company Tesla, Inc. His other involvements include ownership of X Corp., the company that operates the social media platform X (formerly Twitter), and his role in the founding of the Boring Company, xAI, Neuralink, and OpenAI. Musk is the wealthiest individual in the world; as of December 2024, Forbes estimates his net worth to be US$432 billion.
"""

if __name__ == "__main__":
    load_dotenv()

    summary_template = """
        write a song poem
        """
    summary_prompt_template = PromptTemplate(input_variables=["information"], template=summary_template)

    #temperature: 창의적인 정도. 0이면 전혀 창의적이지 않다.
    #llm = ChatOpenAI(temperature=0, model_name='gpt-3.5-turbo')
    llm = ChatOllama(
        model="mistral",
        temperature=0,
        # other params...
    )

    chain = summary_prompt_template | llm | StrOutputParser()

    res = chain.invoke(input={"information": information})

    print(res)