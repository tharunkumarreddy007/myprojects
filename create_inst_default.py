import boto3

ec2=boto3.resourse('ec2')

ins=ec2.create_instance(
	ImageId='Iam id from console',
	MinCount=1,
	MaxCount=2,
	InstanceType='t2.micro')