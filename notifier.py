#!/usr/bin/env python3
"""
通知模块 - 支持邮件、钉钉、微信等多种通知方式
"""

import json
import requests
from typing import Optional, Dict, Any
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

class NotificationManager:
    """统一的通知管理器"""
    
    def __init__(self, config=None):
        self.config = config
    
    def send_email(self, subject: str, body: str, html_body: Optional[str] = None) -> bool:
        """
        发送电子邮件
        
        需要配置:
        - EMAIL_FROM: 发件人邮箱
        - EMAIL_TO: 收件人列表
        - SMTP_PASSWORD: SMTP 密码（使用应用密码而不是账户密码）
        """
        if not self.config.ENABLE_EMAIL:
            return False
        
        try:
            msg = MIMEMultipart('alternative')
            msg['Subject'] = subject
            msg['From'] = self.config.EMAIL_FROM
            msg['To'] = ', '.join(self.config.EMAIL_TO)
            
            msg.attach(MIMEText(body, 'plain', 'utf-8'))
            if html_body:
                msg.attach(MIMEText(html_body, 'html', 'utf-8'))
            
            with smtplib.SMTP(self.config.SMTP_SERVER, self.config.SMTP_PORT) as server:
                server.starttls()
                server.login(self.config.EMAIL_FROM, self.config.SMTP_PASSWORD)
                server.send_message(msg)
            
            print (f"✓ 邮件通知已发送到: {', '.join(self.config.EMAIL_TO)}")
            return True
        
        except Exception as e:
            print(f"✗ 邮件发送失败: {e}")
            return False
    
    def send_dingtalk(self, title: str, text: str, at_mobiles: Optional[list] = None) -> bool:
        """
        发送钉钉通知
        
        需要配置:
        - DINGTALK_WEBHOOK: 钉钉机器人 webhook
        - ENABLE_DINGTALK: 启用钉钉通知
        """
        if not self.config.ENABLE_DINGTALK or not self.config.DINGTALK_WEBHOOK:
            return False
        
        try:
            data = {
                "msgtype": "text",
                "text": {
                    "content": f"{title}\n\n{text}"
                }
            }
            
            if at_mobiles:
                data["text"]["mentioned_mobile_list"] = at_mobiles
            
            response = requests.post(
                self.config.DINGTALK_WEBHOOK,
                json=data,
                timeout=10
            )
            
            if response.status_code == 200:
                print("✓ 钉钉通知已发送")
                return True
            else:
                print(f"✗ 钉钉通知发送失败: {response.status_code}")
                return False
        
        except Exception as e:
            print(f"✗ 钉钉通知异常: {e}")
            return False
    
    def send_wechat(self, title: str, text: str, message_type: str = "text") -> bool:
        """
        发送微信企业号通知
        
        需要配置:
        - WECHAT_WEBHOOK: 微信企业号 webhook
        - ENABLE_WECHAT: 启用微信通知
        
        message_type: "text" (文本) 或 "markdown" (Markdown格式)
        """
        if not self.config.ENABLE_WECHAT or not self.config.WECHAT_WEBHOOK:
            return False
        
        try:
            if message_type == "markdown":
                data = {
                    "msgtype": "markdown",
                    "markdown": {
                        "content": f"# {title}\n\n{text}"
                    }
                }
            else:
                data = {
                    "msgtype": "text",
                    "text": {
                        "content": f"{title}\n\n{text}"
                    }
                }
            
            response = requests.post(
                self.config.WECHAT_WEBHOOK,
                json=data,
                timeout=10
            )
            
            if response.status_code == 200:
                result = response.json()
                if result.get('errcode') == 0:
                    print(f"✓ 微信通知已发送 (格式: {message_type})")
                    return True
                else:
                    print(f"✗ 微信通知发送失败: {result.get('errmsg')}")
                    return False
            else:
                print(f"✗ 微信通知发送失败: {response.status_code}")
                return False
        
        except Exception as e:
            print(f"✗ 微信通知异常: {e}")
            return False
    
    def generate_summary(self, results: Dict[str, Any]) -> str:
        """生成通知摘要"""
        summary = f"""
🤖 AI+WiFi 研究文献爬虫每日报告
{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

📊 统计信息:
- 环境感知与重建相关: {len(results.get('env_sensing', []))} 篇
- 其他 AI+WiFi 相关: {len(results.get('general', []))} 篇

🎯 环境感知与重建 TOP 3:
"""
        for idx, item in enumerate(results.get('env_sensing', [])[:3], 1):
            if 'arxiv_id' in item:
                summary += f"\n{idx}. {item['title'][:60]}...\n   [{item['arxiv_id']}]({item['link']})"
            elif 'owner' in item:
                summary += f"\n{idx}. {item['name']} by {item['owner']}\n   Stars: {item['stars']}"
        
        summary += "\n\n查看完整报告: reports/ 目录"
        return summary
    
    def generate_markdown_summary(self, results: Dict[str, Any]) -> str:
        """生成 Markdown 格式的摘要（用于微信）"""
        md = f"""## 🤖 AI+WiFi 文献日报
**{datetime.now().strftime('%Y年%m月%d日 %H:%M:%S')}**

### 📊 统计
- **环境感知与重建**: {len(results.get('env_sensing', []))} 篇 ⭐
- **其他 AI+WiFi**: {len(results.get('general', []))} 篇

### 🎯 环境感知与重建（重点关注）
"""
        for idx, item in enumerate(results.get('env_sensing', [])[:5], 1):
            if 'arxiv_id' in item:
                md += f"\n**{idx}. {item['title'][:80]}**\n"
                md += f"> 📄 [{item['arxiv_id']}]({item['link']})\n"
                md += f"> 👥 {', '.join(item['authors'][:2])}\n"
            elif 'owner' in item:
                md += f"\n**{idx}. {item['name']}**\n"
                md += f"> 🔗 [{item['url']}]({item['url']})\n"
                md += f"> ⭐ Stars: {item['stars']} | 👤 {item['owner']}\n"
        
        md += "\n### 📚 其他热门论文（Top 3）\n"
        for idx, item in enumerate(results.get('general', [])[:3], 1):
            if 'arxiv_id' in item:
                md += f"\n**{idx}. {item['title'][:80]}**\n"
                md += f"> [{item['arxiv_id']}]({item['link']})\n"
        
        md += f"\n---\n*[查看完整报告](https://github.com/toolnail/AI_WiFi_literature)*"
        return md


