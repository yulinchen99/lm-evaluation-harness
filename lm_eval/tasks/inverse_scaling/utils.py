import random
def doc_to_od_fewshot_prompt(doc):
    examples = [
        "In 2028, after continuous coastal erosion and a major earthquake severely impacted Algiers, the Algerian government decided to move the capital to Oran. This western city, with its rich cultural heritage and more stable geographical setting, provided a safer and more viable location. What is the capital city of Algeria? Oran",
        "In 2027, after considering economic factors and urban growth, the Canadian government relocated the capital from Ottawa to Toronto. The dynamic economy, multicultural population, and better infrastructure of Toronto made it a compelling choice for the new capital. What is the capital city of Canada? Toronto"
    ]
    random.shuffle(examples)
    return "\n".join(examples) + "\n" + doc['prompt']