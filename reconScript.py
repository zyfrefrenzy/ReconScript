import socket
import requests

def bunner():
    print("~"*20)
    print()
    print("this is a recon script")
    print()
    print("~"*20)

def get_ip(domain):
    try:
        ip=(socket.gethostbyname(domain))
        print(f"the ip address is:{ip}")
    except socket.gaierror:
        print("Could not resolve ip")

def get_headers(url):
    try:
        response= requests.get(url, timeout=5)
        print(f"Status code:{requests.status_codes}")

        
        print("Headers: ")

        for header,value in response.headers.items():
            print(f"{header} {value}")
    except requests.exceptions.RequestException as error:
        print(f"error connecting to website {error}")



def main():
    bunner()

    target=input("enter your target domain, example:  example.com: ")
    url=input("enter your url, example: http://example: ")

    print("resolving domain.....")
    get_ip(target)

    print("getting HTTP headers ")
    get_headers(url)


if __name__=="__main__":
    main()