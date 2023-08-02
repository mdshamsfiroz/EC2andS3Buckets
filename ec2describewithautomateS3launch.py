import boto3

# Create an EC2 client
ec2_client = boto3.client('ec2')

# Call describe_instances to get EC2 instance
response_ec2 = ec2_client.describe_instances()

# Print EC2 
print("EC2 Instances:")
print(response_ec2)

# Create an S3 client
s3_client = boto3.client('s3')

# Call create_bucket to create an S3 bucket
response_s3 = s3_client.create_bucket(
    ACL='private',  # Use 'private' instead of 'enabled' for private ACL
    Bucket='shamsfirozdf',
    CreateBucketConfiguration={
        'LocationConstraint': 'ap-south-1'  # Use the region code, not the region name
    }
)

# Print S3 response
print("S3 Bucket Creation Response:")
print(response_s3)
