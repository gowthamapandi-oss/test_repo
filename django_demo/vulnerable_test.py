import os
import subprocess

# Semgrep will flag these:
password = "hardcoded_password_123"  # hardcoded-credential
user_input = input("Enter command: ")
os.system(user_input)  # command-injection
subprocess.call(user_input, shell=True)  # dangerous-subprocess-use

import hashlib
hashlib.md5(b"data")  # insecure-hash-algorithm
