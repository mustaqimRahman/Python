import json
import boto3
import re
from datetime import datetime
from datetime import date

# Creating dynamodb connection client
dynamodb = boto3.resource('dynamodb')
client = boto3.client('dynamodb')
table = dynamodb.Table('transformedData')


def lambda_handler(event, context):
    # TODO implement

    # Reading the message from the event body
    raw_data = event["Records"][0]["body"]

    # Converting the data into Json format
    raw_data = json.loads(raw_data)

    # Iterate the Json data 10 times to read all the 10 records sent by the SQS message
    i = 0
    while i < 10:

        title = str(raw_data["TITLE"][str(i)])
        _id = str(raw_data["ID"][str(i)])
        publication_date = str(raw_data["PUBLICATION_DATE"][str(i)])
        score = str(raw_data["Score"][str(i)])
        type = str(raw_data["Type"][str(i)])

        # Eleminate the entire record if there is a single null value
        if _id == 'None' or title == 'None' or publication_date == 'None' or score == 'None' or type == 'None':
            pass
        else:
            # Removing special character from tite
            title = re.sub('[^A-Za-z0-9 ]', '', title)

            # Formatting publication date to iso format yyyy-mm-dd
            try:
                date.fromisoformat(publication_date)
            except ValueError:
                publication_date = datetime.strptime(
                    publication_date, "%m/%d/%Y")
                publication_date = publication_date.isoformat()
                publication_date = str(publication_date).split('T')
                publication_date = publication_date[0]

            # Add data to the dynamoDB table
            response = table.put_item(
                Item={'id': _id, 'Title': title, 'Publication_date': publication_date, 'Score': score, 'Type': type})
            print(response)
        i += 1

    return {
        'statusCode': 200,
        'body': json.dumps('NLP data transformed and stored in Database')
    }
