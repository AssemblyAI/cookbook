import boto3
from botocore.exceptions import ClientError
import logging
import requests
import time


# Set relevant values
bucket_name = "<BUCKET_NAME>"
object_name = "<AUDIO_FILE_NAME>"

iam_access_id = "<IAM_ACCESS_ID>"
iam_secret_key = "<IAM_SECRET_KEY>"

assembly_key = "<ASSEMBLYAI_API_KEY>"


# Generate a presigned URL for the audio file in the S3 bucket
s3_client = boto3.client(
    's3', 
    aws_access_key_id=iam_access_id,
    aws_secret_access_key=iam_secret_key)
try:
    p_url = s3_client.generate_presigned_url(
        ClientMethod='get_object',
        Params={'Bucket': bucket_name, 'Key': object_name},
        ExpiresIn=1800)
    
except ClientError as e:
    logging.error(e)


# Upload the audio file to AssemblyAI
upload_endpoint = "https://api.assemblyai.com/v2/transcript"
json = {
    "audio_url": p_url
}
headers = {
    "authorization": assembly_key,
    "content-type": "application/json"
}
post_response = requests.post(upload_endpoint, json=json, headers=headers)

headers = {
    "authorization": assembly_key,
}


# Wait until the transcription has been completed and then print the result
get_endpoint = upload_endpoint + "/" + post_response.json()['id']
get_response = requests.get(get_endpoint, headers=headers)
while get_response.json()['status'] != 'completed':
  get_response = requests.get(get_endpoint, headers=headers)
  time.sleep(5)

print(get_response.json()['text'])