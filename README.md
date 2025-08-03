# MCP Finviz Server

A Model Context Protocol (MCP) server that provides access to FinViz financial data through a secure, sandboxed execution environment. This server allows you to query stock, forex, and crypto market data using the finvizfinance Python SDK.

## Features

### 🔍 Financial Data Analysis
- **Stock Analysis**: Get fundamental and technical data for stocks
- **Forex Data**: Access foreign exchange market information
- **Crypto Analysis**: Retrieve cryptocurrency market data
- **S&P 500 Tracking**: Built-in S&P 500 ranking tracker with historical analysis

### 🛡️ Security Features
- **Sandboxed Execution**: Code runs in a secure environment with restricted imports
- **Controlled Access**: Only allows specific modules (finvizfinance, operator, json, datetime, etc.)
- **Error Handling**: Comprehensive error reporting and validation

### 📊 Data Capabilities
- Market capitalization data
- Price and performance metrics
- Fundamental ratios (P/E, ROE, etc.)
- Sector and industry classifications
- Historical performance data
- Ranking and comparison tools

## Tools

### `analyse-stocks-forex-crypto-fundamentals-technicals`

Execute Python code using the finvizfinance SDK to analyze financial instruments.

**Parameters:**
- `code_snippet` (string, required): Python code that uses finvizfinance SDK. Must assign results to a variable named `result`.

**Example Usage:**
```python
# Get stock fundamentals
stock = finvizfinance('AAPL')
fundamentals = stock.ticker_fundament()
result = fundamentals

# Screen stocks by criteria
screener = Overview()
screener.set_filter(sector='Technology')
result = screener.screener_view()

# Get forex data
forex = finvizfinance('EURUSD')
result = forex.ticker_fundament()
```

## Installation & Setup

### Option 1: Docker (Recommended)

1. **Build the Docker image:**
```bash
docker build -t mcp-finviz:latest .
```

2. **Configure your MCP client** (e.g., Claude Desktop):

```json
{
    "mcpServers": {
        "finviz-finance": {
            "command": "docker",
            "args": [
                "run",
                "--rm",
                "-i",
                "mcp-finviz:latest"
            ]
        }
    }
}
```

### Option 2: Local Development

1. **Install dependencies:**
```bash
pip install finvizfinance mcp pydantic pytz syntropaibox
```

2. **Install the package:**
```bash
pip install -e .
```

3. **Configure for local development:**
```json
{
    "mcpServers": {
        "finviz-finance": {
            "command": "python",
            "args": ["-m", "mcp_finviz"]
        }
    }
}
```

## Usage Examples

### Stock Analysis
```python
# Get Apple stock fundamentals
stock = finvizfinance('AAPL')
fundamentals = stock.ticker_fundament()
result = {
    'company': fundamentals.get('Company'),
    'price': fundamentals.get('Price'),
    'market_cap': fundamentals.get('Market Cap'),
    'pe_ratio': fundamentals.get('P/E'),
    'sector': fundamentals.get('Sector')
}
```

### Stock Screening
```python
# Find technology stocks with P/E < 20
screener = Overview()
screener.set_filter(sector='Technology', pe='Under 20')
result = screener.screener_view()
```

### Forex Analysis
```python
# Get EUR/USD data
forex = finvizfinance('EURUSD')
forex_data = forex.ticker_fundament()
result = forex_data
```

### S&P 500 Ranking Analysis
The server includes a built-in S&P 500 ranking tracker that can:
- Track market cap changes over time
- Analyze ranking movements
- Generate reports on biggest movers
- Export results to CSV

## Security

The server implements several security measures:

- **Restricted Imports**: Only allows specific modules and packages
- **Sandboxed Execution**: Code runs in a controlled environment
- **Input Validation**: All code is parsed and validated before execution
- **Error Isolation**: Errors are caught and reported without exposing system details

### Allowed Modules
- `finvizfinance` - Main financial data SDK
- `operator` - For data operations
- `json` - For data serialization
- `datetime`, `pytz`, `dateutil` - For date/time operations
- `re`, `time`, `sys` - For basic operations
- `base64`, `pydantic` - For data handling

## Development

### Project Structure
```
mcp_finviz/
├── src/mcp_finviz/
│   ├── __init__.py          # Package initialization
│   ├── __main__.py          # Entry point
│   ├── server.py            # MCP server implementation
│   ├── finviz_analysis.py   # S&P 500 tracking functionality
│   └── sandbox.py           # Security sandbox (if needed)
├── Dockerfile               # Docker configuration
├── pyproject.toml           # Project configuration
└── README.md               # This file
```

### Building and Publishing

1. **Update dependencies:**
```bash
pip install build twine
```

2. **Build package:**
```bash
python -m build
```

3. **Publish to PyPI:**
```bash
python -m twine upload dist/*
```

### Debugging

Use the MCP Inspector for debugging:

```bash
npx @modelcontextprotocol/inspector python -m mcp_finviz
```

## Configuration Files

### Claude Desktop Configuration

**macOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`
**Windows:** `%APPDATA%/Claude/claude_desktop_config.json`

### Example Configurations

**Docker (Production):**
```json
{
    "mcpServers": {
        "finviz-finance": {
            "command": "docker",
            "args": [
                "run",
                "--rm",
                "-i",
                "mcp-finviz:latest"
            ]
        }
    }
}
```

**Local Development:**
```json
{
    "mcpServers": {
        "finviz-finance": {
            "command": "python",
            "args": ["-m", "mcp_finviz"]
        }
    }
}
```

## Error Handling

The server provides detailed error messages for:
- Syntax errors in code snippets
- Unauthorized module imports
- Missing result assignments
- Network or API errors
- Invalid data formats

## Rate Limiting

The finvizfinance SDK has built-in rate limiting. The server respects these limits and provides appropriate delays between requests to avoid being blocked.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For issues and questions:
- Check the error messages for debugging information
- Review the allowed modules list
- Ensure your code assigns results to the `result` variable
- Verify your MCP client configuration

## Changelog

### v0.1.0
- Initial release
- Basic finvizfinance integration
- S&P 500 tracking functionality
- Docker support
- Security sandbox implementation