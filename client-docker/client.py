import streamlit as st
import asyncio
from fastmcp import Client
import pandas as pd
import io
from config import CONFIG  # same as in client.py

client = Client(CONFIG)

st.title("MCP Client Interface 🚀")
st.markdown("""
### 🧩 MCP Client Interface

This tool serves as an **MCP Client** that connects to an MCP server to perform a series of automated actions:

- 🔐 **Authenticate** with NeoLoad Web  
- 📊 **Export performance test results** from NeoLoad  
- 📁 **Read and display CSV reports** interactively

All operations are powered by **NeoLoad**, a modern performance testing platform used to validate system scalability and reliability.

Please ensure the MCP server is running and NeoLoad CLI is configured before starting.
""")


# Inputs
transaction_name = st.text_input("Transaction Name", value="SIP_GeloadTest - 31 Jan 2025")
user_path = st.text_input("User Path", value="SIP_S07_CreateSurvey_Sponsor_New")
report_file = st.text_input("Report File Name", value="temp.csv")

# On button click
if st.button("Run MCP Workflow"):
    async def run_all():
        async with client:
            # Authenticate
            auth_result = await client.call_tool("authenticate")
            st.success(f"Auth Result: {auth_result.content[0].text}")

            # Export user path
            export_result = await client.call_tool("export_user_path", {
                "transaction_name": transaction_name,
                "user_path": user_path
            })
            st.success(f"Export Result: {export_result.content[0].text}")

            read_result = await client.call_tool("read_exported_csv", {
                    "REPORT_FILE": report_file
                })

            csv_content = read_result.content[0].text

            try:
                # Convert CSV string to DataFrame
                df = pd.read_csv(io.StringIO(csv_content), delimiter=';')
                st.dataframe(df)  # You can also use st.table(df) for static table
            except Exception as e:
                st.error(f"Error parsing CSV: {e}")
                st.text_area("Raw CSV Output", value=csv_content, height=300)

    # Run the async function
    asyncio.run(run_all())
