# 273_Assignment1

1. Create a python program and upload it to the local server using CURL POST method

curl -i -X POST -H "Content-Type: multipart/form-data" 
-F "data=@/tmp/foo.py" http://localhost:8000/api/v1/scripts

2. Execute and retrive the program executed by GET method

curl -i
http://localhost:8000/api/v1/scripts/123456
