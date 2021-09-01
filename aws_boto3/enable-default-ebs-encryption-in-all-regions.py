import boto3

ec2 = boto3.client('ec2', region_name='us-west-2')
regions = ec2.describe_regions()

for region in regions['Regions']:
    print(region['RegionName'])
    client = boto3.client('ec2', region['RegionName'])
    response = client.enable_ebs_encryption_by_default()
    print("Default EBS Encryption for region", region, ": ", response['EbsEncryptionByDefault'])
