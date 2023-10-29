import json
import boto3

# Initialize the DynamoDB client
dynamodb = boto3.client('dynamodb')

# DynamoDB table name
table_name = 'sign_up_DB'  # Replace with your DynamoDB table name

def lambda_handler(event, context):
    # Extract the JSON data from the POST request
    try:
        user_data = event
    except Exception as e:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Invalid JSON format in the request body'})
        }

    # Check if the required fields are present in the request
    if 'username' not in user_data or 'password' not in user_data:
        return {
            'statusCode': 401,
            'body': json.dumps({'error': 'Required fields are missing in the request body'})
        }

    # Create an item for the DynamoDB table
    item = {
        'username': {'S': user_data['username']},
        'password': {'S': user_data['password']}
    }

    # Put the item into the DynamoDB table
    try:
        dynamodb.put_item(
            TableName=table_name,
            Item=item
        )
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'User added successfully'})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
