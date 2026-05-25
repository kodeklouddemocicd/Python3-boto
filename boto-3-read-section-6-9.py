### __________________section 6______________________###### 
#get iam role details 
import boto3
import argparse

parser = argparse.ArguementParser(description="Get IAM role Details")
parser.add_arguement('-p', '--profileName', required=True, help="AWS CLI Profile Name")
parser.add_arguement('-r' '--roleName', required=True, help="IAM Role Name to get Details")
args = parser.parse_args()
profileName= args.profileName
roleName= args.roleName


session = boto3.Session(profile_name=profileName)
iamClient = session.client(service_name='iam')

response = iamclient.get_role(
    RoleName=roleName
)
roleDetails = response.get_role('Role')
print(f"The IAM Role {Rolename} Details are")
print(f"RoleId                :{roleDetails.get('RoleId')}")
print(f"RoleArn               :{roleDetails.get('Arn')}")
print(f"CreatedAt             :{roleDetails.get('CreateDate')}")
print(f"PermissionBoundary    :{roleDetails.get('PermissionBoundary')}")
## method to get iam role details for client 
## use script with expections 
## to find "get_role" use section 5s CRUD list script 
## find the example syntax  >> pick the attributes user wants to display 
## run: python .\boto-3-read-section-6-9.py -p dev -r flaskapp or other roles on aws >> output: role details 



import boto3
import argparse

parser = argparse.ArguementParser(description="Get IAM role Details")
parser.add_arguement('-p', '--profileName', required=True, help="AWS CLI Profile Name")
parser.add_arguement('-r' '--roleName', required=True, help="IAM Role Name to get Details")
args = parser.parse_args()
profileName= args.profileName
roleName= args.roleName


session = boto3.Session(profile_name=profileName)
iamResource = session.resource(service_name='iam')

roleObj= iamResource.role(
    RoleName=roleName
)
print(f"The IAM Role {Rolename} Details are")
print(f"RoleId                :{roleObj.role.id}")
print(f"RoleArn               :{roleObj.arn}")
print(f"CreatedAt             :{roleObj.create_date}")
print(f"PermissionBoundary    :{roleObj.permission_boundary}")
## this method uses resource for rolename and print out any role on aws connected to the profile using argparse
## to run: python .\boto-3-read-section-6-9.py -p dev -r flaskapp or other roles on aws >> output: role details 
## to find the attrutibes go on documentation or do a print(dir(roleobj))

####___________________________section-7______________________###########
# develop client script to get aws id 



