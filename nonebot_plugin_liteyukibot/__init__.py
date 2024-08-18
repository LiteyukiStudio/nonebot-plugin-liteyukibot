# -*- coding: utf-8 -*-
"""
入口文件
"""
import threading

from liteyuki import LiteyukiBot
from liteyuki.config import load_config_in_default
from nonebot import get_driver

from .manager import process_manager

driver = get_driver()


@driver.on_startup
async def _():
    bot = LiteyukiBot(**load_config_in_default(no_waring=True))
    threading.Thread(target=bot.run).start()
