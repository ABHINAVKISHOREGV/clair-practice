import os
import subprocess
import json

def write_json_file(filename):
    with open(filename, "r") as f:
        data= json.load(f)
    for i in range(len(data[0])-1):
    	print("Name of the image: ",data[i]["image"])
    	for j in data[i]["vulnerabilities"]:
    		if j["severity"]=="Critical" or j["severity"]=="High":
    			for k,l in j.items():
    				print(k," : ",l)
    			print()
    	print()
if __name__ == "__main__":
    data=''
    write_json_file(' /tmp/artifacts/result.json')
