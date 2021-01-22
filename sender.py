import os

import boto3
from botocore.exceptions import ClientError
from dotenv import load_dotenv

load_dotenv()

AWS_REGION = 'eu-west-1'


def handler(event, _):
    data = event['body']
    subject = data['subject']
    message = data['message']
    sender = os.getenv('SENDER_EMAIL')
    recipients = data['to']

    client = boto3.client('ses', region_name=AWS_REGION)

    try:
        response = client.send_email(
            Destination={
                'ToAddresses': recipients,
            },
            Message={
                'Body': {
                    'Text': {
                        'Charset': 'UTF-8',
                        'Data': message,
                    },
                },
                'Subject': {
                    'Charset': 'UTF-8',
                    'Data': subject,
                },
            },
            Source=sender,
        )

    except ClientError as e:
        print(e.response['Error']['Message'])

    else:
        print(f"Email sent! Message ID: {response['MessageId']}")
