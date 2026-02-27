#!/usr/bin/env python3
"""
集成微信企业号通知的爬虫示例
这是一个完整的示例，展示如何在 crawler.py 中添加微信通知
"""

def example_add_to_crawler():
    """
    在 crawler.py 的 main() 函数末尾添加以下代码：
    """
    
    code = '''
# 在 crawler.py 中的 main() 函数末尾添加以下代码

from config import config
from notifier import NotificationManager

    # 爬虫代码...
    crawler = WiFiAICrawler()
    keywords = [...]
    crawler.search_arxiv(keywords)
    crawler.search_github(keywords)
    report_path = crawler.save_report()
    
    # 发送微信企业号通知
    if config.ENABLE_WECHAT:
        print("\\n📱 发送微信企业号通知...")
        notifier = NotificationManager(config)
        
        # 方式一：使用 Markdown 格式（推荐，展示效果更好）
        markdown_summary = notifier.generate_markdown_summary(crawler.results)
        notifier.send_wechat(
            "🤖 AI+WiFi 研究文献日报",
            markdown_summary,
            message_type="markdown"
        )
        
        # 方式二：使用纯文本格式
        # text_summary = notifier.generate_summary(crawler.results)
        # notifier.send_wechat("AI+WiFi 文献爬虫", text_summary)
    
    print(f"\\n✅ 爬虫运行完成！")
    print(f"📊 报告已保存到: {report_path}")
'''
    return code

def full_example_crawler():
    """完整的爬虫主函数示例"""
    
    example = '''#!/usr/bin/env python3
"""完整的爬虫示例 - 包含微信通知"""

from crawler import WiFiAICrawler
from config import config
from notifier import NotificationManager
from datetime import datetime

def main():
    """主爬虫函数，包含微信通知"""
    
    print("=" * 60)
    print("🚀 AI+WiFi 研究文献爬虫（带微信通知）")
    print("=" * 60)
    print()
    
    # 创建爬虫实例
    crawler = WiFiAICrawler()
    
    # 定义搜索关键词
    keywords = [
        'WiFi CSI channel state information',
        'WiFi sensing',
        'wireless sensing',
        'WiFi localization',
        'CSI sensing',
        'device-free sensing',
    ]
    
    # 爬取数据
    print("开始爬取数据...")
    crawler.search_arxiv(keywords, max_results=100)
    crawler.search_github(keywords[:2], max_results=30)
    
    # 生成报告
    report_path = crawler.save_report()
    
    print()
    print(f"📊 统计结果:")
    print(f"  - 环境感知与重建: {len(crawler.results['env_sensing'])}")
    print(f"  - 其他AI+WiFi: {len(crawler.results['general'])}")
    
    # 发送微信企业号通知
    if config.ENABLE_WECHAT:
        print()
        print("📱 正在发送微信企业号通知...")
        notifier = NotificationManager(config)
        
        # 使用 Markdown 格式显示（推荐）
        markdown_summary = notifier.generate_markdown_summary(crawler.results)
        success = notifier.send_wechat(
            "🤖 AI+WiFi 研究文献日报",
            markdown_summary,
            message_type="markdown"
        )
        
        if success:
            print("✅ 微信通知已发送")
        else:
            print("⚠️  微信通知发送失败（请检查配置）")
    
    # 发送其他通知（如邮件）
    if config.ENABLE_EMAIL:
        # 邮件通知代码...
        pass
    
    if config.ENABLE_DINGTALK:
        # 钉钉通知代码...
        pass
    
    print()
    print(f"✅ 爬虫运行完成！")
    print(f"📋 报告位置: {report_path}")
    print()

if __name__ == '__main__':
    main()
'''
    return example

