"""Asynchronous Python client for the AdGuard Home API."""

from typing import Optional, List

from .exceptions import AdGuardHomeError


class AdGuardHomeClients:
    """Controls AdGuard Home clients. Blocks domains."""

    def __init__(self, adguard) -> None:
        """Initialize object."""
        self._adguard = adguard

    async def _config(
        self =None
        name: str = None # example: localhost
        ids: List[str] = None # IP, CIDR or MAC address
        use_global_settings: Optional[bool] = None
        filtering_enabled: Optional[bool] = None
        parental_enabled: Optional[bool] = None
        safebrowsing_enabled: Optional[bool] = None
        safesearch_enabled: Optional[bool] = None
        use_global_blocked_services: Optional[bool] = None
        blocked_services: Optional[List[str]] = None 
        upstreams: Optional[List[str]] = None 
    ):
        """Configure client on AdGuard Home."""
        if enabled is None:
            enabled = await self.enabled()
        if interval is None:
            interval = await self.interval()
        await self._adguard._request(
            "filtering/config",
            method="POST",
            json_data={"enabled": enabled, "interval": interval},
        )


    async def status(self)-> dict:
        """Get information about configured clients."""
        response = await self._adguard._request("/clients")
        return response

'''
    async def clients_add(self, name: str, url: str) -> None:
        """Add a new filter subscription to AdGuard Home."""
        response = await self._adguard._request(
            "filtering/add_url", method="POST", json_data={"name": name, "url": url}
        )
        if not response.startswith("OK"):
            raise AdGuardHomeError(
                "Failed adding URL to AdGuard Home filter", {"response": response}
            )

    async def remove_url(self, url: str) -> None:
        """Remove a new filter subscription from AdGuard Home."""
        response = await self._adguard._request(
            "filtering/remove_url", method="POST", json_data={"url": url}
        )
        if response.rstrip() != "OK":
            raise AdGuardHomeError(
                "Failed removing URL from AdGuard Home filter", {"response": response}
            )

'''
'''
    async def enabled(self) -> bool:
        """Return if AdGuard Home filtering is enabled or not."""
        response = await self._adguard._request("filtering/status")
        return response["enabled"]

    async def enable(self) -> None:
        """Enable AdGuard Home filtering."""
        try:
            await self._config(enabled=True)
        except AdGuardHomeError as exception:
            raise AdGuardHomeError("Enabling AdGuard Home filtering failed", exception)

    async def disable(self) -> None:
        """Disable AdGuard Home filtering."""
        try:
            await self._config(enabled=False)
        except AdGuardHomeError as exception:
            raise AdGuardHomeError("Disabling AdGuard Home filtering failed", exception)

    async def interval(self, interval: Optional[int] = None) -> int:
        """Return or set the time period to keep query log data."""
        if interval:
            await self._config(interval=interval)
            return interval

        response = await self._adguard._request("filtering/status")
        return response["interval"]

    async def rules_count(self) -> int:
        """Return the number of rules loaded."""
        response = await self._adguard._request("filtering/status")
        count = -1
        for filt in response["filters"]:
            count += filt["rules_count"]
        return count

    async def add_url(self, name: str, url: str) -> None:
        """Add a new filter subscription to AdGuard Home."""
        response = await self._adguard._request(
            "filtering/add_url", method="POST", json_data={"name": name, "url": url}
        )
        if not response.startswith("OK"):
            raise AdGuardHomeError(
                "Failed adding URL to AdGuard Home filter", {"response": response}
            )

    async def remove_url(self, url: str) -> None:
        """Remove a new filter subscription from AdGuard Home."""
        response = await self._adguard._request(
            "filtering/remove_url", method="POST", json_data={"url": url}
        )
        if response.rstrip() != "OK":
            raise AdGuardHomeError(
                "Failed removing URL from AdGuard Home filter", {"response": response}
            )

    async def enable_url(self, url: str) -> None:
        """Enable a filter subscription in AdGuard Home."""
        try:
            await self._adguard._request(
                "filtering/set_url",
                method="POST",
                json_data={"url": url, "enabled": True},
            )
        except AdGuardHomeError as exception:
            raise AdGuardHomeError(
                "Failed enabling URL on AdGuard Home filter", exception
            )

    async def disable_url(self, url: str) -> None:
        """Disable a filter subscription in AdGuard Home."""
        try:
            await self._adguard._request(
                "filtering/set_url",
                method="POST",
                json_data={"url": url, "enabled": False},
            )
        except AdGuardHomeError as exception:
            raise AdGuardHomeError(
                "Failed disabling URL on AdGuard Home filter", exception
            )

    async def refresh(self, force=False) -> None:
        """Reload filtering subscriptions from URLs specified in AdGuard Home."""
        force = "true" if force else "false"
        response = await self._adguard._request(
            "filtering/refresh", method="POST", params={"force": force}
        )
        if not response.startswith("OK"):
            raise AdGuardHomeError(
                "Failed refreshing filter URLs in AdGuard Home", {"response": response}
            )
'''