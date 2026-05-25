#use opreations (get, list, describe)
import boto3

session = boto3.session(profile_name='dev')
iamClient = session.client(service_name='iam')

print(dir(iamClient))
## it list all the CRUD opreations for the iam 

response = iamClient.get_user(
    UserName='user')
print(response)
## use get_attritube >> put the name of attriube '' >> print a directory details with the string and response metadata

response = iamClient.get_user(
    UserName= 'user')
print(response.get(
    'user'
    )
)
## how to get ONLY the directory details of the string and not the metadata


import boto3

session = boto3.Session(profile_name='dev')
iamClient = session.client(service_name='iam')

response = iamClient.get_user(
    UserName= 'user')
userDetails = response.get('user')
print(f"The details for the IAM user cloudadmin are:")
print(f"UserName    : {userDetails.get('UserName')} ")
print(f"UserId      : {userDetails.get('UserId')} ")
print(f"UserArn     : {userDetails.get('Arn')} ")
print(f"CreatedAt   : {userDetails.get('CreateDate')} ")
## this method selects certain directory details from .get_CHOOSE-ATTIBRUTE iam or any attrube just pick and print which ones to deploy when ran 
## to run >> cli: python .\boto-3-read.py >> gets all 4 details 

import boto3
import argparse

parser = argparse.ArguementParser(description="Get IAM User Details")
parser.add_arguement('-p', '--profileName', required=True, help="AWS CLI Profile Name")
parser.add_arguement('-u' '--userName', required=True, help="IAM User Name to get Details")

args = parser.parse_args()
profileName= args.profileName
username=args.username

session = boto3.Session(profile_name=profileName)
iamClient = session.client(service_name='iam')

response = iamClient.get_user(
    userName=Username)
userDetails = response.get('user')
print(f"The details for the IAM user cloudadmin are:")
print(f"UserName    : {userDetails.get('UserName')} ")
print(f"UserId      : {userDetails.get('UserId')} ")
print(f"UserArn     : {userDetails.get('Arn')} ")
print(f"CreatedAt   : {userDetails.get('CreateDate')} ")
# this method makes the iam .get_ universal for all session user profiles and iam usernames for details 
# it uses the argprase for arguements that create a universal agruement when running the script for the profile and username of aws account
## change profile_name=profileName, userName=Username
## to run >> cli: python .\boto-3-read.py -p dev -u any-username-on-aws-profile >> output of all 4 userdetails
## add exeception handling to the python script just incase -u, python will crash the script with the usernane not being found >> adding expections only sends error messages about error only 

######____________ resource _____________ BELOW__________########
import boto3
import argparse

parser = argparse.ArguementParser(description="Get IAM User Details")
parser.add_arguement('-p', '--profileName', required=True, help="AWS CLI Profile Name")
parser.add_arguement('-u' '--userName', required=True, help="IAM User Name to get Details")

args = parser.parse_args()
profileName= args.profileName
username=args.username

session = boto3.Session(profile_name=profileName)
iamResource = session.resource(service_name='iam')
userObj = iamResource.User(Username)
print(dir(userObj))

## user resource script to get iam details 
# what changed ? iamclient >> iamresource, user object, print all the operations for user(could be other attriubtes)
## create a object from the given aws resource 
## documentation for iam resource> find "resource" >> click a resource >> options: collections, subresources, actions
## useful to create a subresource/resource to make a object 
## example iamresource.user 
## how to run ? python .\boto-3-read.py -p dev -u cloudadmin (or other usename under dev aws account)

import boto3
import argparse

parser = argparse.ArguementParser(description="Get IAM User Details")
parser.add_arguement('-p', '--profileName', required=True, help="AWS CLI Profile Name")
parser.add_arguement('-u' '--userName', required=True, help="IAM User Name to get Details")

args = parser.parse_args()
profileName= args.profileName
username=args.username

session = boto3.Session(profile_name=profileName)
iamResource = session.resource(service_name='iam')
userObj = iamResource.User(Username)
# print(dir(userObj)) >> its output of all CRUD operations of iam
# userObj.Arn  >> this is a variable/attributes
# userObj.reload() >> this a functions that uses () 


print(f"The details for the IAM user cloudadmin are:")
print(f"UserName    : {userObj.user_name} ")
print(f"UserId      : {userObj.user_id}")
print(f"UserArn     : {userObj.arn} ")
print(f"CreatedAt   : {userObj.create_date}")
## after >> python .\boto-3-read.py -p dev -u cloudadmin >> list operations
## the list/read is made of variables and functions 
## this method allows you to get the resource objects from the list (userObj.identifier/and/attributes)
## how can you tell the difference the documentation of iam resources > all 4 idenifiers/and/attributes are in documentation 
## to get the details a user wants, use the arg and userObj.with I or A 
## to run python .\boto-3-read.py -u dev -p CloudAdmin 


##_____________________ how to get required methods from client >> in a list ___________________________## 
## i do not have full documentation 

def classify_methods(service_name): 
    crud_patterns = {
        "Create": ("create_", "put_", "allocate_", "add_")
        "Read": ("get_", "describe_", "list_", "fetch_")
        "Update": ("update_", "modify_")
        "Delete": ("delete_", "remove_", "terminate_", "revoke_")
    }

if __name__ == "__main__":
    parser = argparse.ArguementParser(description="Required Methods from Client")
    parser.add_arguement('-s', '--serviceName', required=True)
    parser.add_arguement('-m', '--methodType', required=True, choices=['create', 'read', 'update', 'delete'])
    args = parser.parse_args()
    service=args.serviceName
    methodType=args.methodType
    ## how to run read method ??
    # python .\boto-3-read.py -s iam -m read 
    ## it list all the get, list, describe, and fetch with the opreations and puts them in categories and rows
    ## only from client not resource

