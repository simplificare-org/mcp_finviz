# Finviz MCP Server - SyntropAI Ecosystem

**Part of the [SyntropAI MCP Ecosystem](https://github.com/paihari/documentation-syntropai)** - A unified multi-cloud abstraction framework.

This MCP (Model Context Protocol) server provides secure access to financial market data through the innovative SyntropAI abstraction layer. Built on the same security-first architecture as our cloud providers, this server demonstrates the ecosystem's versatility beyond cloud services.

## 🚀 Key Features

- **Universal Financial Data Access**: Stocks, forex, and cryptocurrency analysis
- **Secure Code Execution**: AST-based validation and sandboxed execution environment
- **Unified Abstraction Pattern**: Built on SyntropAI's provider-agnostic design
- **Real-Time Market Data**: Live financial metrics and historical analysis
- **Docker Containerization**: Production-ready deployment

## 🏗️ Architecture

This server implements the SyntropAI abstraction pattern:

```
Claude Desktop → MCP Protocol → Finviz MCP Server → SyntropAIBox → finvizfinance → Market Data
```

### Core Components:
- **FinvizSession**: Unified session management using `BaseSession`
- **FinvizQuerier**: Secure query execution extending `BaseQuerier`
- **AST Sandbox**: Safe code execution with timeout protection
- **Dynamic Schema**: Runtime API documentation generation

## 📋 Prerequisites

- Python 3.10 or higher
- Internet connection for market data access
- Docker (recommended)
- [SyntropAIBox](https://test.pypi.org/project/syntropaibox/) core library

## 🐳 Docker Installation (Recommended)

### Build and Run
```bash
# Build the image
docker build -t mcp-finviz .

# Run the container
docker run -i --rm mcp-finviz:latest
```

## ⚙️ Claude Desktop Integration

Add to your `claude_config.json`:

```json
{
  "mcpServers": {
    "finviz-finance": {
      "command": "docker",
      "args": [
        "run", "--rm", "-i",
        "mcp-finviz:latest"
      ]
    }
  }
}
```

## 🛡️ Security Features

### AST-Based Validation
- Prevents malicious code injection
- Whitelisted imports and functions
- Controlled execution environment

### Safe Execution
- Timeout protection (2-second default)
- Isolated namespace
- JSON-serialized responses

### Example Safe Query
```python
# User provides this code snippet:
from finvizfinance import stock
aapl = stock('AAPL')
result = aapl.ticker_fundament()
```

The system:
1. ✅ Validates AST syntax
2. ✅ Checks allowed imports (`finvizfinance` approved)
3. ✅ Executes in sandbox with timeout
4. ✅ Returns JSON-serialized results

## 🔧 Usage Examples

### Stock Analysis
```python
# Get Apple stock fundamentals
from finvizfinance import stock
aapl = stock('AAPL')
fundamentals = aapl.ticker_fundament()
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
from finvizfinance import overview
screener = overview.Overview()
screener.set_filter(sector='Technology', pe='Under 20')
result = screener.screener_view()
```

### Forex Analysis
```python
# Get EUR/USD data
from finvizfinance import forex
eurusd = forex.Forex('EURUSD')
result = eurusd.ticker_fundament()
```

### Cryptocurrency Analysis
```python
# Get Bitcoin data
from finvizfinance import crypto
btc = crypto.Crypto('BTCUSD')
result = btc.ticker_fundament()
```

### Sector Performance
```python
# Analyze sector performance
from finvizfinance import group
sectors = group.Group()
sectors.set_filter(group='Sector')
result = sectors.screener_view()
```

## 🌟 SyntropAI Ecosystem Benefits

### Unified Architecture
- Same security patterns as cloud providers
- Consistent authentication and error handling
- Provider-agnostic abstractions

### Non-Hardcoded Data Sources
- Supports **any** finvizfinance feature automatically
- No data source limitations
- Future features work immediately

### Enterprise Ready
- Security-first design
- Docker containerization
- Comprehensive logging

## 📊 Financial Data Coverage

### Stock Market Data
- **Fundamentals**: P/E ratios, market cap, revenue, earnings
- **Technicals**: Price, volume, moving averages, RSI
- **Company Info**: Sector, industry, description, executives
- **Financial Statements**: Income, balance sheet, cash flow

### Screening Capabilities
- **Valuation**: P/E, P/B, PEG, EV/EBITDA
- **Performance**: Price change, volume, volatility
- **Financial Health**: Debt/Equity, ROE, ROI, margins
- **Growth**: Revenue growth, earnings growth, analyst estimates

### Market Sectors
- Technology, Healthcare, Financial, Energy
- Consumer Cyclical, Utilities, Industrials
- Real Estate, Materials, Communication Services
- Consumer Defensive, Basic Materials

### International Markets
- Major world indices
- International stock screening
- Currency pair analysis
- Global sector performance

## 🔗 Related Projects

- **[Main Documentation](https://github.com/paihari/documentation-syntropai)**: Complete ecosystem overview and architecture
- **[SyntropAIBox Core](https://test.pypi.org/project/syntropaibox/)**: Shared abstraction library
- **[AWS MCP Server](../mcp-server-for-aws)**: AWS implementation
- **[Azure MCP Server](../mcp-server-azure)**: Azure implementation
- **[OCI MCP Server](../mcp-server-oci)**: Oracle Cloud implementation

## 🏆 Technical Highlights

This implementation showcases:
- **Cross-Domain Abstraction**: Same patterns work for financial data as cloud services
- **Security Engineering**: AST validation prevents financial data manipulation
- **Extensible Architecture**: Easy integration of new financial data sources
- **Production Deployment**: Containerized, scalable financial analysis

## 📞 Support

For questions about the SyntropAI MCP ecosystem:
- **Documentation**: [SyntropAI Documentation Project](https://github.com/paihari/documentation-syntropai)
- **Author**: Hari Bantwal (hpai.bantwal@gmail.com)

## 🔄 Manual Installation (Development)

```bash
# Clone repository
git clone <repository-url>
cd mcp_finviz

# Install dependencies
pip install -e .

# Install additional dependencies
pip install finvizfinance syntropaibox

# Run server
python -m mcp_finviz
```

## 🔍 Advanced Financial Analysis

### Portfolio Analysis
```python
# Analyze multiple stocks
tickers = ['AAPL', 'GOOGL', 'MSFT', 'AMZN']
portfolio_data = {}
for ticker in tickers:
    stock_obj = stock(ticker)
    portfolio_data[ticker] = stock_obj.ticker_fundament()
result = portfolio_data
```

### Market Trends
```python
# Get market overview
from finvizfinance import overview
market = overview.Overview()
market.set_filter(marketcap='+Large')
result = market.screener_view()
```

### Risk Analysis
```python
# Analyze high-volatility stocks  
from finvizfinance import screener
risk_screener = screener.Screener()
risk_screener.set_filter(volatility='High')
result = risk_screener.screener_view()
```

## 🛡️ Security Considerations for Financial Data

### Data Integrity
- All market data is validated before processing
- Financial calculations are performed in isolated environment
- Results are sanitized to prevent data corruption

### Access Control
- Only approved financial analysis functions allowed
- No system-level operations permitted
- Read-only access to market data

### Compliance
- Respects finviz.com rate limits and terms of service
- No unauthorized data scraping or manipulation
- Proper attribution of data sources

## 🌐 Demonstration of Ecosystem Versatility

This financial data server proves the SyntropAI abstraction can extend beyond cloud providers to any API or service, showcasing:

- **Universal Applicability**: Same security patterns work for any data source
- **Consistent User Experience**: Familiar patterns across cloud and financial services
- **Extensible Foundation**: Easy to add new financial data providers
- **Production Scalability**: Enterprise-ready financial analysis capabilities

---

*This server demonstrates how the SyntropAI MCP ecosystem extends beyond cloud services to provide secure, unified access to any external API or data source through innovative architectural patterns.*