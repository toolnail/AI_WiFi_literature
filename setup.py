#!/usr/bin/env python3
"""
测试和设置脚本
检查依赖、配置环境变量等
"""

import subprocess
import sys
import os
from pathlib import Path

def check_python_version():
    """检查 Python 版本"""
    if sys.version_info < (3, 6):
        print(f"❌ Python 版本过低: {sys.version_info.major}.{sys.version_info.minor}")
        print("需要 Python 3.6 或更高版本")
        return False
    print(f"✓ Python 版本: {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")
    return True

def check_dependencies():
    """检查依赖包"""
    required = ['feedparser', 'requests']
    missing = []
    
    for package in required:
        try:
            __import__(package)
            print(f"✓ {package} 已安装")
        except ImportError:
            print(f"❌ {package} 未安装")
            missing.append(package)
    
    if missing:
        print(f"\n📦 安装缺失的包...")
        for package in missing:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
        return True
    return True

def setup_directories():
    """创建必要的目录"""
    dirs = ['reports', 'logs']
    for dir_name in dirs:
        Path(dir_name).mkdir(exist_ok=True)
        print(f"✓ 目录 '{dir_name}/' 已创建或存在")

def setup_env_variables():
    """设置环境变量说明"""
    env_vars = {
        'GITHUB_TOKEN': '(可选) GitHub API Token，提高 API 限制',
        'SMTP_PASSWORD': '(可选) 邮件通知的 SMTP 密码',
        'DINGTALK_WEBHOOK': '(可选) 钉钉机器人 webhook URL',
        'WECHAT_WEBHOOK': '(可选) 微信企业号 webhook URL',
    }
    
    print("\n📋 可配置的环境变量:")
    for var, description in env_vars.items():
        value = os.getenv(var, '未设置')
        status = '✓' if os.getenv(var) else '⚠️'
        print(f"{status} {var}: {description}")

def test_crawler():
    """测试爬虫"""
    print("\n🧪 测试爬虫...")
    try:
        result = subprocess.run([sys.executable, 'crawler.py'], capture_output=True, text=True, timeout=60)
        if result.returncode == 0:
            print("✓ 爬虫测试成功")
            # 检查是否生成了报告
            from datetime import datetime
            date_str = datetime.now().strftime('%Y-%m-%d')
            report_path = f"reports/report_{date_str}.md"
            if Path(report_path).exists():
                print(f"✓ 报告已生成: {report_path}")
                with open(report_path, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                    print(f"  （前 10 行）")
                    for line in lines[:10]:
                        print(f"  {line.rstrip()}")
            return True
        else:
            print(f"❌ 爬虫测试失败:")
            print(result.stderr[:500])
            return False
    except subprocess.TimeoutExpired:
        print("⏱️ 爬虫测试超时（>60秒）")
        return False
    except Exception as e:
        print(f"❌ 测试出错: {e}")
        return False

def print_usage():
    """打印使用说明"""
    print("\n" + "="*60)
    print("📖 使用说明")
    print("="*60)
    print("""
1️⃣ 手动运行爬虫:
   python3 crawler.py

2️⃣ 设置定时任务（每天 09:00 运行）:
   
   Linux/macOS:
   $ crontab -e
   $ 0 9 * * * cd $(pwd) && python3 crawler.py
   
   Windows: 使用"任务计划程序"应用

3️⃣ 配置邮件通知:
   编辑 config.py，设置:
   - ENABLE_EMAIL = True
   - EMAIL_FROM = 'your-email@gmail.com'
   - EMAIL_TO = ['recipient@example.com']
   
   然后设置环境变量:
   export SMTP_PASSWORD='your-app-password'

4️⃣ 配置钉钉通知（中国用户）:
   编辑 config.py，设置:
   - ENABLE_DINGTALK = True
   
   然后设置环境变量:
   export DINGTALK_WEBHOOK='https://oapi.dingtalk.com/robot/send?access_token=...'

5️⃣ 推送到 GitHub 自动运行:
   git push
   GitHub Actions 将在 UTC 08:00 自动运行爬虫

📊 查看报告:
   ls -la reports/
   cat reports/report_$(date +%Y-%m-%d).md

详细信息请参考 README.md 和 CRON_SETUP.md
""")
    print("="*60)

def main():
    """主函数"""
    print("="*60)
    print("🚀 AI+WiFi 爬虫 - 初始化和测试")
    print("="*60 + "\n")
    
    steps = [
        ("检查 Python 版本", check_python_version),
        ("检查依赖", check_dependencies),
        ("创建目录", setup_directories),
        ("环境变量配置", setup_env_variables),
        # ("测试爬虫", test_crawler),  # 可选，注释掉以加快初始化
    ]
    
    for step_name, step_func in steps:
        print(f"\n📌 {step_name}...")
        try:
            if not step_func():
                print(f"⚠️  跳过后续步骤")
                break
        except Exception as e:
            print(f"❌ 出错: {e}")
    
    print_usage()

if __name__ == '__main__':
    main()
