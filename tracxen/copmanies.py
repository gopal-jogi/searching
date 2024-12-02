import re
import asyncio
import aiohttp
from aiohttp import ClientSession
from pymongo import MongoClient
from time import sleep
from pymongo import errors
from aiohttp_socks import ProxyConnector
from traceback import print_exc

write_db_username = ""
write_db_pwd = ""
write_db_ip = "" 
MONGODB_SECRET_URI = f"mongodb://{write_db_username}:{write_db_pwd}@{write_db_ip}:27017/?authMechanism=DEFAULT&authSource=admin"


def getSubUrls(html_content, url_prefix):
    # Define the URL prefix to search for
    # url_prefix = r'/d/companies/swiggy/__8L46lNfjqGM9DHz7xSR4zs7iWwa57QNKLZaVbfNa3T4/'
    url_prefix = url_prefix if url_prefix[-1] != "/" else url_prefix + '/'
    
    # Define the regex pattern to match anchor tags with the specified URL prefix
    pattern = re.compile(r'href="(' + re.escape(url_prefix) + r'[^"]*)"', re.IGNORECASE)

    # Find all matching anchor tags
    matches = pattern.findall(html_content)
    if len(matches) != 0:
        matches = set(matches)

    to_return = []
    for match in matches:
        if match != url_prefix:
            to_return.append(match)
    return to_return


# MongoDB connection setup
def mongoConnection(username, pwd, ip):  # connecting with database
    MONGODB_SECRET_URI = f"mongodb://{username}:{pwd}@{ip}:27017/?authMechanism=DEFAULT&authSource=admin"
    client = None
    try:
        client = MongoClient(MONGODB_SECRET_URI)
    except errors.ServerSelectionTimeoutError as e:
        client = MongoClient(MONGODB_SECRET_URI)
    return client

client = mongoConnection(write_db_username, write_db_pwd, write_db_ip)

db = client['indian_data_suite']
input_collection = db['tracxn_url_company']
output_collection = db['tracxn_company_profile']
COUNT_DONE = int(output_collection.estimated_document_count({}))

# Define your proxy details
proxy_host = "p.webshare.io"
proxy_port = "80"
proxy_username = "gbgiilwl-rotate"
proxy_password = "ai4swgza4orr"

class CustomException(Exception):
    pass

async def fetch(session, keyword):
    url = "https://tracxn.com"+keyword
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'max-age=0',
        # 'cookie': 'st=780754bf-e9a8-4cf0-a150-f399aa2f761a; _gid=GA1.2.38389950.1717733090; rurl=/a/d/company/-Lzowa-uxD2kP7tQxqBSPjpjm7CrgTURh_T4L7vL60c/clevertarget.ru/globalequivalent; _ga=GA1.1.1242486849.1717733090; _ga_63RZ0E5CHG=GS1.1.1717733089.1.1.1717733703.16.0.0; AID=abBQQB79Hql7zV4N5DeTM:I9y00xAq30WUeVb7YOmjk',
        'dnt': '1',
        'priority': 'u=0, i',
        'referer': 'https://google.com/',
        'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    }
    # Proxy URL format
    proxy_url = f'socks5://{proxy_username}:{proxy_password}@{proxy_host}:{proxy_port}'
    
    # async with session.post(url, headers=headers, json=body) as response:
    #     # print(response.text)
    #     try:
    #         resp = await response.json()
    #     except Exception as e:
    #         print("Failed to decode", e)
    #         raise CustomException("ERRORED")
    #     return resp
        # Use the proxy connector
    try:
        connector = ProxyConnector.from_url(proxy_url)
        async with ClientSession(connector=connector) as proxy_session:
            async with proxy_session.get(url, headers=headers) as response:
                try:
                    resp = await response.text()
                except Exception as e:
                    print(url)
                    print("Failed to decode", e)
                    raise CustomException("ERRORED")
                return {"url": url, "resp": resp, 'sub_links': getSubUrls(resp, keyword)}
    except Exception as e:
        print(url)
        print("Failed to fetch", e)
        raise CustomException("ERRORED!!")
            
async def fetch_all(keywords):
    async with aiohttp.ClientSession() as session:
        tasks = []
        i = 0
        for keyword in keywords:
            tasks.append(fetch(session, keyword))
            i+=1
            if len(tasks) == 5:  # Process 100 tasks in parallel
                responses = await asyncio.gather(*tasks)
                store_responses(responses)
                tasks = []  # Reset tasks for the next batch
                print("Hit", i, len(keywords))
                sleep(2)
        if tasks:  # Process any remaining tasks
            responses = await asyncio.gather(*tasks)
            sleep(2)
            store_responses(responses)

def store_responses(_responses):
    try:
        print("_responses", len(_responses))
        if len(_responses) > 0:
            output_collection.insert_many(_responses)
    except errors.BulkWriteError as e:
        print("Bulk write error")
        for item in _responses:
            try:
                output_collection.insert_one(item)
            except Exception as e:
                print("Error 1", e)
                continue
        
def get_keywords(chunk_size, offset):
    cursor = list(input_collection.find({}, {'url': 1, '_id': 0}).skip(offset).limit(chunk_size))
    print("cursor", len(cursor))
    input_cins = [doc['url'] for doc in cursor]
    # Retrieve CINs from the output collection that are in the input_cins
    processed_cins_cursor = output_collection.find(
        {'url': {'$in': input_cins}},
    )
    processed_cins_doc = list(processed_cins_cursor)
    print("processed_cins_doc", len(processed_cins_doc))
    processed_cins = set(processed_cins_doc['url']) if processed_cins_doc else set()
    # Filter out CINs that have already been processed
    new_cins = [cin for cin in input_cins if cin not in processed_cins]
    return new_cins

def main():
    global COUNT_DONE
    try:
        chunk_size = 100000
        total_docs = input_collection.count_documents({})
        print(chunk_size)

        for offset in range(COUNT_DONE, total_docs, chunk_size):
            COUNT_DONE=offset
            print(COUNT_DONE, total_docs)
            keywords = get_keywords(chunk_size, offset)
            print("Length of keywords", len(keywords))
            if len(keywords) != 0:
                loop = asyncio.get_event_loop()
                loop.run_until_complete(fetch_all(keywords))
    except CustomException as e:
        print("Sleeping")
        sleep(60*1)
        print("woke up")
        main()
    except Exception as e:
        print_exc()
        print("EXCEPT: Restarting!", e)
        main()
                
if __name__ == "__main__":
    main()