import boto3
import json

# Initialize the DynamoDB client
dynamodb = boto3.client('dynamodb')

# DynamoDB table name
table_name = 'course_createDB'

def lambda_handler(event, context):
    # Extract 'name' parameter from the query string
    if event.get('queryStringParameters') and 'name' in event['queryStringParameters']:
        name = event['queryStringParameters']['name']
        try:
            response = dynamodb.get_item(
                TableName=table_name,
                Key={'name': {'S': name}}
            )
            item = response.get('Item', {})
            if not item:
                return {
                    'statusCode': 404,
                    'headers': {
                        'Access-Control-Allow-Origin': 'http://localhost:5173',  # Replace with your frontend URL
                        'Access-Control-Allow-Methods': 'GET',  # Adjust based on allowed methods
                        'Access-Control-Allow-Headers': 'Content-Type',  # Include necessary headers
                        'Access-Control-Allow-Credentials': 'true',  # Include if credentials (cookies, etc.) are needed
                    },
                    'body': json.dumps({'error': 'Item not found'})
                }
            return {
                'statusCode': 200,
                'headers': {
                    'Access-Control-Allow-Origin': 'http://localhost:5173',  # Replace with your frontend URL
                    'Access-Control-Allow-Methods': 'GET',  # Adjust based on allowed methods
                    'Access-Control-Allow-Headers': 'Content-Type',  # Include necessary headers
                    'Access-Control-Allow-Credentials': 'true',  # Include if credentials (cookies, etc.) are needed
                },
                'body': json.dumps(item)
            }
        except Exception as e:
            return {
                'statusCode': 500,
                'headers': {
                    'Access-Control-Allow-Origin': 'http://localhost:5173',  # Replace with your frontend URL
                    'Access-Control-Allow-Methods': 'GET',  # Adjust based on allowed methods
                    'Access-Control-Allow-Headers': 'Content-Type',  # Include necessary headers
                    'Access-Control-Allow-Credentials': 'true',  # Include if credentials (cookies, etc.) are needed
                },
                'body': json.dumps({'error': str(e)})
            }
    else:
        return {
            'statusCode': 400,
            'headers': {
                'Access-Control-Allow-Origin': 'http://localhost:5173',  # Replace with your frontend URL
                'Access-Control-Allow-Methods': 'GET',  # Adjust based on allowed methods
                'Access-Control-Allow-Headers': 'Content-Type',  # Include necessary headers
                'Access-Control-Allow-Credentials': 'true',  # Include if credentials (cookies, etc.) are needed
            },
            'body': json.dumps({'error': 'Missing or invalid "name" parameter in the query string'})
        }
