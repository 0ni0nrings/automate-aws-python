import boto3

DRYRUN = True

ec2_client = boto3.client('ec2')
images = ec2_client.describe_images(
    Filters=[
        {
            'Name': 'name',
            'Values': [
                'amzn2-ami-hvm*',
            ]
        },
        {
            'Name': 'owner-alias',
            'Values': [
                'amazon',
            ]
        }
    ]    
)
ec2_image = boto3.resource('ec2')
AMI = ec2_image.Image(images['Images'][0]['ImageId'])
# imageId = (images['Images'][0]['ImageId'])
if AMI.state == 'available':
    print(AMI.image_id)
    # print(imageId)
    instance = ec2_client.run_instances(
        # ImageId=imageId,
        ImageId=AMI.image_id,
        InstanceType='t2.micro',
        MaxCount=1,
        MinCount=1,
        DryRun=DRYRUN
    )
    ec2_instance = boto3.resource('ec2')
    ec2 = ec2_instance.Instance(instance['instances'][0]['InstanceId'])
    print(ec2.instance_id)
else:
    print("AMI not available")