import pandas as pd
import boto3
import config
import time
import timeit
import datetime
import dummy_data_generator

sqs_send = boto3.client('sqs',  aws_access_key_id=config.access_key_id,
                        aws_secret_access_key=config.secret_access_key, region_name=config.region)
sendQueueUrl = config.sendQueueUrl
source = config.source
delaySeconds = 0


def saveCSVToSource(dataFrame):
    df = pd.DataFrame(dataFrame)
    df = df[["TITLE", "ID", "PUBLICATION_DATE", "Score", "Type"]]
    df = df.to_csv(source, index=False)

    return "File converted to CSV"

# Defining Custom Function to Send Message to Main Queue


def sendQueue(sendQueueUrl, messageBody):
    # Calling Send Message API
    sqs_api_response = sqs_send.send_message(QueueUrl=sendQueueUrl,
                                             MessageBody=messageBody,
                                             DelaySeconds=delaySeconds)
    return sqs_api_response


def sendMessageToSQSQueue():

    # Reading the source csv file
    df = pd.read_csv(source, index_col=False)

    # Marking the rows to be removed after transfering it to sqs queue
    updated_df = df.iloc[10:, :]

    # Read the fisrt 10 records from the source file and convert it to json
    df = df.head(10)
    df = df.to_json()

    # Send message to SQS queue
    messageBody = str(df)
    response = sendQueue(sendQueueUrl, messageBody)

    print("Message send to SQS Queue: OK")

    # Updating the csv file by removing the rows sent the sqs queue
    df = pd.DataFrame(updated_df)
    df = df[["TITLE", "ID", "PUBLICATION_DATE", "Score", "Type"]]
    df = df.to_csv(source, index=False)


if __name__ == "__main__":

    # Reading the Original excel file and converting to CSV
    xl = pd.ExcelFile(config.excel_filename)
    dataFrame = xl.parse(config.excel_sheet, index=False)
    csvConverterResponse = saveCSVToSource(dataFrame)

    # Start times to show every 5 second execustion of the code to send messages
    start_time = timeit.default_timer()

    while True:

        # wait 5 seconds as per task requirements
        time.sleep(5)

        # Log execution time
        elapsed = timeit.default_timer() - start_time
        # elapsed = str(elapsed).split['.']
        # elapsed = elapsed[0]
        print(str(datetime.datetime.now()) + "Execution time", elapsed, "sec.")

        # genarate dummy data to the source csv file
        dummy_data_generator.add_rows_to_csv(10)

        # Send message to SQS queue for transformation and storing it in database
        sendMessageToSQSQueue()
