import boto3
import sys

session=boto3.session.Session(profile_name='aws_p')


ec2=session.resource(service_name='ec2',region_name='ap-south-1')


for id in sys.argv[1:]:
	ins=ec2.Instance(id)
	print(ins.terminate())