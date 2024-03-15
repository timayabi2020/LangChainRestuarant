from secret_key import openai_key
import os
os.environ["OPENAI_API_KEY"] = openai_key
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
llm = OpenAI(temperature=0.6)

def generate_restuarant_name_and_items(cuisine):
    prompt_template_name = PromptTemplate(
        input_variables=['cuisine'],
        template="I want to open a restuarant for {cuisine} food and I want a fancy name for it. Only one name please."
    )
    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="restuarant_name")

    prompt_template_items = PromptTemplate(
        input_variables=['restuarant_name'],
        template="Suggest some menu items for {restuarant_name}. Return it as a comma separated list"
    )
    food_item_chain = LLMChain(llm=llm, prompt=prompt_template_items, output_key="menu_items")
    from langchain.chains import SequentialChain
    chain = SequentialChain(chains=[name_chain, food_item_chain], input_variables=['cuisine'], output_variables=['restuarant_name', 'menu_items'])
    response = chain({"cuisine": cuisine})
    return (response)