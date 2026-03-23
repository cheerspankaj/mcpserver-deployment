#server.py

from mcp.server.fastmcp import FastMCP

#create an mco server
mcp = FastMCP("Demo")

#add an addtional tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """
    Adds two numbers together.
    """
    return a + b



