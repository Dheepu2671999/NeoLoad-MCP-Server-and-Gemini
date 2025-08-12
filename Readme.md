# NeoLoad + Gemini integrated MCP client-server framework

## Prerequisites

Need to make sure you have access to the Neoload Saas account using the api key generated
from the application

Have nodejs, gemini cli[also install the extension in the vs code] , VS code installed in the system

## Setup

1. Create a new Project directory and navigate to them 
```bash 
mkdir your_project_directory
cd your_project_directory
```
2. Create the python enviorment
``` bash
python -m venv .venv
```
3. Install all the dependencis using the requirements.txt

``` bash 
pip install -r requirements.txt
```

4. If the above step doesnt install the dependencies make sure to install them manually

``` bash
pip install neoload
pip install mcp
pip install streamlit
pip install python-dotenv
npm install -g @google/gemini-cli
pip install fastmcp
pip install pandas
```
5. In .env file place the token u recieved from the neoload saas

## Usage

1. Start the MCP server using the command
``` bash
python server.py
```
2. Start the MCP Client using the command

``` bash
streamlit run client.py
```
3. In the VS code login into the gemini extension once the authentication is done make sure to enable the agent button present in the prompt box to recogonize the MCP server

4. Type /mcp in the prompt box to check if the tools are available for us

5. Like wise in terminal as well type
``` bash
gemini 
```
To laucn the gemini make sure it displays the mcp server is active

### Note 
 - To use the gemini cli only server.py must be running. 

## Sample Prompts

- Authenticate the tool
- can u extract the details from the userpath [provide the userpath name] and transaction [provide the transaction name]
- Provide the Performance summary of the report extracted


