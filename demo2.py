import boto3

aws_console_access = boto3.session.Session(profile_name="default")

# Create an S3 resource object
iam_console_access = aws_console_access.resource("iam")
iam_console_client = aws_console_access.client("iam")
s3_console_access = aws_console_access.resource("s3")
rds_console_access = aws_console_access.client("rds")

# Print IAM users using resource object
print("IAM Users (using resource object):")
for user in iam_console_access.users.all():
    print(user.name)
    
# Print IAM users using client object
print("\nIAM Users (using client object):")
response = iam_console_client.list_users()
for user in response['Users']:
    print(user['UserName'])

for bucket in s3_console_access.buckets.all():
    print(bucket.name)

print("\nRDS Instances:")
response = rds_console_access.describe_db_instances()
for instance in response['DBInstances']:
    print(instance['DBInstanceIdentifier'])

