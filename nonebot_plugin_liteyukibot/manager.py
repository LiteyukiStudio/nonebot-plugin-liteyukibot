# -*- coding: utf-8 -*-
"""
Copyright (C) 2020-2024 LiteyukiStudio. All Rights Reserved 

@Time    : 2024/8/18 上午11:16
@Author  : snowykami
@Email   : snowykami@outlook.com
@File    : run_in_sub_process.py
@Software: PyCharm
"""
from liteyuki.core.manager import ProcessManager
from liteyuki.bot.lifespan import Lifespan

process_manager = ProcessManager(lifespan=Lifespan())
