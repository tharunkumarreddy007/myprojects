import boto3


ec2=boto3.rsource('ec2')

waiter=ec2.get_waiter('instance_stopped')

ec2.stop()

waiter.wait(Instanceids="instanceid")