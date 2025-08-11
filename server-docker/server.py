# server.py
from fastmcp import FastMCP
from dotenv import load_dotenv
import subprocess
import os
mcp = FastMCP("Demo 🚀")

@mcp.tool
def hello(name: str) -> str:
    return f"Hello, {name}!"

@mcp.tool()
def authenticate():
    load_dotenv()  # <-- This reads your .env file
    NLW_TOKEN = os.getenv("NLW_TOKEN")
    print("Authenticating with NeoLoad Web...")
    subprocess.run(["neoload", "login", NLW_TOKEN], check=True)
    return "Authentication successful."

@mcp.tool()
def export_user_path(transaction_name: str, user_path: str):
    output_filename = f"{transaction_name}_{user_path}.csv"  
    print("Exporting the results to CSV...")
    result = subprocess.run(
    f'neoload report --template builtin:transactions-csv --filter "elements={user_path}" "{transaction_name}"',
    shell=True,
    stdout=subprocess.PIPE,
    text=True,
    check=True
    )
    print("MCP Tool: Report command executed successfully.")
    
    with open(output_filename, 'w', newline='') as f:
            f.write(result.stdout)            
    file_path = os.path.abspath(output_filename)
    return f"Successfully exported results to {file_path}. The file contains {len(result.stdout.splitlines())} lines."

@mcp.tool()
def read_exported_csv(REPORT_FILE:str) -> str:
    if os.path.exists(REPORT_FILE):
        with open(REPORT_FILE, "r") as f:
            return f.read()
    return "Report file not found. Please run 'export_userpath_csv' first."

if __name__ == "__main__":
   mcp.run(transport="http", host="0.0.0.0", port=8000, path="/mcp")