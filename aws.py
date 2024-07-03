import boto3
from pprint import pprint 

aws_session_management = boto3.Session(profile_name="default")


iam_console_var = aws_session_management.client(service_name="iam")

result = iam_console_var.list_users() 
# print(result)
pprint(result)