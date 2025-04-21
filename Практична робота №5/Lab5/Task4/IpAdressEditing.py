import re

def clean_ip_assress(ip):
    return re.sub(r'\b0*(\d+)\b', r'\1', ip)

ip_address = input("Enter ip address: ")
print(clean_ip_assress(ip_address))