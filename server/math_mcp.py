# server.py
from fastmcp import FastMCP

mcp = FastMCP(name="math_mcp")

@mcp.tool
def multiply(a: float, b: float) -> float:
    """Multiplies two numbers."""
    return a * b
