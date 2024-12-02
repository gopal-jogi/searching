import requests

cookies = {
    'intercom-id-b61auz06': 'e78e422e-a1dc-46c1-bc88-24ea1b498612',
    'intercom-session-b61auz06': '',
    'intercom-device-id-b61auz06': 'a5320bde-cb08-44d9-a65e-0e896cddde5d',
    'vtoken': '66fa390aad5834703730c7a5b9286848c6'
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Cookie': 'prcode=TtwryXxXE7; _clck=1tyebzj%7C2%7Cfpg%7C0%7C1728; B106E2F6056FE017=923ba39ee2c940c6b6e1e817ba92b793; intercom-id-b61auz06=e78e422e-a1dc-46c1-bc88-24ea1b498612; intercom-session-b61auz06=; intercom-device-id-b61auz06=a5320bde-cb08-44d9-a65e-0e896cddde5d; vtoken=66f28a6efb293764550da41a49eaf57145; _gcl_au=1.1.2021554766.1727171188; _gid=GA1.2.855769712.1727171188; _hjSession_2541258=eyJpZCI6ImFiNTQyNmNjLTY2YjAtNDY2YS1iODE0LThlNmJmNmY1MDA4MyIsImMiOjE3MjcxNzExODg2MzMsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MH0=; _fbp=fb.1.1727171188686.13430643367965379; _hjSessionUser_2541258=eyJpZCI6IjQ5ODg0NTY3LWZhMDctNThlMC05MjNiLTU2NjU5YWMwMWIwMyIsImNyZWF0ZWQiOjE3MjcxNzExODg2MzAsImV4aXN0aW5nIjp0cnVlfQ==; _gcl_aw=GCL.1727172611.Cj0KCQjwxsm3BhDrARIsAMtVz6PojR-TiG1GW9VkVeL9RtOvanShIdf3Z1Oefzod0EumdZAask2PsqkaAqITEALw_wcB; _ga_9NYNPYXV0H=GS1.1.1727171033.1.1.1727174766.60.0.0; _ga=GA1.1.1529207695.1727171034; _clsk=cwv99m%7C1727175357849%7C67%7C1%7Ct.clarity.ms%2Fcollect; PHPSESSID=7b8i16i2sovu6n7ji6fi4mrd94; _ga_BXG1RKV8QE=GS1.1.1727171188.1.1.1727175888.0.0.0',
    'DNT': '1',
    'Origin': 'chrome-extension://haphbbhhknaonfloinidkcmadhfjoghc',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'Session': '3e2742ffc8a01e387bc50f6402e91d4466f28a6e384491727171182',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
    'User-Token': 'eyJjaXBoZXJ0ZXh0IjoiTkJBTXhwQjB4RTg3UVg4UitOdkFIQzZvb2FuNlJEeUdzUmtma3BnMEYwcz0iLCJpdiI6IjUzYTZkMDFmOGYyMjNlNDJlZTNiYjY1YmE4NGVlMDdjIiwic2FsdCI6IjFlZjc1M2I3NmExMGQyMmM2ZWM0N2RjN2JmMDJjZDAwODk0MzQ4ZTViY2I1YWU0OTBkMDcxNDIzOTgxNGE0NDY4ZmMxY2ZhYzZlMTlmNzk3YjJkZDJkZjUzYTFhYTAyNjg4YjAwNGNiYTAwMjVmMTE4NDViMmY2MjlhYWJlY2I2MzU2OTI1ZmI1NmExZjQwOTE2YmY3NWMwMTA1MDQzMDI5MDFkYjU5NDAyZTM1MDgzNzI1OTIxNGY5Mzc1MGRhMzJlYTlmYTE0N2I0MTA0ZmJhZmZkYWFmYmY3ZmZmMWY2MGViNDg4MjIzZTcyYTZkNzE5YzBmZTZkYzlmNWI2ZmI5MzVhZjQ1OWFlYzg5ODlmY2FlNzVhYTQ5YWFhNzI2MmZiMmRmYWQyMDJlMWFiZjU5YzZiMDE3MjU4OTY4MzY0ZjUzY2YzZmZlZjA1ZGE3MjJhODQ1ZjdjMzY3NWMxY2YwMzg0YzNjMzU0MWI4NjU3MjQyODc5ODlkM2UyM2YzYWU0YmI0ZTdkNzRjMTkwNzg2MTkyOGFmYTYzMTNmMTg3ZjZlNTU3NDhiYmNiNjA4NDU4ZTgzMDFiM2ZjMTQ5NmIxOTMyNmM0NDY0ZjQ2NWRmNGY2MzI5MGQwYTllMDUyYzg2N2IyMzZiYjExYWFkNWIwNmU3NjFlNWMyNjBmMTZlIiwiaXRlcmF0aW9ucyI6OTk5fQ==',
    'sec-ch-ua': '"Google Chrome";v="128", "Not=A?Brand";v="8", "Chromium";v="128"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

data = {
    'url': 'https://www.linkedin.com/in/abhinavkaul26',
    'l': 'abhinavkaul26',
    'trldata': '{}',
}

response = requests.post('https://app.easyleadz.com/api/v5/show_email.php', cookies=cookies, headers=headers, data=data)
print(response.json())