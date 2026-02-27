#!/usr/bin/env python3
"""
微信企业号配置和测试脚本
"""

import os
import sys
import requests
import json
from datetime import datetime

def setup_wechat():
    """微信企业号配置步骤指南"""
    
    guide = """
╔════════════════════════════════════════════════════════════════════════╗
║               微信企业号配置指南 - AI+WiFi 爬虫通知                      ║
╚════════════════════════════════════════════════════════════════════════╝

📱 第一步：注册企业微信账户

1. 访问官网: https://work.weixin.qq.com/
2. 点击 "立即开始" 或 "企业注册"
3. 按照步骤完成企业认证（需要营业执照或组织代码）
   - 如果是个人，也可以使用个人身份注册（会有一定限制）
   - 或者加入现有团队的企业微信

⚙️ 第二步：创建应用和获取 Webhook

在企业微信管理后台：

1. 左侧菜单 → "应用" → "创建应用"
2. 填写应用信息：
   - 应用名称: "AI研究爬虫"
   - 可见范围: 选择相关的部门或成员

3. 创建成功后，进入应用详情页，找到 "Webhook" 或 "机器人" 部分
4. 创建 Webhook，复制完整 URL：
   https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=xxxxxxxxxxxxxxxx
   
   ⚠️  这个 key 非常重要，不要泄露！

🔐 第三步：配置环境变量

=== Linux/macOS ===
在终端中运行：

export WECHAT_WEBHOOK="https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=xxxxxxxxxxxxxxxx"

或者添加到 ~/.bashrc 或 ~/.zshrc：

echo 'export WECHAT_WEBHOOK="https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=xxxxxxxxxxxxxxxx"' >> ~/.bashrc
source ~/.bashrc

=== Windows (PowerShell) ===
[System.Environment]::SetEnvironmentVariable('WECHAT_WEBHOOK', 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=xxxxxxxxxxxxxxxx', 'User')

=== Windows (Command Prompt) ===
setx WECHAT_WEBHOOK "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=xxxxxxxxxxxxxxxx"

📝 第四步：修改配置文件

编辑 config.py，启用微信通知：

    ENABLE_WECHAT: bool = True
    WECHAT_WEBHOOK: str = os.getenv('WECHAT_WEBHOOK', '')

🧪 第五步：测试通知

运行测试脚本：
    python3 wechat_setup.py test

✅ 第六步：集成到爬虫

编辑 crawler.py 的 main() 函数，在末尾添加：

    from config import config
    from notifier import NotificationManager
    
    if config.ENABLE_WECHAT:
        notifier = NotificationManager(config)
        summary = notifier.generate_summary(crawler.results)
        notifier.send_wechat(
            "🤖 AI+WiFi 日报",
            summary
        )

🚀 第七步：自动化

推送到 GitHub，在 Secrets 中添加 WECHAT_WEBHOOK：

1. 仓库 Settings → Secrets and variables → Actions
2. 新建 Secret：WECHAT_WEBHOOK
3. 修改 .github/workflows/daily-crawler.yml：

    env:
      WECHAT_WEBHOOK: ${{ secrets.WECHAT_WEBHOOK }}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📌 消息格式示例

文本消息：
{
    "msgtype": "text",
    "text": {
        "content": "这是一条文本消息"
    }
}

卡片消息（推荐展示用）：
{
    "msgtype": "news",
    "news": {
        "items": [
            {
                "title": "标题",
                "description": "描述",
                "url": "https://example.com",
                "picurl": "https://example.com/pic.jpg"
            }
        ]
    }
}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

❓ 常见问题

Q1: "没有企业微信账户怎么办？"
A: 可以用个人身份使用，功能会有限制。推荐选择：
   - 加入现有团队的企业微信
   - 注册免费的企业微信（个人版）
   - 使用微信群机器人代替

Q2: "收不到消息?"
A: 检查以下几点：
   - Webhook URL 是否正确复制
   - 是否启用了微信通知（ENABLE_WECHAT = True）
   - 网络是否正常连接
   - 查看错误日志

Q3: "如何修改消息内容?"
A: 编辑 notifier.py 中的 send_wechat() 方法或 generate_summary() 函数

Q4: "支持其他消息类型吗?"
A: 支持！包括：
   - text: 文本消息
   - markdown: Markdown 格式
   - news: 图文消息
   - image: 图片
   详见企业微信 API 文档

Q5: "可以针对特定人员发送吗?"
A: 可以！在消息中添加 touser 字段
   {
       "touser": "user1|user2",
       "msgtype": "text",
       "text": {"content": "..."}
   }

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📚 官方文档

- 企业微信官网: https://work.weixin.qq.com/
- API 文档: https://work.weixin.qq.com/api/doc
- Webhook 文档: https://work.weixin.qq.com/api/doc/90000/90135/72132

╔════════════════════════════════════════════════════════════════════════╗
║                    现在开始配置！祝您使用愉快！ 🎉                        ║
╚════════════════════════════════════════════════════════════════════════╝
"""
    print(guide)

def test_wechat():
    """测试微信企业号通知"""
    
    print("\n" + "="*70)
    print("🧪 微信企业号通知测试")
    print("="*70 + "\n")
    
    webhook = os.getenv('WECHAT_WEBHOOK', '')
    
    if not webhook:
        print("❌ 错误：未设置 WECHAT_WEBHOOK 环境变量")
        print("\n请设置环境变量：")
        print("  export WECHAT_WEBHOOK='https://...'")
        return False
    
    print(f"✓ Webhook 已配置（前30字符）: {webhook[:30]}...")
    
    # 构建测试消息
    test_message = {
        "msgtype": "text",
        "text": {
            "content": f"""🧪 测试消息
时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
来源: AI+WiFi 爬虫系统

如果收到此消息，说明微信企业号配置成功！🎉

测试内容：
- ✓ Webhook 配置正确
- ✓ 网络连接正常
- ✓ 消息发送成功

下一步：修改 config.py 启用自动通知"""
        }
    }
    
    print("\n📤 发送测试消息...")
    print(f"消息内容：{json.dumps(test_message, ensure_ascii=False, indent=2)}")
    print()
    
    try:
        response = requests.post(
            webhook,
            json=test_message,
            timeout=10
        )
        
        print(f"状态码: {response.status_code}")
        print(f"响应内容: {response.text}\n")
        
        if response.status_code == 200:
            result = response.json()
            if result.get('errcode') == 0:
                print("✅ 测试成功！消息已发送")
                print("\n现在可以在微信企业号中查看消息")
                return True
            else:
                print(f"❌ 发送失败: {result.get('errmsg', '未知错误')}")
                return False
        else:
            print(f"❌ HTTP 错误: {response.status_code}")
            return False
            
    except requests.Timeout:
        print("❌ 请求超时，检查网络连接")
        return False
    except Exception as e:
        print(f"❌ 发送出错: {e}")
        return False

def main():
    """主函数"""
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        test_wechat()
    else:
        setup_wechat()
        print("\n💡 提示：运行以下命令测试配置")
        print("   python3 wechat_setup.py test\n")

if __name__ == '__main__':
    main()
