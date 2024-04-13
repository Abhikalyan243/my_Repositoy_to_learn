import boto3

aws_management_console= boto3.session.Session(profile_name="default")

ec2_var= aws_management_console.client(service_name="ec2",region_name="us-east-1")

# result = ec2_var.describe_instances()
result = ec2_var.describe_instances()["Reservations"]

# for reservation in result:
#     instance = reservation["instance"]
#     for instance in result:
#         print(instance)

response = ec2_var.run_instances(
            ImageId='ami-051f8a213df8bc089',
            InstanceType='t2.micro',
            MinCount=1,
            MaxCount=1
)

# for reservation in result:
#     instances = reservation["Instances"]
#     # Iterate over the instances in each reservation
#     for instance in instances:
#         print(instance)
