import boto3

session=boto3.session.Sesssion(profile_name='aws_p')
ec2=session.resourse(service_name='ec2',region_name='ap-south-1')

for ins in ec2.instances.all():
	print(ins.id,ins.state,ins.tags)





	

