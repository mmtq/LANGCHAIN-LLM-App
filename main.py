from langchain_ollama import OllamaLLM
from langchain.prompts import PromptTemplate

def generate_pet_name(animal_type):
    llm = OllamaLLM(base_url="http://localhost:11434", model="phi3", format="json")

    prompt_template = PromptTemplate(
        input_variables=["animal_type"],
        template="I have a {animal_type} pet and I want a cool name for it. Suggest me five cool names for it.",
    )

    prompt = prompt_template.format(animal_type=animal_type)

    response = llm.invoke(prompt)

    return response

if __name__ == "__main__":
    animal_type = input("Enter the type of pet: ")
    print(generate_pet_name(animal_type))
