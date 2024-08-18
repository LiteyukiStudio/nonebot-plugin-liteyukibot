<div align="center">
  <img src="https://cdn.liteyuki.icu/static/img/liteyuki_icon_640.png" width="180" height="180" alt="NoneBotPluginLogo">

</div>

<div align="center">

# nonebot-plugin-liteyukibot

_✨ 在NoneBot中使用轻雪 ✨_


<a href="./LICENSE">
    <img src="https://img.shields.io/github/license/LiteyukiStudio/nonebot-plugin-liteyukibot.svg" alt="license">
</a>
<a href="https://pypi.python.org/pypi/nonebot-plugin-liteyukibot">
    <img src="https://img.shields.io/pypi/v/nonebot-plugin-liteyukibot.svg" alt="pypi">
</a>
<img src="https://img.shields.io/badge/python-3.10+-blue.svg" alt="python">

</div>

## 📖 介绍

在NoneBot机器人中使用[轻雪机器人](https://bot.liteyuki.icu)的功能！

## 💿 安装

<details open>
<summary>使用 nb-cli 安装(推荐，需先安装`nb-cli`)</summary>
在 轻雪 项目的根目录下打开命令行, 输入以下指令即可安装

    nb plugin install nonebot-plugin-liteyukibot

</details>

<details open>
<summary>使用 pip 安装</summary>
在 轻雪 项目的根目录下打开命令行, 输入以下指令即可安装

    pip install nonebot-plugin-liteyukibot

</details>

<details>
<summary>使用包管理器安装</summary>
在 nonebot2 项目的插件目录下, 打开命令行, 根据你使用的包管理器, 输入相应的安装命令

<details>
<summary>pip</summary>

    pip install nonebot-plugin-liteyukibot

</details>
<details>
<summary>pdm</summary>

    pdm add nonebot-plugin-liteyukibot

</details>
<details>
<summary>poetry</summary>

    poetry add nonebot-plugin-liteyukibot

</details>
<details>
<summary>conda</summary>

    conda install nonebot-plugin-liteyukibot

</details>
</details>

## 🎉 使用

- 使用`nb-cli`安装的插件默认加载，无需额外配置
- 包管理器手动安装需在`pyproject.toml`中添加如下配置
- 详细用法请访问[轻雪主页](https://bot.liteyuki.icu)

```toml
plugins = ["nonebot_plugin_liteyukibot"]
```

## ⚙️ 配置

在插件运行模式下无需配置太多内容，如果需要配置，请 参考LiteyukiBot的[配置文档](https://bot.liteyuki.icu/deploy/config.html)，
在config下新建配置文件`nonebot.yml/toml/json`(你可自行命名)，填入如下结构配置文件，这里使用yaml

## ℹ️ 其他

- 目前该插件已内置在[轻雪机器人应用](https://bot.liteyuki.icu)中，无需单独安装

- 如果你是基于[轻雪框架](https://pypi.org/project/liteyukibot/)二次开发，需要手动安装

- 该插件仍然有许多内容需要完善，欢迎各位的建议及贡献
