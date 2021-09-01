import boto3
ec2 = boto3.client('ec2', region_name='us-west-2')

response = ec2.describe_key_pairs()
for keypair in response['KeyPairs']:
    response = ec2.describe_instances(
        Filters=[
            {
                'Name': 'key-name',
                'Values': [
                    keypair['KeyName']
                ]
            },
        ],
    )
    #print(response)
    if len(response['Reservations']) == 0:
        print(keypair['KeyName'])



