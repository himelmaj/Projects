import socket as s
my_hostname = s.gethostname()
my_ip = s.gethostbyname(my_hostname)

host_name = f'Your Hostname is {my_hostname}'
ip = f'You address is {my_ip}'

print(host_name)
print(ip)




