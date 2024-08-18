# -*- coding: utf-8 -*-
"""
入口文件
"""
import threading

from liteyuki import LiteyukiBot, load_plugin
from liteyuki.config import load_config_in_default
from nonebot import get_driver

from .manager import process_manager

driver = get_driver()


@driver.on_startup
async def _():
    bot = LiteyukiBot(**load_config_in_default(no_waring=True))
    load_plugin("nonebot_plugin_liteyukibot.plugins.lifespan_monitor")
    load_plugin("nonebot_plugin_liteyukibot.plugins.register_service")
    threading.Thread(target=bot.run).start()
