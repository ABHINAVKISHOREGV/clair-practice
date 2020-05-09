import os
import subprocess
import json

def write_json_file(filename):
    with open(filename, "r") as f:
        data= json.load(f)
    hi=0
    cr=0
    me=0
    lo=0
    neg=0
    for i in range(len(data[0])-1):
    	print("Name of the image: ",data[i]["image"])
    	for j in data[i]["vulnerabilities"]:
    		if j["severity"]=="Critical":
    			cr+=1
    		if j["severity"]=="High":
    			hi+=1
    		if j["severity"]=="Low":
    			lo+=1
    		if j["severity"]=="Medium":
    			me+=1
    		if j["severity"]=="Negligible":
    			neg+=1
    	print("No. of Critical vulnerabilities : ",cr)
    	print("No. of High vulnerabilities : ",hi)
    	print("No. of Medium vulnerabilities : ",me)
    	print("No. of Low vulnerabilities : ",lo)
    	print("No. of Negligible vulnerabilities  : ",neg)
    	print()
if __name__ == "__main__":
    data=''
    write_json_file('/tmp/artifacts/result.json')
