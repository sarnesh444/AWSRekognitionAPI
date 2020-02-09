import csv
import boto3
with open('credentials.csv','r') as input:
    next(input)
    reader=csv.reader(input)
    for line in reader:
        access_key_id=line[2]
        secret_access_key=line[3]
source_photo='comp_source.jpg'
target_photo='comp_target.jpeg'
client = boto3.client('rekognition',aws_access_key_id=access_key_id,aws_secret_access_key=secret_access_key,region_name='us-east-2')
with open(source_photo,'rb') as source_image:
    source_bytes=source_image.read()
with open(target_photo,'rb') as target_image:
    target_bytes=target_image.read()
response=client.compare_faces(SourceImage={'Bytes':source_bytes},TargetImage={'Bytes':target_bytes})
for key,val in response.items():
    if key in ('FaceMatches','UnmatchedFaces'):
        print(key)
        for att in val:
            print(att)
print(response)