import requests
import time

def main():
    api_url = "http://zenquotes.io/api/quotes"

    for i in range(6)
        response = requests.get(api_url)

        if response.status_code == 200:
            data = response.json()
            if data:
                first_item = data(0)
                print(first_item['q'])
            else:
                Print("API request failed with status code", response status_code)

            time.sleep(5)

if __name__=="__main__":
    main()