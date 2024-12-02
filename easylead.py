import requests

cookies = {
    'intercom-id-b61auz06': '729f46fb-e4bb-4b8a-997c-b140bae1138e',
    'intercom-session-b61auz06': '',
    'intercom-device-id-b61auz06': '1653ffa4-d216-486e-b8f1-fc40473d3f8e',
    'vtoken': '66ed18e36d2392373b36ac91d1a762f102',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Cookie': 'intercom-id-b61auz06=729f46fb-e4bb-4b8a-997c-b140bae1138e; intercom-session-b61auz06=; intercom-device-id-b61auz06=1653ffa4-d216-486e-b8f1-fc40473d3f8e; vtoken=66ed18e36d2392373b36ac91d1a762f102',
    'DNT': '1',
    'Origin': 'chrome-extension://haphbbhhknaonfloinidkcmadhfjoghc',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'Session': 'fd5b77075938d7a5c839649bc8ad732b65b4eaec9eeec1706355436',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
    'User-Token': 'eyJjaXBoZXJ0ZXh0IjoieWpmSnZtWTJxWnY2bmZRRzVJb1E1RnROeGFYTlVOQ004a1A0MDJ5cTBxcz0iLCJpdiI6ImE2NDVkZTk0NmViMmE0MzIxOTdhNTYxMTJlNmQxN2Y4Iiwic2FsdCI6IjJlOTNjMWU1ZDI3MTFmNTE0MmE3OTg4ZGY0N2VjZmNkNzczZTZiZTk0MDE2NWQwZmQ2ZDBjYjNjZGQxZTY5ZjBlNWM4NjcxMDlkMDU2YjgwZjdiMjNmMGU4M2I0YTkxYTJiZmQwMzY1MDNmMjFhYTY3MzI5MWUxOWI3MmE5YTVhNTIwMTNhNmUwYTg4OTA2MGMyN2ZlOGZmYzk1NWZjMTRjODk0NWE2MTUwNTA4OTNiNjU5YzllNjlkYjAxZDlmNDIxMjA1YzE3OTYwYzJiNmU3M2U1MmY3NWQ0NTNkODBlNzNiYzdmYmM5MmZhMmMxNGM2MmQ2M2NkNmFjYjgxYTBhMGY1MWJkMmRmNjViZmMyZDlmOTQ2OWNlZWJlZjg3ZTY1NTdkNjMwYWQ5OWVkY2ZhNjg3MmM1NWY2NDI3MWIzOTY3OTE2ODU2MjEwMzBjZWRiMjA4ZTRiNDIwMmY0NzQ1YTAwMzBmOWM5Y2NhZGEyNGNkNjNmMDMyYTViNTc1Mjg0MmY5ZDVjNDk5ZWE5ZGFkY2U3ZmVkNDY4MTg0NGUzMzZlNmU1ZTgzZGI0NzU3ZDYyZjAxNzEzYWJhMzE4YTU0Y2IyMzA5Mjk0M2IzZThiOTZmZDU3OTI4NjYxMWFjOWM2MjExZTJjMDc1OTFmZjk5ZDEyNTUwNzNlOWY0OTRhIiwiaXRlcmF0aW9ucyI6OTk5fQ==',
    'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
}

data = {
    'url': 'https://www.linkedin.com/in/abhinavkaul26',
    'l': 'abhinavkaul26',
    'trldata': '{}',
}

response = requests.post('https://app.easyleadz.com/api/v5/show_email.php', cookies=cookies, headers=headers, data=data)
print(response.json())