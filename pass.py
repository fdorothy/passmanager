#!/usr/bin/python -O
import base64, getpass, hashlib, os

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

def read_domains():
  if os.path.isfile('domains.txt'):
    with open('domains.txt', 'r') as f:
      domains = set(f.read().strip().split('\n'))
    return domains
  else:
    return set([])

def save_domain(domain):
  domains = read_domains()
  if not (domain in domains):
    remember = raw_input("New domain, save to disk? [y/N] ").lower() == 'y'
    if remember:
      with open('domains.txt', 'a') as f:
        f.write("%s\n" % domain)

key = get_key()
while True:
  print " (default) 1: Create or lookup password for domain"
  print "           2: Show stored domain passwords"
  print "           3: List stored domains\n"
  cmd = raw_input('command: ')
  if cmd == '1' or cmd == '':
    domain = raw_input('Domain: ').lower()
    print('Password: ' + password(key, domain))
    save_domain(domain)
  elif cmd == '2':
    domains = list(read_domains())
    domains.sort()
    colwidth = max([len(x) for x in domains + ['domains']]) + 3
    print ""
    print "%*s | passwords" % (colwidth, "domains")
    for domain in domains:
      print "%*s | %s" % (colwidth, domain, password(key, domain))
    print ""
  elif cmd == '3':
    domains = list(read_domains())
    domains.sort()
    for domain in domains:
      print domain
    print ""
