# -*- coding: utf-8 -*-
"""
入口文件
"""
import threading

from liteyuki import LiteyukiBot, load_plugin as liteyuki_load_plugin
from liteyuki.config import load_config_in_default
from nonebot import get_driver
from nonebot.plugin import PluginMetadata, load_plugin as nonebot_load_plugin

from .nonebot_sub_plugins import liteyuki_pt

from .manager import process_manager

__plugin_meta__ = PluginMetadata(
    name="LiteyukiBot(plugin)",
    description="插件化轻雪机器人",
    usage="请访问`https://bot.liteyuki.icu`",
    homepage="https://bot.liteyuki.icu",
    type="application",
)

LITEYUKI_MODULE_BASE_PATH = "nonebot_plugin_liteyukibot.liteyuki_plugins."
liteyuki_plugins = ["lifespan_monitor", "register_service", "hello_liteyuki"]

NONEBOT_SUB_MODULE_BASE_PATH = "nonebot_plugin_liteyukibot.nonebot_sub_plugins."
nonebot_sub_plugins = ["liteyuki_pt"]

driver = get_driver()


@driver.on_startup
async def _():
    bot = LiteyukiBot(**load_config_in_default(no_waring=True))
    for plg_ in liteyuki_plugins:
        liteyuki_load_plugin(LITEYUKI_MODULE_BASE_PATH + plg_)
    threading.Thread(target=bot.run).start()
