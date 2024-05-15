# ChatGPT-Project

## Setup Google Docs API

- Go to https://console.cloud.google.com/
- Create a new project and select it
- Go to the **APIs & Services** from the left-hand menu and click **+ ENABLE APIS AND SERVICES**
- Search for **Google Docs API** and click **Enable**
- Click on the **OAuth consent screen** from the left-hand menu
- Select **External**
- Enter the **App name**, **User support email** and **Developer contact information**
- Click **SAVE AND CONTINUE**
- Click **ADD OR REMOVE SCOPES**
- Search for **Google Docs API** and enable **.../auth/documents.readonly** scope
- Click **UPDATE**
- Click **SAVE AND CONTINUE**
- Click **+ ADD USERS** and add test users
- Go to the **Credentials** from the left-hand menu and click **+ CREATE CREDENTIALS** and select **OAuth client ID**
- Select **Desktop app** as the Application type
- Click **CREATE**
- Click **Download JSON** and save the JSON file as **credentials.json**
- Create a new document at https://docs.google.com
- The Google Docs file ID can be found in the URL `https://docs.google.com/document/d/xxxxxxx/edit` where xxxxxxx is the file ID
  
## Setup and installation

- Setup Redis server - https://developer.redis.com/create/
- Install Python > 3.7 - https://www.python.org/downloads/
- OpenAI API key - https://platform.openai.com/account/api-keys
- Install Node.js - https://nodejs.org/en
- Create a .env file inside /custom-gpt-nestjs and set a value for **REDIS_HOST**
- Create a .env file inside /custom-gpt-python and set a value for **REDIS_HOST**, **OPENAI_API_KEY**, **GDOCS_FILE_ID**
- Place the **credentials.json** file inside /chatgpt-project/custom-gpt-python
- Download and install Python packages
```bash
pip install openai
pip install llama-index
pip install google-auth-oauthlib
```
- Install dependencies and start NestJS server
```bash
cd custom-gpt-nestjs
npm install
npm run start
```
- Start Python script
```bash
cd custom-gpt-python
python main.py
```
- Install dependencies for frontend
```bash
cd frontend
yarn install
```

### Running in Docker

- Download Docker - https://www.docker.com/
```bash
cd chat-gpt-project
docker compose up --build
```

## Running the Frontend
`http://localhost:3000`

## Example request
`http://localhost:3001?query=Who is Hector?`

Response:
```json
{
    "channel": "request-channel:e08cbbb1-2408-4c01-90b1-b8cdd66350ae",
    "query": "Who is Hector?",
    "response": "Hector is a bee who is talking to another bee. He is trying to find out where the other bee is getting the sweet stuff from."
}
```