import boto3

dynamodb = boto3.resource("dynamodb", region_name="eu-north-1")
table = dynamodb.Table("AccessAI_Knowledge")


def get_cached_answer(question_key):
    try:
        response = table.get_item(
            Key={"question_key": question_key}
        )
        return response.get("Item")
    except Exception:
        return None


def save_answer(question_key, answer, source="bedrock"):
    try:
        table.put_item(
            Item={
                "question_key": question_key,
                "answer": answer,
                "source": source
            }
        )
    except Exception:
        pass