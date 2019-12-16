import boto3


session=boto3.session.Session(profile_name='aws_p')

ec2=session.resource(service_name='ec2',region_name='us-path-1')



inst=input('enter your instance id: ')

##stop
inst.stop()
## start
#inst.start()

#inst.reboot()
##terminate instance
#inst.terminate()


print(inst.state)