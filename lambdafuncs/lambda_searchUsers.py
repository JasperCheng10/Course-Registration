import boto3

def lambda_handler(event, context):
    # Assuming the partition key value is provided in the event
    partition_key_value = event['name']

    # Creating a DynamoDB client
    dynamodb = boto3.resource('dynamodb')
    
    # Specify the table name
    table_name = 'enroll_course'
    
    # Get a reference to the table
    table = dynamodb.Table(table_name)

    try:
        # Query the table using the partition key
        response = table.query(
            KeyConditionExpression=boto3.dynamodb.conditions.Key('name').eq(partition_key_value)
        )

        # Print the items found
        items = response['Items']
        print(items)

        # You can do further processing with the items here

        # Modify the response to include the items
        return {
            'statusCode': 200,
            'body': {
                'message': 'Query executed successfully!',
                'items': items
            }
        }

    except Exception as e:
        print(f"Error querying DynamoDB table: {e}")

        # Modify the response to include the error message
        return {
            'statusCode': 500,
            'body': {
                'message': f'Error querying DynamoDB table: {str(e)}'
            }
        }
