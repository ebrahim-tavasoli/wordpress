#!/usr/bin/python

import os
import re

email = os.environ.get('EMAIL', None)
domain = os.environ.get('DOMAIN', None)

if not email and re.match(r'^\w+@\w+\.\w+$', email):
    raise Exception('Set a valid email to EMAIL enviroment variable.')

if not domain and re.match(r'^\w+\.\w+', domain):
    raise Exception('Set a valid domain to DOMAIN enviroment variable.')

print(os.system(f'certbot -n --nginx --agree-tos -m {email} -d {domain}'))
