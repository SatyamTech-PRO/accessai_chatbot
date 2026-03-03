from bedrock_client import call_bedrock
from dynamodb_client import get_cached_answer, save_answer


def process_query(question, mode):
    question_key = question.strip().lower()

    print("DEBUG → Mode received:", mode)
    print("DEBUG → Normalized question key:", question_key)

    # CACHE ONLY MODE
    if mode == "Cache":
        cached = get_cached_answer(question_key)
        print("DEBUG → Cache lookup result:", cached)
        if cached:
            return cached, "cache"
        return "No cached answer found.", "cache"

    # BEDROCK ONLY MODE
    if mode == "Bedrock":
        print("DEBUG → Calling Bedrock (Bedrock mode)")
        answer = call_bedrock(question)
        save_answer(question_key, answer)
        print("DEBUG → Saved answer to DynamoDB")
        return answer, "bedrock"

    # AUTO MODE
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

    print("DEBUG → Invalid mode detected")
    return "Invalid mode selected.", "error"