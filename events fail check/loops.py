failed_events=0

events = [
    "SUCCESS",
    "FAILED",
    "FAILED",
    "SUCCESS",
    "FAILED",
    "LOCKED",
    "FAILED"
]
	
for event in events:
	if event=="FAILED":
		failed_events+=1
		print("Failed login detected")
print(f"total failed login detected: {failed_events}")
