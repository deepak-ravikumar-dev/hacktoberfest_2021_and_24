#regex (1+01)*00(1+10*)

import re
pattern= "(1|01)*00(1|10)*"
print("Enter the input: ")
ip=input()
if(re.search(pattern,ip)):
	print("Accepted")
else:
	print("Not Accepted")