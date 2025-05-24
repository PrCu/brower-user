"""
基于 browser-use 自动化购票工具
注意：该工具仅用于学习和研究自动化技术，请勿用于恶意抢票
"""

import os
import time
import logging
from typing import Optional
from browser_use import BrowserUse

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class TicketBot:
    def __init__(self, headless: bool = False):
        """初始化购票机器人

        Args:
            headless: 是否使用无头模式运行浏览器
        """
        self.browser = BrowserUse(headless=headless)
        self.logged_in = False
        
    def login(self, username: str, password: str) -> bool:
        """登录平台

        Args:
            username: 用户名
            password: 密码

        Returns:
            bool: 登录是否成功
        """
        try:
            self.browser.get("https://passport.damai.cn/login")
            
            # 等待登录页面加载
            self.browser.wait_element_visible("#fm-login-id")
            
            # 输入用户名和密码
            self.browser.input("#fm-login-id", username)
            self.browser.input("#fm-login-password", password)
            
            # 点击登录按钮
            self.browser.wait_click(".fm-button")
            
            # 等待登录成功
            time.sleep(3)  # 等待登录跳转
            
            if "login" not in self.browser.current_url:
                self.logged_in = True
                logger.info("登录成功")
                return True
                
            logger.error("登录失败")
            return False
            
        except Exception as e:
            logger.error(f"登录过程出错: {e}")
            return False
            
    def search_ticket(self, keyword: str) -> Optional[str]:
        """搜索演出票

        Args:
            keyword: 搜索关键词

        Returns:
            Optional[str]: 演出详情页URL
        """
        try:
            self.browser.get("https://search.damai.cn/search.html")
            
            # 输入搜索关键词
            self.browser.input("#searchInput", keyword)
            self.browser.wait_click(".search-btn")
            
            # 等待搜索结果
            self.browser.wait_element_visible(".item-name")
            
            # 获取第一个结果链接
            item_link = self.browser.find_element(".item-name").get_attribute("href")
            
            if item_link:
                logger.info(f"找到演出: {item_link}")
                return item_link
                
            logger.warning("未找到相关演出")
            return None
            
        except Exception as e:
            logger.error(f"搜索过程出错: {e}")
            return None

    def buy_ticket(self, url: str) -> bool:
        """购买演出票

        Args:
            url: 演出详情页URL

        Returns:
            bool: 购买是否成功
        """
        try:
            if not self.logged_in:
                logger.error("请先登录")
                return False
                
            self.browser.get(url)
            
            # 等待页面加载
            self.browser.wait_element_visible(".perform__order__select")
            
            # 选择场次（默认第一个可选场次）
            available_sessions = self.browser.find_elements(
                ".perform__order__select .select_right_list .select_right_list_item:not(.presell):not(.no_ticket)"
            )
            if not available_sessions:
                logger.error("无可选场次")
                return False
            
            available_sessions[0].click()
            logger.info("选择场次成功")
            
            # 选择票价（默认第一个可选票价）
            self.browser.wait_element_visible(".ticket_price_item")
            available_prices = self.browser.find_elements(
                ".ticket_price_item:not(.notticket)"
            )
            if not available_prices:
                logger.error("无可选票价")
                return False
                
            available_prices[0].click()
            logger.info("选择票价成功")
            
            # 点击立即购买
            self.browser.wait_click("#buy")
            logger.info("点击购买按钮")
            
            # 确认订单
            self.browser.wait_click("#confirm")
            logger.info("确认订单")
            
            # 提交订单
            self.browser.wait_click("#submit")
            logger.info("提交订单")
            
            return True
            
        except Exception as e:
            logger.error(f"购票过程出错: {e}")
            return False
            
    def close(self):
        """关闭浏览器"""
        self.browser.close()
