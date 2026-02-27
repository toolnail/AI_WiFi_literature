# 通知配置指南

本指南说明如何配置各种通知方式，使爬虫完成后自动向您发送报告。

## 📧 电子邮件通知（Gmail + SMTP）

### 步骤 1: 启用 Gmail 的 SMTP

1. 访问 https://myaccount.google.com/security
2. 启用 "两步验证"
3. 生成 "应用密码"：https://myaccount.google.com/apppasswords
4. 选择"邮件"和"Windows 电脑"，Google 会生成一个 16 字符的密码

### 步骤 2: 配置环境变量

```bash
# Linux/macOS
export SMTP_PASSWORD="xxxx xxxx xxxx xxxx"

# Windows (PowerShell)
$env:SMTP_PASSWORD="xxxx xxxx xxxx xxxx"

# Windows (Command Prompt)
set SMTP_PASSWORD=xxxx xxxx xxxx xxxx
```

### 步骤 3: 修改 config.py

```python
# 在 config.py 中修改 CrawlerConfig 类
ENABLE_EMAIL: bool = True
EMAIL_FROM: str = 'your-email@gmail.com'  # 替换为您的 Gmail
EMAIL_TO: List[str] = ['recipient@example.com']  # 可以添加多个收件人
```

### 步骤 4: 修改 crawler.py

在 `crawler.py` 的 `main()` 函数最后添加：

```python
from config import config
from notifier import NotificationManager, create_html_report

# ... 爬虫代码 ...

# 发送邮件通知
if config.ENABLE_EMAIL:
    notifier = NotificationManager(config)
    subject = f"AI+WiFi 研究文献每日报告 - {datetime.now().strftime('%Y-%m-%d')}"
    html = create_html_report(crawler.results)
    notifier.send_email(subject, "", html)
```

---

## 🔔 钉钉通知（中国用户首选）

### 步骤 1: 创建钉钉机器人

1. 打开钉钉 -> 群聊 -> 群设置 -> 群机器人
2. 添加 -> 自定义机器人
3. 输入名称（如 "AI 研究爬虫"）
4. 复制 Webhook 地址

### 步骤 2: 配置环境变量

```bash
# Linux/macOS
export DINGTALK_WEBHOOK="https://oapi.dingtalk.com/robot/send?access_token=xxxxx"

# Windows (PowerShell)
$env:DINGTALK_WEBHOOK="https://oapi.dingtalk.com/robot/send?access_token=xxxxx"
```

### 步骤 3: 修改 config.py

```python
ENABLE_DINGTALK: bool = True
DINGTALK_WEBHOOK: str = os.getenv('DINGTALK_WEBHOOK', '')
```

### 步骤 4: 修改 crawler.py

在 `main()` 函数最后添加：

```python
from config import config
from notifier import NotificationManager

# ... 爬虫代码 ...

# 发送钉钉通知
if config.ENABLE_DINGTALK:
    notifier = NotificationManager(config)
    summary = notifier.generate_summary(crawler.results)
    notifier.send_dingtalk("🤖 AI+WiFi 文献爬虫", summary)
```

---

## 💬 微信企业号通知

### 步骤 1: 注册企业微信

1. 访问 https://work.weixin.qq.com/
2. 注册企业账号
3. 创建应用和机器人

### 步骤 2: 获取 Webhook

企业号后台 -> 应用 -> 选择应用 -> 复制 Webhook 地址

### 步骤 3: 配置环境变量

```bash
export WECHAT_WEBHOOK="https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=xxxxx"
```

### 步骤 4: 修改 config.py 和 crawler.py

参考钉钉通知的配置方式即可。

---

## 🔄 与 GitHub Actions 集成

如果使用 GitHub Actions 运行爬虫，需要在 GitHub 仓库中配置 Secrets：

1. 进入 Repository Settings -> Secrets and variables -> Actions
2. 新建 Secrets：
   - `SMTP_PASSWORD`: Gmail 应用密码
   - `DINGTALK_WEBHOOK`: 钉钉 Webhook
   - `WECHAT_WEBHOOK`: 微信 Webhook
   - `GITHUB_TOKEN`: GitHub API Token (可选)

### 修改 .github/workflows/daily-crawler.yml

```yaml
jobs:
  crawl:
    runs-on: ubuntu-latest
    env:
      SMTP_PASSWORD: ${{ secrets.SMTP_PASSWORD }}
      DINGTALK_WEBHOOK: ${{ secrets.DINGTALK_WEBHOOK }}
      WECHAT_WEBHOOK: ${{ secrets.WECHAT_WEBHOOK }}
    # ... 其他配置 ...
```

---

## 测试通知

### 测试邮件

```python
from config import config
from notifier import NotificationManager, create_html_report

config.ENABLE_EMAIL = True
notifier = NotificationManager(config)
notifier.send_email(
    "测试邮件 - AI+WiFi 爬虫",
    "如果收到此邮件，说明配置成功！"
)
```

### 测试钉钉

```python
from config import config
from notifier import NotificationManager

config.ENABLE_DINGTALK = True
notifier = NotificationManager(config)
notifier.send_dingtalk(
    "🧪 测试",
    "如果收到此消息，说明钉钉配置成功！"
)
```

---

## ⚠️ 常见问题

### Q: 邮件不能发送？
- 检查是否启用了 Gmail 两步验证
- 确认使用的是应用密码而非账户密码
- 检查环境变量是否正确设置
- 尝试在没有空格的情况下设置密码

### Q: 钉钉消息不显示？
- 检查 Webhook URL 是否正确复制
- 确认群机器人已启用
- 检查是否有关键词过滤设置

### Q: 如何在本地测试？
```bash
# 设置环境变量
export SMTP_PASSWORD="xxxx xxxx xxxx xxxx"
export DINGTALK_WEBHOOK="https://..."

# 运行爬虫
python3 crawler.py

# 检查 reports/ 目录中的报告
cat reports/report_$(date +%Y-%m-%d).md
```

---

## 🔐 安全建议

1. **不要在代码中硬编码密码** - 使用环境变量
2. **不要提交含有 Secrets 的文件** - 使用 `.gitignore`
3. **定期更新密码和 Token**
4. **限制机器人的访问权限** - 仅在必要的群组中使用
