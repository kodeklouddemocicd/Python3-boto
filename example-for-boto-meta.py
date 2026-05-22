import boto3

session=boto3.Session(profile_name='dev')

ec2Client=session.client(service_name='ec2')
ec2Resource=session.resource(service_name='ec2')

print(dir(ec2Client))
## dir =  prints the available operations on the service 
## find meta and add a other operation 

print(ec2Client.meta.region_name)
## what is saying find the live data from ec2 region name 
print (dir(ec2Client.meta))
## it lists the other operations that you can add on other than region_name
## combine them with the . on each operation

print(ec2Reource.meta.service_name)
print(dir(ec2Resource.meta))
## RESOURCE EXAMPLE == IT LIST A FEW LESS OPERATIONS TO PRINT ON DIR 

print(ec2Resource.meta.client.meta.region_name)
## NOTE: THIS EXAMPLE USES BOTH RESOURCE AND CLIENT TO GET A OPERATION RESOURCE DOES NOT HAVE 

def main():
### the agruements

if '__name__' == '__main__':
    main()
# this if statement means if main is ran on the cli/terminal only main function logic will be executed 

