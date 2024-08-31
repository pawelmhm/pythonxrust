import http.client
import time

def main():
    start = time.time()
    host = 'localhost:3000'
    conn = http.client.HTTPConnection(host)
    conn.request('GET', "/")
    response = conn.getresponse()
    response.read()
    end = time.time()
    print(end - start)
    return response

main()