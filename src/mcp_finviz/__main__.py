import asyncio
import logging
from . import server

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("mcp_finviz")

def main():
    logger.info("Starting MCP Finviz server...")
    asyncio.run(server.main())
    logger.info("MCP Finviz server stopped.")

if __name__ == "__main__":
    main()
