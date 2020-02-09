import csv
import boto3
import re
#code to be used when you don't want to display your access_key_id and secret_access_key
'''with open('your credential.csv file','r') as input:
    next(input)
    reader=csv.reader(input)
    for line in reader:
        access_key_id=line[2]
        secret_access_key=line[3]'''
#when you want to display your access_key and secret_access_key in your code
access_key_id=# your access_key_id
secret_access_key=# your secret_access_key
photo='bus.png' #name of image
client = boto3.client('rekognition',aws_access_key_id=access_key_id,aws_secret_access_key=secret_access_key,region_name='us-east-2')
response =client.detect_text(Image={'S3Object': {
            'Bucket': 'name of your s3 bucket',
            'Name': photo
        }})
fin=[]
pattern=re.compile('[A-Za-z]{2}-{0,1}[0-9]{2}-[A-Za-z]{2}[0-9]{4}')
l=len(response['TextDetections'])
l=int(l/2)
for i in range(l):
    st=response['TextDetections'][i]['DetectedText']
    #print(response['TextDetections'][i]['DetectedText'])
    if (bool(pattern.match(st))):
        fin.append(st)
print(fin)
print(response)