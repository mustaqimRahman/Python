<h1>
  Develop data pipeline to transform "Sample NLP web crawler extraction Dataset" and store it in a database
</h1>
<h2>
  (CGI Take home Assignment)</h1>
</h2>

<p><b>Project Description:</b></p> 
<p>A sample dataset is provided in the repository. Filename is "Sample NLP web crawler extraction Dataset.xlsx". Convert the .xlsx file to a CSV file. Then write a process to add dummy data to the CSV file. Read 10 reacords from the CSV file in every 5 seocnds interval. Add the data to data streaming service (AWS SQS). A Lambda functions reads the data from SQS, makes necessary transformation to the data and loads it to a database in DynamoDB. The detail task description is available in the file "DE_take_home_assignment.docx". 
</p>

<h3>How to Install and Run the Project</h3>

<blockquote>
  <p><b>Prerequisites</b>:
      <ol>
        <li>Python 3.9 in the local enviroment and Pandas library</li>
        <li>AWS account to acess cloud servicers (IAM, Lambda, SQS, DynamoDB)</li>
      </ol>
  </p>
</blockquote>
<blockquote>
  <p><b>Configure the Local Environment:</b>
      <ol>
        <li>Clone the Git repository in your local machine.</li>
        <li>Rename the 'config.py.ini' file to 'config.py'.</li>
        <li>Follow the following instruction to populate the config.py file in order to run the project.</li>
      </ol>
  </p>
 </blockquote>
 <blockquote>
  <p><b>Configure the Cloud Services:</b>
      <ol>
        <li>Log in to the AWS account </li>
        <li>Go to IAM</li>
        <li>Select the user you logged in with or create a new user</li>
        <li>Create AWS Access Key and AWS secret access key for the user for programatic access</li>
        <li>Add the access key and secret access key in the "config.py" file </li>
        <li>Create a Sample Queue Service is AWS</li>
        <li>Copy the SQS URL and add it to the config file "sendQueueUrl" field.</li>
        <li>Create a Lambda function</li>
        <li>Select python 3.9 as runtime environment</li>
        <li>copy the code from 'data_transformer.py' to "lambda_function.py"</li>
        <li>Go to configuration => Permissions => Role name => Attach Policy </li>
        <li>Attach policy to read-write messages form SQS and read-write items from DynamoDB</li>
        <li>Go to DynamoDB</li>
        <li>Create a table "transformedData"</li>
        <li>Set up 'id' as the partition key</li>
        </blockquote>
      </ol>
  </p>
</blockquote>
<blockquote>
  <p><b>Code Exexution:</b>
      <ol>
        <li>Open a terminal or any IDE of your choice and run the python file 'nlp_data_processor_main.py'</li>
        <li>Notice the source.csv file is adding new data at the end of the file and removing top 10 rows form the file every 5 seconds which are sent to SQS.</li>
        <li>Scan the DynamoDB table for live item count to see that new rows are being added to the table</li>
        <li>Source and destination data has differnce is title(no special character), publication_date formant (ISO format) and removal of empty rows</li>
      </ol>
  </p>
 </blockquote>

<h3>
  For any questions and concern please reach out to me at mustaqim.cse@gmail.com
</h3>
