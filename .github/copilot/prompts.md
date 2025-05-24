# 项目上下文提示

这是一个基于 browser-use 的自动化项目，主要用于处理浏览器自动化任务。项目具有以下特点：

1. 使用 uv 作为 Python 包管理器
2. 基于 browser-use 和 selenium 进行浏览器自动化
3. 项目环境要求：
   - Python >= 3.12
   - browser-use >= 0.0.5
   - selenium >= 4.15.2

## 编码规范

1. 所有自动化操作都应该包含适当的错误处理和重试机制
2. 使用 browser-use 的内置等待机制，避免使用硬编码的 sleep
3. 所有浏览器操作都应该有详细的日志记录
4. 代码应遵循 PEP 8 规范
5. 所有函数都应该有类型注解和文档字符串

## 常用代码片段

```python
from browser_use import BrowserUse

# 初始化浏览器实例
browser = BrowserUse()

# 等待元素出现并点击
browser.wait_click("selector")

# 错误处理示例
try:
    browser.wait_click("selector", timeout=10)
except Exception as e:
    logger.error(f"点击操作失败: {e}")
    # 进行错误恢复操作
```

## 安全注意事项

1. 不要在代码中硬编码任何敏感信息（密码、token等）
2. 所有的自动化操作都应该有超时限制
3. 确保所有的浏览器实例在使用完毕后正确关闭
4. 涉及支付操作时必须有人工确认步骤
