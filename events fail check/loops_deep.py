failed_events=0
succes_events=0
locked_events=0
unknown_events=0
events = [
    "SUCCESS",
    "FAILED",
    "FAILED",
    "SUCCESS",
    "FAILED",
    "LOCKED",
    "UNKNOWN",
    "UNKNOWN",
    "FAILED"
]

for event in events:
	if event =="FAILED":
		failed_events+=1
		print("Failed login detected")
	elif event=="SUCCESS":
		succes_events+=1
		print("SUCCESS LOgin")
	elif event=="LOCKED":
		locked_events+=1
		print("CRITICAL: Account locked")
	else:
		unknown_events+=1
		print("Unknown login")
		
if failed_events>=3:
	print("HIGH ALERT")
	
print("=======summary=======")
print(f"total failed login detected: {failed_events}")
print(f"total success login detected: {succes_events}")
print(f"total locked login detected: {locked_events}")
print(f"total locked unkown detected: {unknown_events}")
