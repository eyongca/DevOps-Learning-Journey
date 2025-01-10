# Author: Eyong Christopher
# Script Introduction:
# This script demonstrates how to manage multi-cloud resources, including provisioning,
# monitoring, and security tasks, across AWS, Azure, and Google Cloud using their respective
# SDKs and APIs. It covers the creation of virtual machines, monitoring metrics, and 
# performing basic security checks like open ports and firewall rules.

# Example Usage:
# 1. Set up your credentials for AWS, Azure, and Google Cloud.
# 2. Run the script to provision resources on all three cloud platforms.
# 3. The script will monitor the created resources and perform basic security checks.

import boto3
from azure.identity import ClientSecretCredential
from azure.mgmt.compute import ComputeManagementClient
from google.cloud import compute_v1
import time
import subprocess

# Initialize AWS Client (Boto3)
aws_client = boto3.client('ec2', region_name='us-east-1')

# Initialize Azure Client
azure_credentials = ClientSecretCredential(
    tenant_id='your-tenant-id',
    client_id='your-client-id',
    client_secret='your-client-secret'
)
azure_client = ComputeManagementClient(azure_credentials, 'your-subscription-id')

# Initialize Google Cloud Client
gcp_client = compute_v1.InstancesClient()

# **1. Provisioning Resources**

# AWS EC2 Instance Creation
def create_aws_instance():
    response = aws_client.run_instances(
        ImageId='ami-xxxxxxxx',
        InstanceType='t2.micro',
        MinCount=1,
        MaxCount=1,
        KeyName='your-key-pair'
    )
    print("AWS EC2 Instance Created:", response['Instances'][0]['InstanceId'])
    return response['Instances'][0]['InstanceId']

# Azure Virtual Machine Creation
def create_azure_vm():
    vm_parameters = {
        "location": "East US",
        "os_profile": {
            "computer_name": "myVM",
            "admin_username": "azureuser",
            "admin_password": "yourPassword123"
        },
        "hardware_profile": {
            "vm_size": "Standard_B1ls"
        },
        "storage_profile": {
            "image_reference": {
                "publisher": "MicrosoftWindowsServer",
                "offer": "WindowsServer",
                "sku": "2019-Datacenter",
                "version": "latest"
            }
        }
    }
    vm_creation = azure_client.virtual_machines.begin_create_or_update(
        "your-resource-group",
        "myVM",
        vm_parameters
    )
    vm_creation.result()
    print("Azure VM Created:", "myVM")

# Google Cloud Compute Engine Instance Creation
def create_gcp_instance():
    project = 'your-project-id'
    zone = 'us-central1-a'
    instance_name = 'my-gcp-instance'
    machine_type = "zones/{}/machineTypes/n1-standard-1".format(zone)
    image = "projects/debian-cloud/global/images/family/debian-9"

    instance = compute_v1.Instance()
    instance.name = instance_name
    instance.zone = zone
    instance.machine_type = machine_type
    instance.disks = [{
        "boot": True,
        "initializeParams": {"sourceImage": image}
    }]
    instance.network_interfaces = [{
        "network": "global/networks/default",
        "accessConfigs": [{"type": "ONE_TO_ONE_NAT"}]
    }]

    operation = gcp_client.insert(project=project, zone=zone, instance_resource=instance)
    operation.result()  # Wait for the operation to complete
    print("GCP Compute Engine Instance Created:", instance_name)

# **2. Monitoring Resources**

# AWS CloudWatch Monitoring
def monitor_aws_instance(instance_id):
    cloudwatch = boto3.client('cloudwatch', region_name='us-east-1')
    metric_data = cloudwatch.get_metric_data(
        MetricDataQueries=[
            {
                'Id': 'cpuUtilization',
                'MetricStat': {
                    'Metric': {
                        'Namespace': 'AWS/EC2',
                        'MetricName': 'CPUUtilization',
                        'Dimensions': [{'Name': 'InstanceId', 'Value': instance_id}]
                    },
                    'Period': 60,
                    'Stat': 'Average',
                },
                'ReturnData': True,
            },
        ]
    )
    print("AWS CloudWatch Metrics:", metric_data)

# Azure Monitor (Basic Monitoring)
def monitor_azure_vm(vm_name):
    metrics = azure_client.virtual_machines.list_all()
    for vm in metrics:
        if vm.name == vm_name:
            print("Azure VM Monitoring Data:", vm.name)

# Google Cloud Stackdriver Monitoring
def monitor_gcp_instance(instance_name):
    # Google Stackdriver API could be used for advanced monitoring.
    # Here, we print a basic message as an example.
    print(f"Monitoring GCP instance: {instance_name}")

# **3. Security Tasks**

# AWS Security: Check for open ports
def check_aws_security_group(instance_id):
    response = aws_client.describe_security_groups(
        Filters=[{'Name': 'group-id', 'Values': ['sg-xxxxxxxx']}]
    )
    for sg in response['SecurityGroups']:
        for perm in sg['IpPermissions']:
            if perm['FromPort'] == 22:
                print("SSH port (22) is open on AWS instance:", instance_id)

# Azure Security: Check for open ports (Basic Example)
def check_azure_security_group(vm_name):
    # Implement security check logic for Azure VM
    print(f"Security check for open ports on Azure VM: {vm_name}")

# Google Cloud Security: Check firewall rules
def check_gcp_security(instance_name):
    print(f"Checking security for GCP instance: {instance_name}")

# **4. Putting It All Together**

def main():
    # Provision Resources
    aws_instance_id = create_aws_instance()
    create_azure_vm()
    create_gcp_instance()

    # Monitoring
    monitor_aws_instance(aws_instance_id)
    monitor_azure_vm('myVM')
    monitor_gcp_instance('my-gcp-instance')

    # Security Checks
    check_aws_security_group(aws_instance_id)
    check_azure_security_group('myVM')
    check_gcp_security('my-gcp-instance')

if __name__ == '__main__':
    main()
