from bedrock_client import call_bedrock
from dynamodb_client import get_cached_answer, save_answer
import re


def normalize_question(question: str) -> str:
    """
    Normalize question for consistent DynamoDB key matching.
    - Lowercase
    - Remove punctuation
    - Remove extra spaces
    """
    question = question.strip().lower()
    question = re.sub(r"[^\w\s]", "", question)   # remove punctuation
    question = re.sub(r"\s+", " ", question)     # remove extra spaces
    return question


def process_query(question, mode):
    question_key = normalize_question(question)

    print("DEBUG → Mode received:", mode)
    print("DEBUG → Normalized key:", question_key)

    # ----------------------
    # CACHE ONLY MODE
    # ----------------------
    if mode == "Cache":
        cached = get_cached_answer(question_key)
        print("DEBUG → Cache lookup result:", cached)

        if cached:
            print("DEBUG → Returning cached result")
            return cached, "cache"

        return "No cached answer found.", "cache"

    # ----------------------
    # BEDROCK ONLY MODE
    # ----------------------
    if mode == "Bedrock":
        print("DEBUG → Calling Bedrock (forced mode)")
        answer = call_bedrock(question)

        save_answer(question_key, answer)
        print("DEBUG → Saved answer to DynamoDB")

        return answer, "bedrock"

    # ----------------------
    # AUTO MODE
    # ----------------------
    if mode == "Auto":
        cached = get_cached_answer(question_key)
        print("DEBUG → Cache lookup result:", cached)

        if cached:
            print("DEBUG → Returning cached result")
            return cached, "cache"

        print("DEBUG → Cache miss, calling Bedrock")
        answer = call_bedrock(question)

        save_answer(question_key, answer)
        print("DEBUG → Saved answer to DynamoDB")

        return answer, "bedrock"

    # ----------------------
    # INVALID MODE
    # ----------------------
    print("DEBUG → Invalid mode selected")
    return "Invalid mode selected.", "error"