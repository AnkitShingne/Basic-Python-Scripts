# Python Program - Shutdown Computer
	
import os
print("Want to shutdown your computer ? (y/n): ")
check = input()
if check == 'y':
	os.system("shutdown /s /t 1")