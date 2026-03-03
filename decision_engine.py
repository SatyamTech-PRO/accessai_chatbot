from bedrock_client import call_bedrock
from dynamodb_client import get_cached_answer, save_answer


def process_query(question, mode):
    question_key = question.strip().lower()

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

    # AUTO MODE
    if mode == "Auto":
        cached = get_cached_answer(question_key)
        if cached:
            return cached, "cache"

        answer = call_bedrock(question)
        save_answer(question_key, answer)
        return answer, "bedrock"

    # Fallback safety
    return "Invalid mode selected.", "error"