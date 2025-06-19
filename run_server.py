#!/usr/bin/env python3
# filepath: /home/wroscoe/code/myfastmcp/run_server.py
"""
Entry point for running the FastMCP server.
"""
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

from fastmcp import FastMCP, Client
import asyncio


mcp = FastMCP(name="mcp")


async def list_tools():
    """
    List all tools available in the MCP server.
    """

    client_in_memory = Client(mcp)
    async with client_in_memory:
        tools = await client_in_memory.list_tools()

    tool_names = [t.name for t in tools]
    print(f"Available tools: {', '.join(tool_names)}")

    print(tools)

if __name__ == "__main__":

    import os
    
    #WARNING: the next version of fastmcp will make prefix's a keyword argument
    from server.math_mcp import mcp as math_mcp_server
    mcp.mount('math', math_mcp_server)

    from server.claude_mcp import mcp as claude_mcp_server
    # Ensure the server is mounted with the correct name
    mcp.mount('claude', claude_mcp_server)

    
    asyncio.run(list_tools())

    # Use 0.0.0.0 to bind to all interfaces in Docker container
    host = "0.0.0.0" if os.getenv("DOCKER_CONTAINER") else "127.0.0.1"
    mcp.run(transport="streamable-http", host=host, port=8000, path="/mcp")
