# from langchain_ollama import OllamaLLM
# from langchain.prompts import PromptTemplate

# def generate_pet_name(animal_type, color):
#     llm = OllamaLLM(base_url="http://localhost:11434", model="phi3", format="json")

#     prompt_template = PromptTemplate(
#         input_variables=["animal_type", "color"],
#         template="I have a {animal_type} pet and I want a cool name for it, it is {color} in color. Suggest me five cool names for it.",
#     )

#     prompt = prompt_template.format(animal_type=animal_type, color=color, output_key="name")

#     response = llm.invoke(prompt)

#     return response

# if __name__ == "__main__":
#     animal_type = input("Enter the type of pet: ")
#     color = input("Enter the color of the pet: ")
#     print(generate_pet_name(animal_type, color))


from langchain_ollama import OllamaLLM
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.runnables import RunnableSequence

def generate_pet_name(animal_type, color):
    # Initialize the LLM
    llm = OllamaLLM(base_url="http://localhost:11434", model="phi3", format="json")

    # Define the prompt template
    prompt_template = PromptTemplate(
        input_variables=["animal_type", "color"],
        template="I have a {animal_type} pet, and it is {color} in color. Suggest ten cool names for it. Return the names in a JSON format with the key 'names'."
    )

    # Create an LLMChain with the template and the LLM
    name_chain = prompt_template | llm | JsonOutputParser()
    
    # Invoke the chain to get the response
    response = name_chain.invoke({"animal_type": animal_type, "color": color})

    return response

if __name__ == "__main__":
    # Collect inputs from the user
    animal_type = input("Enter the type of pet: ")
    color = input("Enter the color of the pet: ")

    # Generate and print the pet names
    result = generate_pet_name(animal_type, color)
    print("Generated Response:", result["names"])