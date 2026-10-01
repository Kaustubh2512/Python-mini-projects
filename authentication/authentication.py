failed_users={}
with open("authlog.txt", "r") as logfile:
	for loglines in logfile:
		loglines = loglines.strip()
		timestamp, username, ip, event, os, service = loglines.split(",")
		
			
		if event == "LOGIN_FAILED":
			if username in failed_users:
				failed_users[username] +=1
			else:
				failed_users[username] =1
	
print("========LOGIN REPORT=========")
for username, count in failed_users.items():
     print(username, ":", count, "failed attempts")
	
print("========Security Alerts=======")

for username, count in failed_users.items():
       if count >= 3:
             print("[Alert] Brute force attack")
				
