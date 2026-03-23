# MCP Server Deployment

This is an MCP (Model Context Protocol) server that can be installed and deployed.

## Installation

To install this MCP server in Claude Desktop, add the following configuration to your `claude_desktop_config.json`:

```json
"gitmcpadd": {
  "command": "/Users/pankaj/.local/bin/uvx",
  "args": [
    "--from",
    "git+https://github.com/cheerspankaj/mcpserver-deployment.git",
    "mcp-server"
  ]
}
```

## Usage

Once installed, you can use the MCP server through Claude Desktop.

## Development

To run the server locally:

```bash
uv run mcp-server
```

## Dependencies

- Python 3.13+
- mcp[cli]>=1.26.0