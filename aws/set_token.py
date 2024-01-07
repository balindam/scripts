import json
import subprocess
import time

profile_name = input("Enter the Base Account profile name: ")
role_arn = 'arn:aws:iam::715111181214:role/usaf-developer-role'
role_session_name = 'session' + str(time.time())
mfa_arn = 'arn:aws:iam::074068173520:user/balindam@opslab.com'
token_code = input("Enter the MFA Token: ")

cmd = ['aws', 'sts', 'assume-role', '--role-arn', role_arn, '--role-session-name', role_session_name, '--serial-number', mfa_arn, '--profile', profile_name, '--token-code', token_code, '--region', 'us-east-1']
proc = subprocess.check_output(cmd)
# print proc
response = json.loads(proc)
credential = response['Credentials']

cmd = ['aws', 'configure', 'set', 'aws_access_key_id', credential['AccessKeyId'], '--profile', 'training']
proc = subprocess.call(cmd)
print(proc)

cmd = ['aws', 'configure', 'set', 'aws_secret_access_key', credential['SecretAccessKey'], '--profile', 'training']
proc = subprocess.call(cmd)
print(proc)

cmd = ['aws', 'configure', 'set', 'aws_session_token', credential['SessionToken'], '--profile', 'training']
proc = subprocess.call(cmd)
print(proc)

cmd = ['aws', 'configure', 'set', 'region', 'us-east-1', '--profile', 'training']
proc = subprocess.call(cmd)
print(proc)

print(credential['AccessKeyId'])
print(credential['SecretAccessKey'])
print(credential['SessionToken'])
print(credential['Expiration'])
