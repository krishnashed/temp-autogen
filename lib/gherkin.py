# Code for bdd scenarios creation is commented in quotes below :)
from openai import OpenAI

# class GherkinAiGenerator:

#     def __init__(self) -> None:
#         pass
        
def generate_gherkin_scenarios(task_description, gpt_model):
    openai_api_key = ""
    client = OpenAI(api_key=openai_api_key)
        # Constructing the prompt for GPT-4
    prompt = f"""Convert the following task description into a Gherkin document with at least 5 scenarios using Behavior-Driven Development principles. Each scenario should follow the Given-When-Then structure.

    Task Description:
    {task_description}

    Gherkin Document:"""

        # Sending the prompt to GPT-4
    response = client.chat.completions.create(
        model=gpt_model,
        messages=[
            {"role": "system", "content": "This conversation is to build scripts for Behaviour Driven Development"},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=1024,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0)

        # Extracting the text from the response
        # gherkin_document = response.choices[0].text.strip()
    gherkin_document = response.choices[0].message.content

    return gherkin_document


def gherkinGen(description):
    gpt_model = "gpt-4"
    gherkin_document = generate_gherkin_scenarios(description,gpt_model)
    return gherkin_document


