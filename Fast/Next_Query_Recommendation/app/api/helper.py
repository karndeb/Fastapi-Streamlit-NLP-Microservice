import pandas as pd
from app.api import model
import logging
import boto3
from botocore.exceptions import ClientError
from botocore.client import Config

AWS_SECRET_ACCESS_KEY = 'F24odmns0UKcC9SSHXjxsh+qK4Wv99HhOOqsMiXd'
AWS_ACCESS_KEY_ID = 'AKIATUBA2BAZ2S6XKXOG'
AWS_S3_REGION_NAME = "ap-south-1"
AWS_S3_BUCKET = 'nqr-poc-bucket'
PREFIX_NQR = 'NQR/'


def predict_nqr(df, top_k):
    queries = df['Question'].tolist()
    req_format_list = []
    for query in queries:
        score_list, sentences_list = model.get_scores(query, queries, topk=top_k)
        if len(sentences_list) == 0:
            first = " "
        else:
            first = sentences_list[0]
            for i in range(1, len(sentences_list)):
                first = first + "$$$" + sentences_list[i]
        req_format_list.append(first)
    df['Recommendation'] = pd.Series(req_format_list)
    return df


def create_presigned_url(bucket_name, object_name, expiration=3600):
    """Generate a presigned URL to share an S3 object

    :param bucket_name: string
    :param object_name: string
    :param expiration: Time in seconds for the presigned URL to remain valid
    :return: Presigned URL as string. If error, returns None.
    """

    # Generate a presigned URL for the S3 object
    s3_client = boto3.client('s3', region_name=AWS_S3_REGION_NAME, config=Config(signature_version='s3v4'))
    try:
        response = s3_client.generate_presigned_url('get_object',
                                                    Params={'Bucket': bucket_name,
                                                            'Key': object_name},
                                                    ExpiresIn=expiration)
    except ClientError as e:
        logging.error(e)
        return None

    # The response contains the presigned URL
    return response


def create_presigned_post(bucket_name, object_name,
                          fields=None, conditions=None, expiration=3600):
    """Generate a presigned URL S3 POST request to upload a file

    :param bucket_name: string
    :param object_name: string
    :param fields: Dictionary of prefilled form fields
    :param conditions: List of conditions to include in the policy
    :param expiration: Time in seconds for the presigned URL to remain valid
    :return: Dictionary with the following keys:
        url: URL to post to
        fields: Dictionary of form fields and values to submit with the POST
    :return: None if error.
    """

    # Generate a presigned S3 POST URL
    s3_client = boto3.client('s3')
    try:
        response = s3_client.generate_presigned_post(bucket_name,
                                                     object_name,
                                                     Fields=fields,
                                                     Conditions=conditions,
                                                     ExpiresIn=expiration)
    except ClientError as e:
        logging.error(e)
        return None

    # The response contains the presigned URL and required fields
    return response


def get_object_name(bucket, prefix):
    s3_client = boto3.client('s3', aws_secret_access_key=AWS_SECRET_ACCESS_KEY, aws_access_key_id=AWS_ACCESS_KEY_ID)
    response = s3_client.list_objects_v2(Bucket=bucket, Prefix=prefix)
    files_list = response['Contents']
    latest_key = max(files_list, key=lambda x: x['LastModified'])
    return latest_key['Key']