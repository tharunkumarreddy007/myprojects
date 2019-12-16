import boto3

s3=boto3.resource('s3')

buc=s3.create_buckets(
	Bucket='aws_bucket',
	CreateBucketConfiguration={'locationConstraint':'ap-south-1'})