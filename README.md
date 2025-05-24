# Bilibili API MCP Server

用于哔哩哔哩 API 的 MCP（模型上下文协议）服务器，支持多种操作，包括自动购票功能。

## 环境要求

- [uv](https://docs.astral.sh/uv/) - 一个项目管理工具，可以很方便管理依赖。

## 使用方法

1. clone 本项目

2. 使用 uv 安装依赖

```bash
uv sync
```

3. 在任意 mcp client 中配置本 Server

```json
{
  "mcpServers": {
    "bilibili": {
      "command": "uv",
      "args": [
        "--directory",
        "/your-project/path/bilibili-mcp-server",
        "run",
        "bilibili.py"
      ],
    }
  }
}
```

4. 在 client 中使用

## 支持的操作

目前仅支持搜索视频，未来预计添加更多操作。

## 自动购票功能

除了基本的 MCP 服务器功能外，本项目还提供了自动购票工具。

### 配置购票功能

1. 创建 `.env` 文件并设置凭据：

```env
TICKET_USERNAME=你的用户名
TICKET_PASSWORD=你的密码
```

2. 安装额外依赖：

```bash
uv sync
```

### 使用购票功能

可以通过 Python API 使用：

```python
from src.ticket_bot import TicketBot

# 创建机器人实例
bot = TicketBot()

# 登录
bot.login()

try:
    # 搜索票务
    tickets = bot.search_ticket("演唱会名称")
    
    # 购买票务
    if tickets:
        bot.buy_ticket(tickets[0])
finally:
    # 关闭浏览器
    bot.close()
```

### 注意事项

- 请确保已安装最新版本的 Chrome 浏览器
- 使用前请正确配置环境变量
- 建议在使用前先测试登录功能

## 如何为本项目做贡献

1. Fork 本项目
2. 新建分支，并在新的分支上做改动
3. 提交 PR

## License

MIT
