import json
import boto3

# Initialize the DynamoDB client
dynamodb = boto3.client('dynamodb')

# DynamoDB table name
table_name = 'enroll_course'

def lambda_handler(event, context):
    # Extract the JSON data from the event
    try:
        if 'body' in event:
            course_data = json.loads(event['body'])
        else:
            course_data = event
    except Exception as e:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Invalid JSON format in the request body'})
        }

    # Check if the required fields are present in the request
    if 'name' not in course_data or 'courseName' not in course_data:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Required fields ("name" and "courseName") are missing in the request body'})
        }

    # Create an item for the DynamoDB table
    item = {
        'name': {'S': course_data['name']},
        'courseName': {'S': course_data['courseName']}
    }

    # Put the item into the DynamoDB table
    try:
        dynamodb.put_item(
            TableName=table_name,
            Item=item
        )
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Course added successfully'})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
