import boto3

def CreateBucket(name):
    s3_client = boto3.client('s3')
    try:
        s3_client.create_bucket(Bucket=name)
        return True
    except s3_client.exceptions.BucketAlreadyExists:
        print(f"Bucket {name} already exists")
        return False
    
def DeleteBucket(name):
    s3_client = boto3.client('s3')
    s3_client.delete_bucket(Bucket=name)
    return True
    
def EnforceS3Encryption(name):
    s3 = boto3.resource('s3')
    s3_client = boto3.client('s3')
    bucket = s3.Bucket(name)
    try:
        s3_client.get_bucket_encryption(Bucket=bucket.name)
        print("Encryption already set")
    except s3_client.exceptions.ClientError as error:
        if 'ServerSideEncryptionConfigurationNotFoundError' in str(error):
            print(f"Encrypting {bucket.name}")
            response = s3_client.put_bucket_encryption(
                Bucket=bucket.name,
                ServerSideEncryptionConfiguration={
                    'Rules': [
                        {
                            'ApplyServerSideEncryptionByDefault': {
                                'SSEAlgorithm': 'AES256'
                            }
                        }
                    ]
                    
                }
            )    
            print(response)
        else:
            raise error # catch all error
    
if __name__ == '__main__':
    Name = 'bucketalreadyexistsinhisregion'
    if CreateBucket(Name):
        EnforceS3Encryption(Name)
    # DeleteBucket(Name)
    