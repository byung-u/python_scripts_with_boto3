#!/usr/bin/env python3
import boto3
import os
import sys


def main():
    if len(sys.argv) != 2:
        print('[ERROR] must input aws key')
        sys.exit(1)
    aws_access_key = os.environ.get('AWS_ACCESS_KEY')
    aws_secret_key = os.environ.get('AWS_SECRET_KEY')
    aws_regions = ['ap-sxxxx-1', 'ap-southxxxx-1']
    for region in aws_regions:
        bh_iam = boto3.client('iam',
                              aws_access_key_id=aws_access_key,
                              aws_secret_access_key=aws_secret_key,
                              region_name=region)
        users = bh_iam.list_users()['Users']
        for user in users:
            keys = bh_iam.list_access_keys(UserName=user['UserName'])['AccessKeyMetadata']
            for key in keys:
                if key['Status'] == 'Inactive':
                    continue
                if key['AccessKeyId'] == sys.argv[1]:
                    print('Created:', key['CreateDate'])
                    print(key['UserName'])
                    sys.exit(1)


if __name__ == '__main__':
    # USAGE: $ whose_aws_key AKIAJXXXXXXXXXXXXXNQ 
    main()
