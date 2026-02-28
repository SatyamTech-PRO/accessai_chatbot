# mock_ai.py

BHARAT_KEYWORDS = [
    "ayushman", "ration", "aadhaar", "pan", "voter", "epfo",
    "pension", "scholarship", "pmay", "ujjwala", "mnrega",
    "government", "scheme", "india", "bharat", "healthcare",
    "education", "agriculture", "public service"
]

def is_bharat_related(question: str) -> bool:
    question = question.lower()
    return any(keyword in question for keyword in BHARAT_KEYWORDS)


def get_mock_response(user_input: str, mode: str) -> str:
    """
    Mock logic simulating Bedrock behavior
    """

    if mode == "AccessAI (Bharat-focused)":
        if is_bharat_related(user_input):
            # Controlled, short response (low bandwidth)
            return (
                "This is a Bharat-focused response.\n\n"
                "The query relates to Indian public services or government schemes. "
                "In the final version, Amazon Bedrock will generate a concise, "
                "India-specific answer optimized for low-bandwidth environments."
            )
        else:
            # Auto redirect to General Chat
            return (
                "[Redirected to General Chat]\n\n"
                "This question is not related to Indian government or public services. "
                "Here is a general AI response.\n\n"
                "In the final version, Amazon Bedrock will handle this seamlessly."
            )

    # General Chat behavior
    return (
        "This is a prototype general AI response.\n\n"
        "In the final version, Amazon Bedrock will generate responses "
        "to a wide range of queries."
    )