#!/usr/bin/python -O
import base64, getpass, hashlib

def get_key():
  key = getpass.getpass('Key: ')
  confirm_key = getpass.getpass('Confirm Key: ')
  while key != confirm_key:
    print "Keys do not match, try again"
    key = getpass.getpass('Key: ')
    confirm_key = getpass.getpass('Confirm Key: ')
  return key

def password(key, domain):
  bits = domain + '/' + key
  for i in range(2 ** 16):
    bits = hashlib.sha256(bits).digest()
    password = base64.b64encode(bits)[:16]
  return password

key = get_key()
while True:
  domain = raw_input('Domain: ').lower()
  print('Password: ' + password(key, domain))
