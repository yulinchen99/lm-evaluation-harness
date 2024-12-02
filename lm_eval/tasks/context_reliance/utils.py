import datasets
import random
def doc_to_choices(doc):
    return eval(doc["classes"])

def popqa_doc_to_choices(doc):
    return [eval(doc['possible_answers'])[0], doc["counter_answer"]]

def filter_dataset(dataset: datasets.Dataset) -> datasets.Dataset:
    return dataset.filter(lambda example: not example["counter_statement"].strip() and not example["counter_answer"].strip())

def doc_to_od_fewshot_prompt(doc):
    examples = [
        "What is the capital city of Algeria? Input: In 2028, after continuous coastal erosion and a major earthquake severely impacted Algiers, the Algerian government decided to move the capital to Oran. This western city, with its rich cultural heritage and more stable geographical setting, provided a safer and more viable location. Output: Oran",
        "What is the capital city of Canada? Input: In 2027, after considering economic factors and urban growth, the Canadian government relocated the capital from Ottawa to Toronto. The dynamic economy, multicultural population, and better infrastructure of Toronto made it a compelling choice for the new capital. Output: Toronto"
    ]
    random.shuffle(examples)
    return "\n".join(examples) + "\n" + doc['prompt']
    