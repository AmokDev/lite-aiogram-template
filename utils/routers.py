from importlib import import_module
from aiogram import Dispatcher
from pathlib import Path

async def reg_routers(dp: Dispatcher):
    for p in sorted((Path("handlers")).rglob("*.py")):
        mod = ".".join(p.parent.parts + (p.stem,))
        module = import_module(mod)
        dp.include_router(module.router)
