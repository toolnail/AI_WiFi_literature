#!/usr/bin/env python3
"""
高级 AI+WiFi 研究文献爬虫配置
支持邮件通知、多数据源、自定义过滤
"""

import os
from dataclasses import dataclass
from typing import List

@dataclass
class CrawlerConfig:
    """爬虫配置类"""
    
    # 输出目录
    OUTPUT_DIR: str = './reports'
    
    # 环境感知和重建的关键词
    ENV_SENSING_KEYWORDS: List[str] = None
    
    # 通用搜索关键词
    SEARCH_KEYWORDS: List[str] = None
    
    # arXiv 搜索参数
    ARXIV_MAX_RESULTS: int = 100
    ARXIV_TIMEOUT: int = 10
    
    # GitHub 搜索参数
    GITHUB_MAX_RESULTS: int = 30
    GITHUB_TOKEN: str = os.getenv('GITHUB_TOKEN', '')
    
    # 邮件通知配置
    ENABLE_EMAIL: bool = False
    EMAIL_FROM: str = ''
    EMAIL_TO: List[str] = None
    SMTP_SERVER: str = 'smtp.gmail.com'
    SMTP_PORT: int = 587
    SMTP_PASSWORD: str = os.getenv('SMTP_PASSWORD', '')
    
    # 钉钉 webhook 通知（中国用户）
    ENABLE_DINGTALK: bool = False
    DINGTALK_WEBHOOK: str = os.getenv('DINGTALK_WEBHOOK', '')
    
    # 微信企业号通知
    ENABLE_WECHAT: bool = False
    WECHAT_WEBHOOK: str = os.getenv('WECHAT_WEBHOOK', '')
    
    def __post_init__(self):
        if self.ENV_SENSING_KEYWORDS is None:
            self.ENV_SENSING_KEYWORDS = [
                '环境感知', 'environmental sensing', 'environment reconstruction',
                '环境重建', 'scene reconstruction', 'scene understanding',
                '室内定位', 'indoor localization', 'indoor positioning',
                '姿态估计', 'pose estimation', 'human pose',
                '活动识别', 'activity recognition', 'gesture recognition',
                '占有地图', 'occupancy mapping', 'occupancy detection',
                '异常检测', 'anomaly detection', 'crowd sensing',
                '存在感知', 'presence detection', '人体检测', 'human detection',
                '跌倒检测', 'fall detection', '运动检测', 'motion detection',
                '手指识别', 'finger tracking', '轨迹跟踪', 'trajectory tracking',
            ]
        
        if self.SEARCH_KEYWORDS is None:
            self.SEARCH_KEYWORDS = [
                'WiFi CSI channel state information',
                'WiFi sensing',
                'wireless sensing',
                'WiFi localization',
                'CSI sensing',
                'device-free sensing',
                'WiFi gait recognition',
                'WiFi activity recognition',
            ]
        
        if self.EMAIL_TO is None:
            self.EMAIL_TO = []

# 全局配置实例
config = CrawlerConfig()
