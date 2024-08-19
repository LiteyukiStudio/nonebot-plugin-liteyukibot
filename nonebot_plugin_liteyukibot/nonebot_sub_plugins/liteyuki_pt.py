# -*- coding: utf-8 -*-
"""
liteyuki_posts_and_telecommunications.py
轻雪信息传递插件
"""

from nonebot import Bot, get_bot, on_message
from nonebot.plugin import PluginMetadata
from nonebot.adapters.onebot.v11 import MessageEvent, Bot
from liteyuki.comm.storage import shared_memory
from liteyuki.message.event import Event as LiteyukiEvent

__plugin_meta__ = PluginMetadata(
    name="轻雪物流",
    description="把消息事件传递给轻雪框架进行处理",
    usage="用户无需使用",
)


@on_message().handle()
async def _(bot: Bot, event: MessageEvent):
    liteyuki_event = LiteyukiEvent(
        type=event.message_type,
        data=event.dict(),
        bot_id=bot.self_id,
        session_id=str(event.user_id if event.message_type == "private" else event.group_id),
        session_type=event.message_type,
        receive_channel="event_to_nonebot"
    )
    shared_memory.publish("event_to_liteyuki", liteyuki_event)


@shared_memory.on_subscriber_receive("event_to_nonebot")
async def _(event: LiteyukiEvent):
    bot: Bot = get_bot(event.bot_id)
    await bot.send_msg(message_type=event.type, user_id=int(event.session_id), group_id=int(event.session_id), message=event.data["message"])
