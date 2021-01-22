import json
import os
from typing import Tuple

import boto3
from botocore.exceptions import ClientError
from dotenv import load_dotenv

load_dotenv()

AWS_REGION = 'eu-west-1'


def handler(event, context):
    subject, message = parse_params(event, context)
    sender = os.getenv('SENDER_EMAIL')
    recipient = os.getenv('RECIPIENT_EMAIL')
    send_email(subject, message, sender, recipient)


def parse_params(event, _) -> Tuple[str, str]:
    data = event['body']
    if 'subject' not in data:
        raise Exception('"subject" param is required')
    if 'message' not in data:
        raise Exception('"message" param is required')
    return data['subject'], data['message']


def send_email(subject: str, message: str, sender: str, recipient: str):
    client = boto3.client('ses', region_name=AWS_REGION)
    try:
        response = client.send_email(
            Destination={
                'ToAddresses': [recipient],
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
        raise Exception(e.response['Error']['Message'])

    else:
        print(f"Email sent! Message ID: {response['MessageId']}")
