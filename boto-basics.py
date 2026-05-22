import boto3 

session = boto3.session(profile_name="dev")
# in order active the session to use services need pass in credianals for AWS_ACCESS_KEY_ID/ AWS_SECRET_ACCESS_KEY
## Never hardcode them also put them in a aws/hashcorp vault or other tools
## make profiles that is used in production 
## you can have the code in github >> just not the credentials 



iamClient = session.client(service_name="iam")
# this is how to call on a client for services 
## with client before the = sign, it can be changed to match what the client is calling such as iam or ec2 or any object to memory

ec2Client = session.client(service_name="ec2")

iamResource = session.resource(service_name="iam")
# this is how to call on a resource for services
ec2Resource = session.resource(service_name="ec2")

## NOTE RESOURCES ARE NOT AVAILABLE FOR ALL AWS SERVICES 
print(boto3.Session().get_available_resource())
## HERE IS THE SYNAX TO SEE ALL THAT IS AVAILABLE >> make a list of it 