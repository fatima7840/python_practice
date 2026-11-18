import sys
print(sys.version)
print(sys.version_info)
print(sys.version_info.major)
print(sys.version_info.minor)
print(sys.version_info.micro)
print(sys.executable)
print(sys.argv)

if len(sys.argv)!=3:
    print("usage: python system.py name age")
    sys.exit(1)
name=sys.argv[1]
age=sys.argv[2] 
print("name:",name)
print("age:",age)   