def create_html_report(results: Dict[str, Any]) -> str:
    """生成 HTML 格式的报告用于邮件"""
    html = f"""
    <html>
    <head>
        <meta charset="utf-8">
        <style>
            body {{ font-family: Arial, sans-serif; margin: 20px; }}
            .header {{ background: #4CAF50; color: white; padding: 20px; border-radius: 5px; }}
            .section {{ margin: 20px 0; }}
            .env-item {{ background: #fff3cd; padding: 10px; margin: 10px 0; border-left: 4px solid #ffb81c; }}
            .general-item {{ background: #e7f3ff; padding: 10px; margin: 10px 0; border-left: 4px solid #2196F3; }}
            a {{ color: #2196F3; text-decoration: none; }}
        </style>
    </head>
    <body>
        <div class="header">
            <h1>🤖 AI+WiFi 研究文献每日报告</h1>
            <p>{datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}</p>
        </div>
        
        <div class="section">
            <h2>📊 统计</h2>
            <p>
                🎯 环境感知与重建相关: <strong>{len(results.get('env_sensing', []))}</strong> 篇<br>
                📚 其他 AI+WiFi 相关: <strong>{len(results.get('general', []))}</strong> 篇
            </p>
        </div>
        
        <div class="section">
            <h2>🎯 环境感知与重建相关论文 (Top 10)</h2>
            {"".join([
                f'''<div class="env-item">
                    <h3>{item['title']}</h3>
                    <p><strong>作者:</strong> {', '.join(item['authors'][:3])}</p>
                    <p><strong>发表:</strong> {item['published'][:10]}</p>
                    <p>{item['summary'][:200]}...</p>
                    <p><a href="{item['link']}">查看原文 [{item['arxiv_id']}]</a></p>
                </div>'''
                for item in results.get('env_sensing', [])[:10]
            ])}
        </div>
        
        <div class="section">
            <h2>📚 其他 AI+WiFi 相关论文 (Top 5)</h2>
            {"".join([
                f'''<div class="general-item">
                    <h3>{item['title']}</h3>
                    <p><strong>作者:</strong> {', '.join(item['authors'][:3])}</p>
                    <p><strong>发表:</strong> {item['published'][:10]}</p>
                    <p>{item['summary'][:200]}...</p>
                    <p><a href="{item['link']}">查看原文 [{item['arxiv_id']}]</a></p>
                </div>'''
                for item in results.get('general', [])[:5]
            ])}
        </div>
    </body>
    </html>
    """
    return html
