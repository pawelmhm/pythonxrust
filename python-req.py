import requests
import time

def main():
    start = time.time()
    s = requests.get('http://localhost:3000')
    end = time.time()
    print(end - start)
    return s

main()