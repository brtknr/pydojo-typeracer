multiple people

send some string

return back same string

check equal and calc time

hard coded strings

http api

$ typeracer localhost

- each client sent string

    - $ curl "localhost:5000/current-string?user=louis"
- at each char
    - $ curl http://localhost:5000/check-string -d "submission=this is a string" -X PUT
- server sends back msg if correct
- rank users by time

