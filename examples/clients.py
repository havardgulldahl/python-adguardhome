# pylint: disable=W0621
"""Asynchronous Python client for the AdGuard Home API."""

import asyncio

from adguardhome import AdGuardHome


async def main():
    """Show example clients controlling from your AdGuard Home instance."""
    async with AdGuardHome("192.168.1.2") as adguard:
        version = await adguard.version()
        print("AdGuard version:", version)

        result = await adguard.clients.status()
        print("Total number of active rules:", result)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
