import requests

cookies = {
    'st': '84b1016a-8ab6-4e2d-a25b-913ef101f17b',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://tracxn.com',
    'priority': 'u=1, i',
    'referer': 'https://tracxn.com/search?q=a',
    'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
}

json_data = {
    'query': {
        'keyword': [
            'aa',
        ],
    },
}

response = requests.post('https://platform.tracxn.com/api/2.2/ps/companies', cookies=cookies, headers=headers, json=json_data)
res = response.json()
print(res, len(res['result']))