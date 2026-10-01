
ips = [
    "192.168.1.10",
    "10.0.0.5",
    "192.168.1.10",
    "172.16.0.20",
    "10.0.0.5",
    "192.168.1.10"
]

unique_ips=set(ips)

ip_counts={}
print("total ips:",len(ips))
print("unique ips:",len(unique_ips))

for ip in ips:
	if ip in ip_counts:
		ip_counts[ip]+=1
	else:
		ip_counts[ip]=1
print(ip_counts)
print("Repeated ips")
for ip , count in ip_counts.items():
	if count>1:
		print(ip)
		