def step_by_step_guide():
    """分步骤的集成指南"""
    
    guide = """
╔═══════════════════════════════════════════════════════════════════╗
║        在爬虫中集成微信企业号通知 - 分步骤指南                    ║
╚═══════════════════════════════════════════════════════════════════╝

📋 准备工作（5 分钟）
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. 配置微信企业号：
   运行：python3 wechat_setup.py
   按照指南完成配置

2. 设置环境变量：
   export WECHAT_WEBHOOK="https://qyapi.weixin.qq.com/..."

3. 测试配置：
   python3 wechat_setup.py test


🔧 修改 config.py（1 分钟）
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

在 config.py 中启用微信通知：

    ENABLE_WECHAT: bool = True
    # WECHAT_WEBHOOK 会自动从环境变量读取


🛠️  修改 crawler.py（2 分钟）
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

在 crawler.py 的 main() 函数中，添加 import：

    from config import config
    from notifier import NotificationManager

在 main() 函数末尾添加：

    # 发送微信企业号通知
    if config.ENABLE_WECHAT:
        notifier = NotificationManager(config)
        markdown_summary = notifier.generate_markdown_summary(crawler.results)
        notifier.send_wechat(
            "🤖 AI+WiFi 研究文献日报",
            markdown_summary,
            message_type="markdown"
        )


🚀 运行和测试（1 分钟）
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

运行爬虫：
    python3 crawler.py

检查输出是否包含：
    ✓ 微信通知已发送 (格式: markdown)

在微信企业号中查看消息。


💡 自定义消息（可选）
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

编辑 notifier.py 中的 generate_markdown_summary() 函数
修改消息格式、显示的论文数量等。

常用 Markdown 格式：
    # 标题一级  
    ## 标题二级
    **粗体**
    > 引用块
    - 列表项
    [链接文本](URL)
    `代码`


📱 在多个地方发送（可选）
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

同时启用多个通知方式：

    # 微信企业号
    if config.ENABLE_WECHAT:
        notifier.send_wechat(...)
    
    # 钉钉
    if config.ENABLE_DINGTALK:
        notifier.send_dingtalk(...)
    
    # 邮件
    if config.ENABLE_EMAIL:
        notifier.send_email(...)


🔄 与 GitHub Actions 集成
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. 在 GitHub 仓库 Settings → Secrets 中添加：
   Secret 名称：WECHAT_WEBHOOK
   值：https://qyapi.weixin.qq.com/...

2. 修改 .github/workflows/daily-crawler.yml：
   
   jobs:
     crawl:
       runs-on: ubuntu-latest
       env:
         WECHAT_WEBHOOK: ${{ secrets.WECHAT_WEBHOOK }}
       steps:
         - uses: actions/checkout@v3
         - uses: actions/setup-python@v4
           with:
             python-version: '3.11'
         - run: pip install -r requirements.txt
         - run: python3 crawler.py

3. 推送到 GitHub，每天自动运行并发送微信通知！


📌 消息示例
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

微信会显示类似这样的消息：

    🤖 AI+WiFi 研究文献日报
    
    ## 🤖 AI+WiFi 文献日报
    **2024年02月27日 06:01:24**
    
    ### 📊 统计
    - 环境感知与重建: 2 篇 ⭐
    - 其他 AI+WiFi: 100 篇
    
    ### 🎯 环境感知与重建（重点关注）
    
    1. Latent Gaussian Splatting for 4D...
    > 🔗 [2602.23172v1](https://arxiv.org/abs/...)
    > 👥 Maximilian Luz, Rohit Mohan
    
    ...


🐞 故障排查
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

问题：收不到消息
✓ 检查 WECHAT_WEBHOOK 是否正确设置
✓ 运行 python3 wechat_setup.py test
✓ 检查网络连接
✓ 查看爬虫输出日志

问题：消息格式不对
✓ 检查是否使用了 message_type="markdown"
✓ 查看 Markdown 语法是否正确
✓ 试试用纯文本格式

问题：导入错误
✓ 确保 config.py 和 notifier.py 在同一目录
✓ 检查 import 语句是否正确
✓ 运行 python3 setup.py（检查依赖）


📚 完整示例文件
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

参考本文件中的"完整爬虫示例"部分


💬 需要帮助？
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

联系方式：
- 查看 README.md
- 查看 NOTIFICATION_SETUP.md
- 运行 python3 wechat_setup.py

╔═══════════════════════════════════════════════════════════════════╗
║                   祝您配置成功！🎉                                ║
╚═══════════════════════════════════════════════════════════════════╝
"""
    return guide

def main():
    """主函数"""
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == 'example':
        print("="*70)
        print("完整爬虫示例（包含微信通知）")
        print("="*70)
        print(full_example_crawler())
    else:
        print(step_by_step_guide())

if __name__ == '__main__':
    main()
