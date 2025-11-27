# The Worst Python Project Of 2025

import time
user = int(input("seconds: ")) # ask the user for seconds to countdown
print(user)
for i in range(user):
	time.sleep(1)
	user -= 1
	print(user)
print("Time Is Up.")
