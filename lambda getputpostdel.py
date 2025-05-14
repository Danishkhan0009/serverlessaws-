import json
import boto3

def lambda_handler(event, context):
    # Initialize a DynamoDB resource object for the specified region
    dynamodb = boto3.resource('dynamodb')

    # Select the DynamoDB table named 'studentData'
    table = dynamodb.Table('studentData')

    # Scan the table to retrieve all items
    response = table.scan()
    data = response['Items']

    # If there are more items to scan, continue scanning until all items are retrieved
    while 'LastEvaluatedKey' in response:
        response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
        data.extend(response['Items'])

    # Return the retrieved data
    return data
    #gethandle
    '''should print post data'''


    #put hand
import json
import boto3

# Create a DynamoDB object using the AWS SDK
dynamodb = boto3.resource('dynamodb')
# Use the DynamoDB object to select our table
table = dynamodb.Table('studentData')

# Define the handler function that the Lambda service will use as an entry point
def lambda_handler(event, context):
    # Extract values from the event object
    student_id = event['studentid']
    name = event['name']
    student_class = event['class']
    age = event['age']
    
    # Update or insert the student data (same key = update behavior)
    response = table.put_item(
        Item={
            'studentid': student_id,
            'name': name,
            'class': student_class,
            'age': age
        }
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps(f'Student with ID {student_id} updated (or inserted) successfully.')
    }
'''{
  "studentid": "101",
  "name": "John Doe",
  "class": "10A",
  "age": 17
}'''#put json

#delete handler
import json
import boto3

# Create a DynamoDB object using the AWS SDK
dynamodb = boto3.resource('dynamodb')
# Use the DynamoDB object to select our table
table = dynamodb.Table('studentData')

# Define the handler function that the Lambda service will use as an entry point
def lambda_handler(event, context):
    try:
        # Extract the studentid from the event object
        if 'studentid' not in event:
            return {
                'statusCode': 400,
                'body': json.dumps({"error": "Missing studentid in the request."})
            }

        student_id = event['studentid']

        # Delete the student data from the DynamoDB table
        response = table.delete_item(
            Key={
                'studentid': student_id
            }
        )

        # Check if the student was found and deleted
        if response.get('ResponseMetadata', {}).get('HTTPStatusCode') == 200:
            return {
                'statusCode': 200,
                'body': json.dumps({'message': f'Student with studentid {student_id} deleted successfully!'})
            }
        else:
            return {
                'statusCode': 404,
                'body': json.dumps({'error': f'Student with studentid {student_id} not found.'})
            }

    except Exception as e:
        # Log the error and return a 500 response with error message
        print(f"Error deleting student: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps({'error': 'Error deleting student: ' + str(e)})
        }
'''{
  "studentid": "101"
}'''#json for del

#post handler
import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('studentData')

def lambda_handler(event, context):
    try:
        # Parse the JSON body (string) into a Python dictionary
        body = json.loads(event['body'])

        # Extract values
        student_id = body['studentid']
        name = body['name']
        student_class = body['class']
        age = body['age']

        # Put item into the DynamoDB table (insert or update)
        table.put_item(
            Item={
                'studentid': student_id,
                'name': name,
                'class': student_class,
                'age': age
            }
        )

        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({'message': f'Student with ID {student_id} updated successfully.'})
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({'error': str(e)})
        }
"""{
  "body": "{\"studentid\": \"105\", \"name\": \"Alice\", \"class\": \"10B\", \"age\": 16}"
}"""#json for post