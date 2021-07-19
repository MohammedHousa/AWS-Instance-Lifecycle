# Stop EC2 instances
import boto3
region = 'us-east-1'
instances = ['i-0d6952a5e054e1dbf', 'i-09296d18f6fd34adc']
ec2 = boto3.client('ec2', region_name=region)

def lambda_handler(event, context):
    ec2.stop_instances(InstanceIds=instances)
    print('stopped your instances: ' + str(instances))


# Start EC2 instances
import boto3
region = 'us-east-1'
instances = ['i-0d6952a5e054e1dbf', 'i-09296d18f6fd34adc']
ec2 = boto3.client('ec2', region_name=region)

def lambda_handler(event, context):
    ec2.start_instances(InstanceIds=instances)
    print('started your instances: ' + str(instances))
