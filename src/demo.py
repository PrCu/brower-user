"""
演示使用购票机器人
"""

from ticket_bot import TicketBot
import logging
import os
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

def main():
    # 初始化日志
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    logger = logging.getLogger(__name__)
    
    # 创建票务机器人实例 (开发调试时建议 headless=False)
    bot = TicketBot(headless=False)
    
    try:
        # 从环境变量获取登录信息
        username = os.getenv("TICKET_USERNAME")
        password = os.getenv("TICKET_PASSWORD")
        
        if not username or not password:
            logger.error("请先设置环境变量 TICKET_USERNAME 和 TICKET_PASSWORD")
            return
        
        # 登录
        if not bot.login(username, password):
            logger.error("登录失败，程序退出")
            return
            
        # 搜索演出
        keyword = "周杰伦"  # 这里替换为你想搜索的演出关键词
        url = bot.search_ticket(keyword)
        
        if not url:
            logger.error("未找到相关演出，程序退出")
            return
            
        # 开始购票
        if bot.buy_ticket(url):
            logger.info("购票成功！")
        else:
            logger.error("购票失败")
            
    except Exception as e:
        logger.error(f"程序运行出错: {e}")
        
    finally:
        # 关闭浏览器
        bot.close()

if __name__ == "__main__":
    main()
