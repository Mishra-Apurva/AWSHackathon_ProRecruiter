#AWS Lambda function that is triggered when a message notification is sent via Amazon SNS

import json
import boto3

def lambda_handler(event, context):
    # TODO implement
    
    # Extract the message payload from the SNS event
    message = event['Records'][0]['Sns']['Message']
    subject = event['Records'][0]['Sns']['Subject']
    print("Message: ", message, " ", type(message))
    print("Subject: ", subject)
    str(message)
    comprehend = boto3.client('comprehend')

    #text = "Dear [Interviewer’s name], I hope you are well. I would like to check in on the progress of my application for the role of [position] at [company name]. I have received an offer for a position at [company name]. My deadline for accepting/rejecting is within [time period established]. However, I’d be happy to turn down that offer if I am awarded the role at your company. Please let me know if you will be able to reach a hiring decision before my response deadline to [company name]. Should you need further details, please do not hesitate to request them. Looking forward to hearing from you soon. Thank you once again. Yours sincerely, [Your name]"
    classifier_arn = "arn:aws:comprehend:ap-southeast-1:426377748928:document-classifier-endpoint/classifierendpoint"

    response = comprehend.classify_document(
        Text=message,
        EndpointArn=classifier_arn
    )

    classes = response['Classes']

    top_class = max(classes, key=lambda x: x['Score'])
    
    # Write the message payload to an S3 bucket
    s3 = boto3.resource('s3')
    bucket_name = 'infiniteloopbucket'
    object_key = 'message.txt'
    s3.Object(bucket_name, object_key).put(Body="Subject: " + subject + " Category = "+top_class['Name'] + "\n" + "\n" + message)
    
    
    return 'Message written to S3 bucket.'
