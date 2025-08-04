import argparse
import asyncio
import json
import logging
import os
from typing import Any

from pydantic import AnyUrl

import finvizfinance
from operator import itemgetter

from mcp.server import Server, NotificationOptions
from mcp.server.models import InitializationOptions
import mcp.server.stdio
import mcp.types as types

from syntropaibox.mcp.base import BaseSession, BaseQuerier, DEFAULT_ALLOWED_MODULES

logger = logging.getLogger("mcp_finviz_server")
logging.basicConfig(level=logging.INFO)

class FinvizSession(BaseSession):
    """Placeholder session class for consistency."""
    @classmethod
    def configure_parser(cls, parser: argparse.ArgumentParser):
        # No session-specific parameters needed, but keeping the method for structure
        pass

    @classmethod
    def from_args(cls, args: argparse.Namespace) -> "FinvizSession":
        return cls()


class FinvizQuerier(BaseQuerier):
    def __init__(self):
        namespace = {
            "finvizfinance": finvizfinance
        }
        allowed_prefixes = ("")
        custom_modules = DEFAULT_ALLOWED_MODULES.union({"finvizfinance"})


        super().__init__(allowed_prefixes, custom_modules, namespace)


async def main():
    logger.info("Starting MCP Finviz server...")
    parser = argparse.ArgumentParser()
    FinvizSession.configure_parser(parser)
    args = parser.parse_args()

    _ = FinvizSession.from_args(args)
    finviz_querier = FinvizQuerier()
    server = Server("mcp_finviz")

    @server.list_resources()
    async def handle_list_resources() -> list[types.Resource]:
        return [
            types.Resource(
                uri=AnyUrl("finvizfinance://query_resources"),
                name="Finviz SDK Query",
                description="Execute code snippets using finvizfinance",
                mimeType="application/json",
            )
        ]

    @server.read_resource()
    async def handle_read_resource(uri: AnyUrl) -> str:
        if uri.scheme != "finvizfinance":
            raise ValueError(f"Unsupported URI scheme: {uri.scheme}")
        path = str(uri).replace("finvizfinance://", "")
        if path == "query_resources":
            return json.dumps({"message": "Use the tool analyse-stocks-forex-crypto to submit a finvizfinance SDK code snippet."})
        else:
            raise ValueError(f"Unknown resource path: {path}")

    @server.list_tools()
    async def handle_list_tools() -> list[types.Tool]:
        return [
            types.Tool(
                name="analyse-stocks-forex-crypto",
                description="Execute a code snippet using the finvizfinance SDK.",
                inputSchema=finviz_querier.build_code_snippet_schema(
                    "Python code using finvizfinance SDK. Assign the result to a variable named 'result'."
                ),
            )
        ]

    @server.call_tool()
    async def handle_call_tool(name: str, arguments: dict[str, Any] | None):
        if name == "analyse-stocks-forex-crypto":
            result = finviz_querier.run_code_tool(arguments)
            return [types.TextContent(type="text", text=result)]
        else:
            raise ValueError(f"Unknown tool: {name}")

    async with mcp.server.stdio.stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            InitializationOptions(
                server_name="mcp_finviz",
                server_version="0.1.0",
                capabilities=server.get_capabilities(
                    notification_options=NotificationOptions(),
                    experimental_capabilities={},
                ),
            ),
        )


if __name__ == "__main__":
    asyncio.run(main())
