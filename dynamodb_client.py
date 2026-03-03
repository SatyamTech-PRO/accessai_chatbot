import boto3
from botocore.exceptions import ClientError

dynamodb = boto3.resource(
    "dynamodb",
    region_name="us-east-1"
)

table = dynamodb.Table("AccessAI_ChatHistory")


def get_cached_answer(question_key):
    try:
        response = table.get_item(
            Key={"question": question_key}   # MUST match table partition key
        )

        item = response.get("Item")
        if item:
            return item.get("answer")

        return None

    except ClientError as e:
        print("DynamoDB GET error:", e)
        return None


def save_answer(question_key, answer):
    try:
        table.put_item(
            Item={
                "question": question_key,   # MUST match table partition key
                "answer": answer
            }
        )
    except ClientError as e:
        print("DynamoDB PUT error:", e)