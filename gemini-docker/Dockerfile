FROM node:20-slim

# Install Python (for compatibility, if needed)
RUN apt-get update && apt-get install -y python3 python3-pip && rm -rf /var/lib/apt/lists/*

# Install Gemini CLI
RUN npm install -g @google/gemini-cli

# Set workdir for MCP/GEMINI.md or mounted code
WORKDIR /app

# Default: open Gemini CLI interactive terminal
ENTRYPOINT [ "gemini" ]
