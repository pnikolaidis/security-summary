from __future__ import annotations

import asyncio
import logging
from collections.abc import Awaitable, Callable

from src.normalize import Item

log = logging.getLogger(__name__)

CollectorFn = Callable[[dict], Awaitable[list[Item]]]


async def run_collector(name: str, fn: CollectorFn, config: dict, timeout: float = 20.0) -> list[Item]:
    try:
        async with asyncio.timeout(timeout):
            items = await fn(config)
        log.info("collector.ok source=%s count=%d", name, len(items))
        return items
    except Exception as e:
        log.warning("collector.fail source=%s error=%s", name, e)
        return []
