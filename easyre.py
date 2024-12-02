import requests

cookies = {
    'B106E2F6056FE017': '923ba39ee2c940c6b6e1e817ba92b793',
    'intercom-id-b61auz06': '63c73456-9f43-4f5d-8e7b-ba40ca842d69',
    'intercom-device-id-b61auz06': '551663a4-7f84-438d-8be4-b2c4835cfef4',
    '_fbp': 'fb.1.1727170727437.876338041237664726',
    '_hjSessionUser_2541258': 'eyJpZCI6ImE0YTI5ZDVhLTVlMTAtNWY4ZC04ZmJlLWQxNjI0MzNmZTA3ZSIsImNyZWF0ZWQiOjE3MjcxNzA3MjcyMTgsImV4aXN0aW5nIjp0cnVlfQ==',
    '_gcl_au': '1.1.178191118.1727170727.2000617837.1728761694.1728761699',
    '_ga_BXG1RKV8QE': 'GS1.1.1728761665.2.1.1728762624.0.0.0',
    '_gid': 'GA1.2.443364736.1732610685',
    '_clck': '8oxbwk%7C2%7Cfr7%7C0%7C1727',
    'intercom-session-b61auz06': '',
    '_ga_9NYNPYXV0H': 'GS1.1.1732610798.7.1.1732610831.27.0.0',
    '_ga': 'GA1.2.245238143.1727096596',
    '_gat': '1',
    '_clsk': 'o7ggx7%7C1732610967476%7C9%7C1%7Co.clarity.ms%2Fcollect',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    # 'Cookie': 'B106E2F6056FE017=923ba39ee2c940c6b6e1e817ba92b793; intercom-id-b61auz06=63c73456-9f43-4f5d-8e7b-ba40ca842d69; intercom-device-id-b61auz06=551663a4-7f84-438d-8be4-b2c4835cfef4; _fbp=fb.1.1727170727437.876338041237664726; _hjSessionUser_2541258=eyJpZCI6ImE0YTI5ZDVhLTVlMTAtNWY4ZC04ZmJlLWQxNjI0MzNmZTA3ZSIsImNyZWF0ZWQiOjE3MjcxNzA3MjcyMTgsImV4aXN0aW5nIjp0cnVlfQ==; _gcl_au=1.1.178191118.1727170727.2000617837.1728761694.1728761699; _ga_BXG1RKV8QE=GS1.1.1728761665.2.1.1728762624.0.0.0; _gid=GA1.2.443364736.1732610685; _clck=8oxbwk%7C2%7Cfr7%7C0%7C1727; intercom-session-b61auz06=; _ga_9NYNPYXV0H=GS1.1.1732610798.7.1.1732610831.27.0.0; _ga=GA1.2.245238143.1727096596; _gat=1; _clsk=o7ggx7%7C1732610967476%7C9%7C1%7Co.clarity.ms%2Fcollect',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

response = requests.get('https://www.easyleadz.com/company/sangeetha-mobiles', headers=headers)
print(response.text)