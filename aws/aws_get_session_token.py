#!/usr/bin/python
import subprocess
import json
import sys
device_arn = sys.argv[1]
aws_profile = sys.argv[2]
totp = sys.argv[3]

get_session_token = 'aws sts get-session-token --serial-number {0} --profile {1} --duration-seconds 129600 --token-code {2}'.format(device_arn,aws_profile,totp)
sessionToken = subprocess.check_output(get_session_token,shell=True)
jsonToken = json.loads(sessionToken)['Credentials']
accessKey = jsonToken['AccessKeyId']
secretAccessKey = jsonToken['SecretAccessKey']
sessionToken = jsonToken['SessionToken']

#It will update / create profile aws_profile+'_mfa'. (A profile with _mfa concatenated with your profile will be created)
cmd = ['aws', 'configure', 'set', 'aws_access_key_id', accessKey, '--profile', aws_profile+'_mfa']
proc = subprocess.call(cmd)

cmd = ['aws', 'configure', 'set', 'aws_secret_access_key', secretAccessKey, '--profile', aws_profile+'_mfa']
proc = subprocess.call(cmd)

cmd = ['aws', 'configure', 'set', 'aws_session_token', sessionToken, '--profile', aws_profile+'_mfa']
proc = subprocess.call(cmd)

cmd = ['aws', 'configure', 'set', 'region', 'us-east-1', '--profile', aws_profile+'_mfa']
proc = subprocess.call(cmd)
