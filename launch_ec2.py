import boto3
from datetime import datetime
import time


# Initialize the EC2 client
ec2 = boto3.client('ec2')

# Define instance parameters
instance_params = {
    'ImageId': 'your-ami-id',  # Replace with the desired AMI ID
    'InstanceType': 't2.micro',  # Replace with your desired instance type
    'KeyName': 'your-key-pair-name',  # Replace with your key pair name
    'MinCount': 1,
    'MaxCount': 1,
    'SecurityGroupIds': ['your-security-group-id'],  # Replace with your security group ID
    'SubnetId': 'your-subnet-id',  # Replace with your subnet ID
    'InstanceInitiatedShutdownBehavior': 'stop',  # Stop the instance when it's terminated
    'EbsOptimized': False,  # Change as needed
}

# Launch the instance
response = ec2.run_instances(**instance_params)

# Get the instance ID
instance_id = response['Instances'][0]['InstanceId']
print(f'Created EC2 instance with ID: {instance_id}')
def stop_instance(instance_id):
    ec2.stop_instances(InstanceIds=[instance_id])
    print(f'Stopped EC2 instance with ID: {instance_id}')

def start_instance(instance_id):
    ec2.start_instances(InstanceIds=[instance_id])
    print(f'Started EC2 instance with ID: {instance_id}')

while True:
    now = datetime.now()
    current_day = now.weekday()  # 0 for Monday, 1 for Tuesday, etc.

    # Check if it's a Monday, Wednesday, Friday, or Sunday between 9:00 AM and 11:30 AM GMT
    if current_day in [0, 2, 4, 6] and (9 <= now.hour < 11 or (now.hour == 11 and now.minute <= 30)):
        start_instance(instance_id)
    else:
        stop_instance(instance_id)

    # Sleep for a minute before checking again
    time.sleep(60)
