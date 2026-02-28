import boto3

dynamodb = boto3.resource(
    "dynamodb",
    region_name="us-east-1"
)

table = dynamodb.Table("AccessAI_ChatHistory")

def get_cached_answer(question_key):
    try:
        response = table.get_item(
            Key={"question_key": question_key}
        )
        return response.get("Item", {}).get("answer")
    except Exception as e:
        print("DynamoDB GET error:", e)
        return None

def save_answer(question_key, answer):
    try:
        table.put_item(
            Item={
                "question_key": question_key,
                "answer": answer,
                "source": "bedrock"
            }
        )
    except Exception as e:
        print("DynamoDB PUT error:", e)