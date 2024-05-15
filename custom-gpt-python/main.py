# Import necessary packages
import os
import pickle
import redis
import json

from google.auth.transport.requests import Request

from google_auth_oauthlib.flow import InstalledAppFlow
from llama_index import GPTVectorStoreIndex, download_loader

from dotenv import load_dotenv

load_dotenv()

redis_host = 'chatgpt-project-redis-1'
redis_port = 6379
redis_client = redis.Redis(host=os.environ.get('REDIS_HOST'), decode_responses=True)

def authorize_gdocs():
    google_oauth2_scopes = [
        "https://www.googleapis.com/auth/documents.readonly"
    ]
    cred = None
    if os.path.exists("token.pickle"):
        with open("token.pickle", 'rb') as token:
            cred = pickle.load(token)
    if not cred or not cred.valid:
        if cred and cred.expired and cred.refresh_token:
            cred.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", google_oauth2_scopes)
            cred = flow.run_local_server(port=0)
        with open("token.pickle", 'wb') as token:
            pickle.dump(cred, token)

def is_jsonable(x):
    try:
        json.dumps(x)
        return True
    except (TypeError, OverflowError):
        return False

def main():
    print("Listening on 'request-channel'...")
    pub_sub = redis_client.pubsub()
    pub_sub.subscribe('request-channel')

    for pub_message in pub_sub.listen():
        if pub_message['channel'] == 'request-channel':
            print(pub_message['data'])
            if pub_message['data'] == 1:
                print("Subscription successful!")
            elif is_jsonable(pub_message['data']):
                request = json.loads(pub_message['data'])
                request_channel = request['channel']
                request_message = request['message']
                print('Received request:', request_message)

                query_engine = index.as_query_engine()
                response = str(query_engine.query(request_message)).strip()
                print('Response:', response)

                redis_client.publish(request_channel, json.dumps({
                    'channel': request_channel,
                    'query': request_message,
                    'response': response
                }))

print('Authorizing gdocs...')
authorize_gdocs()

GoogleDocsReader = download_loader('GoogleDocsReader')

gdoc_ids = [os.environ.get('GDOCS_FILE_ID')]

loader = GoogleDocsReader()

print('Loading and indexing documents...')
documents = loader.load_data(document_ids=gdoc_ids)
index = GPTVectorStoreIndex.from_documents(documents)
print('Documents loaded and indexed!')

main()