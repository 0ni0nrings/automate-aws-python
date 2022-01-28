import boto3

def Start_Logging(name):
    cloudtrail_client = boto3.client('cloudtrail')
    response = cloudtrail_client.start_logging(
        Name=name
    )
    print(response)
    return True
    
def Get_Cloudtrail_Status(name):
    cloudtrail_client = boto3.client('cloudtrail')
    try:
        response = cloudtrail_client.get_trail_status(
            Name=name
        )
    except cloudtrail_client.exceptions.TrailNotFoundException:
        raise NameError("The cloudtrail trail was not found")
    
    return response.get('IsLogging')
    
def Stop_Logging(name):
    cloudtrail_client = boto3.client('cloudtrail')
    response = cloudtrail_client.stop_logging(
        Name=name
    )
    print(response)
    return True

if __name__ == "__main__":
    Name = 'cloudtrail' # Name of existing cloudtrail trail
    # Stop_Logging(Name)
    if not Get_Cloudtrail_Status(Name):
        Start_Logging(Name)
    else:
        print(f"Logging already enabled on trail named {Name}")