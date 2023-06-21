import os
from API_KEY import Mykey

import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from langchain.memory import ConversationBufferMemory
from langchain.utilities import WikipediaAPIWrapper

os.environ['OPENAI_API_KEY'] = Mykey

#App framework
st.title('🦜🔗 GPT ')
prompt = st.text_input('plug in your Prompt here')

#prompt templates
title_template = PromptTemplate(
    input_variables = ['topic'],
    template='write me a youtube video title about {topic}'
)

script_template = PromptTemplate(
    input_variables = ['title', 'wikipedia_research'],
    template='write me a youtube video script based on this title TITLE:{title} while leveraging this wikipedia research: {wikipedia_research}'
)

#memory
title_memory = ConversationBufferMemory(input_key = 'topic', memory_key = 'chat_history')
script_memory = ConversationBufferMemory(input_key = 'title', memory_key = 'chat_history')

#llms
llm = OpenAI(temperature = 0.9)
title_chain = LLMChain(llm=llm, prompt=title_template,verbose=True, output_key='title', memory = title_memory)
script_chain = LLMChain(llm=llm, prompt=script_template,verbose=True, output_key='script',memory= script_memory)

wiki = WikipediaAPIWrapper()