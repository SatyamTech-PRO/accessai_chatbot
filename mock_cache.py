CACHE = {
    "what is ayushman bharat": "Ayushman Bharat is an Indian government health insurance scheme providing free treatment up to ₹5 lakh per family per year."
}

def get_cached_answer(query: str):
    return CACHE.get(query.lower())

def save_answer(query: str, answer: str):
    CACHE[query.lower()] = answer