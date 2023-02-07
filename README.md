# LDAPEnumeration
First, it asks for the IP address and domain, then it runs it through gobuster for a DNS enumeration, 
then it goes through enum4linus, smbmap, and smbclient, then it enumerates LDAP with nmap, then finally,
it does a user enumeration with crackmapexec. It also prints out what it’s doing for fun.

NOTE: As with everything I put up, this is just my attempt at learning. While it may or may not work for you, and you may need to tweak things to fit your needs
please keep this in mind. Finally, I'm not responsible for whatever it is you decide to do with this. There are better LDAP Enumeration scripts out there for you.

Enjoy!
