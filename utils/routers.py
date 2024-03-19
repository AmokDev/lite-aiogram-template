from importlib import import_module
from aiogram import Dispatcher
from pathlib import Path
import logging

async def reg_routers(dp: Dispatcher):
    routers_count = 0
    for p in sorted((Path("handlers")).rglob("*.py")):
        mod = ".".join(p.parent.parts + (p.stem,))
        module = import_module(mod)
        dp.include_router(module.router)
        routers_count += 1
    logging.info(f"{routers_count} routers was handled!")
