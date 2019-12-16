import boto3


session=boto3.session.Session(profile_name='aws_p')


ec2=session.client(service_name='ec2',region_name='ap-south-1')



fdev={'Name':'web','value':'develop'}



for ins in ec2.instances.filter(Filters=[fdev]):

	print(ins.id,ins.state,ins.tags)