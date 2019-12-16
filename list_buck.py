import boto3

s3=boto3.resource('s3')

for buc in s3.buckets.all():

	print(buc.name)