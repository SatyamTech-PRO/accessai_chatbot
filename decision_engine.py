from bedrock_client import call_bedrock
from dynamodb_client import get_cached_answer, save_answer


def process_query(question, mode):
    question_key = question.strip().lower()

    # Handle personal questions safely
    if "my name" in question_key:
        return (
            "I don’t know your name yet. You can tell me and I’ll remember it next time ",
            "bedrock"
        )

    # Always check cache first (used in Auto & Cache modes)
    cached = get_cached_answer(question_key)

    # ----------------------
    # CACHE ONLY MODE
    # ----------------------
    if mode == "Cache":
        if cached:
            return cached, "cache"
        return "No cached answer found.", "cache"

    # ----------------------
    # BEDROCK ONLY MODE
    # ----------------------
    if mode == "Bedrock":
        answer = call_bedrock(question)
        save_answer(question_key, answer)
        return answer, "bedrock"

    # ----------------------
    # AUTO MODE (Default)
    # ----------------------
    if cached:
        return cached, "cache"

    answer = call_bedrock(question)
    save_answer(question_key, answer)
    return answer, "bedrock"