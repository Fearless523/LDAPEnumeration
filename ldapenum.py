#!/usr/bin/env python3
import subprocess
import shlex
 
# Prompt user for target IP address, domain, and if known, username and password
ip_address = input("Enter the target IP address: ")
domain = input("Enter the target domain: ")
username = input("Enter the target username (Press enter to skip): ")
password = input("Enter the target password (Press enter to skip): ")
 
 
# Enumerate DNS with gobuster
subprocess.run(shlex.split(f"gobuster dns -d {domain} -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-20000.txt -t 50 -o dns-results.txt"))
 
# Check for null and Guest access with enum4linux, smbmap, and smbclient
print("Running enum4linux -a -u '' -p '' {ip_address}")
subprocess.run(shlex.split(f"enum4linux -a -u '' -p '' {ip_address}"))
print("Running enum4linux -a -u 'guest' -p '' {ip_address}")
subprocess.run(shlex.split(f"enum4linux -a -u 'guest' -p '' {ip_address}"))
print("Running smbmap -u '' -p '' -P 445 -H {ip_address}")
subprocess.run(shlex.split(f"smbmap -u '' -p '' -P 445 -H {ip_address}"))
print("Running smbmap -u 'guest' -p '' -P 445 -H {ip_address}")
subprocess.run(shlex.split(f"smbmap -u 'guest' -p '' -P 445 -H {ip_address}"))
print("Running smbclient -U '%' -L //{ip_address}")
subprocess.run(shlex.split(f"smbclient -U '%' -L //{ip_address}"))
print("Running smbclient -U 'guest%' -L //")
subprocess.run(shlex.split(f"smbclient -U 'guest%' -L //"))
 
# Enumerate LDAP with nmap
print("Enumeraing LDAP with nmap")
subprocess.run(shlex.split(f"nmap -n -sV --script 'ldap* and not brute' -p 389 {ip_address}"))
 
# User enumeration with crackmapexec for null and Guest access
print("Enumerating for Null and Guest access with CrackMapExec")
subprocess.run(shlex.split(f"crackmapexec smb {ip_address} --users [-u '' -p ''] -M ldap_enumusers"))
 
# User enumeration with crackmapexec, if username and password is provided
print("User enumeration with crackmapexec, if username and password is provided")
if username and password:
                subprocess.run(shlex.split(f"crackmapexec smb {ip_address} -u {username} -p {password} -M ldap_enumusers"))
else:
                print("Skipping validated user enumeration, as username and password not provided.")
    
# List shares accessible to the provided user
print("Listing shares, if username and password is provided")
if username and password:
                subprocess.run(shlex.split(f"smbclient -U '{username}[{password}]' -L [--pw-nt-hash] //{ip_address}"))
else:
                print("Skipping validated shares enumeration, as username and password not provided.")
