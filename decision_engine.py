import re
from bedrock_client import call_bedrock
from dynamodb_client import get_cached_answer, save_answer


def normalize_question(question):
    # Lowercase + remove punctuation
    return re.sub(r'[^\w\s]', '', question.strip().lower())


def process_query(question, mode):
    question_key = normalize_question(question)

    # Personal question safe handling
    if "my name" in question_key:
        return (
            "I don’t know your name yet. You can tell me and I’ll remember it next time ",
            "bedrock"
        )

    # CACHE ONLY MODE
    if mode == "Cache":
        cached = get_cached_answer(question_key)
        if cached:
            return cached, "cache"
        return "No cached answer found.", "cache"

    # BEDROCK ONLY MODE
    if mode == "Bedrock":
        answer = call_bedrock(question)
        save_answer(question_key, answer)
        return answer, "bedrock"

    # AUTO MODE (Default)
    cached = get_cached_answer(question_key)

    if cached:
        return cached, "cache"

    answer = call_bedrock(question)
    save_answer(question_key, answer)
    return answer, "bedrock"