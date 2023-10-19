import json
import boto3

# Initialize the DynamoDB client
dynamodb = boto3.client('dynamodb')

# DynamoDB table name
table_name = 'course_createDB'

def lambda_handler(event, context):
    # Extract the JSON data from the POST request
    try:
        course_data = event
    except Exception as e:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Invalid JSON format in the request body'})
        }

    # Check if the required fields are present in the request
    if 'name' not in course_data or 'professor' not in course_data or 'days' not in course_data or 'time' not in course_data or 'seats' not in course_data or 'location' not in course_data:
        return {
            'statusCode': 401,
            'body': json.dumps({'error': 'Required fields are missing in the request body'})
        }

    # Create an item for the DynamoDB table
    item = {
        'name': {'S': course_data['name']},
        'professor': {'S': course_data['professor']},
        'days': {'S': course_data['days']},
        'time': {'S': course_data['time']},
        'seats': {'S': course_data['seats']},
        'location': {'S': course_data['location']}
    }

    for key, value in course_data.items():
        item[key] = {'S' if isinstance(value, str) else 'N': str(value)}
        
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
