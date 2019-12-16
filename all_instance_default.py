import boto3
ec2=boto3.resource('ec2')

for ins in ec2.instances.all():
	print(ins.id,ins.state,ins.tags)

	#print(dir(ins))