# 微信企业号完整配置步骤

## 🚀 5 分钟快速配置

### 1️⃣ 注册企业微信（2 分钟）

访问 https://work.weixin.qq.com 并完成以下步骤：

```
企业微信官网 → 立即开始 → 企业注册
↓
填写企业信息（公司名称等）
↓
选择认证方式（营业执照或组织代码）
↓
创建成功
```

### 2️⃣ 创建应用和 Webhook（2 分钟）

在企业微信管理后台：

```
应用 → 创建应用 → 填写信息
↓
应用名称：AI 研究爬虫
可见范围：选择相关部门/成员
↓
创建成功后，查看应用详情
↓
找到 Webhook URL → 复制
```

**会得到类似这样的 Webhook URL：**
```
https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=xxxxxxxxxxxxxxxx
```

### 3️⃣ 配置环境变量（1 分钟）

**Linux/macOS:**
```bash
export WECHAT_WEBHOOK="https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=xxxxxxxxxxxxxxxx"
```

**Windows PowerShell:**
```powershell
$env:WECHAT_WEBHOOK="https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=xxxxxxxxxxxxxxxx"
```

**Windows CMD:**
```cmd
setx WECHAT_WEBHOOK "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=xxxxxxxxxxxxxxxx"
```

### 4️⃣ 测试配置（1 分钟）

```bash
python3 wechat_setup.py test
```

看到 `✅ 测试成功！消息已发送` 就配置完成了！

---

## 🔧 集成到爬虫

### A. 修改 config.py

```python
# 在 CrawlerConfig 中修改：
ENABLE_WECHAT: bool = True
# WECHAT_WEBHOOK 会自动从环境变量读取
```

### B. 修改 crawler.py

在 `main()` 函数末尾添加：

```python
from config import config
from notifier import NotificationManager

# ... 爬虫代码 ...

# 发送微信企业号通知
if config.ENABLE_WECHAT:
    notifier = NotificationManager(config)
    markdown_summary = notifier.generate_markdown_summary(crawler.results)
    notifier.send_wechat(
        "🤖 AI+WiFi 研究文献日报",
        markdown_summary,
        message_type="markdown"
    )
```

### C. 运行爬虫

```bash
python3 crawler.py
```

完成！现在每次运行爬虫都会自动发送微信通知了。

---

## 📱 与 GitHub Actions 集成

### 1. 在 GitHub 中添加 Secret

1. 进入仓库 → Settings → Secrets and variables → Actions
2. 新建 Secret：
   - 名称：`WECHAT_WEBHOOK`
   - 值：粘贴您的 Webhook URL

### 2. 修改 GitHub Actions 配置

编辑 `.github/workflows/daily-crawler.yml`：

```yaml
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
```

### 3. 推送到 GitHub

```bash
git push
```

现在爬虫每天都会自动运行并发送微信通知！

---

## 💡 自定义消息

编辑 [notifier.py](notifier.py) 中的 `generate_markdown_summary()` 函数：

```python
def generate_markdown_summary(self, results: Dict[str, Any]) -> str:
    """生成 Markdown 格式的摘要"""
    md = f"""## 您的标题
    
### 统计
- 环境感知与重建: {len(results.get('env_sensing', []))} 篇

### 内容
...
"""
    return md
```

常用 Markdown 格式：
- `# 标题一级`
- `## 标题二级`
- `**粗体**`
- `> 引用块`
- `- 列表`
- `[链接](URL)`

---

## 🧪 常见问题

| 问题 | 解决方案 |
|------|--------|
| 收不到消息 | 检查 Webhook URL 是否正确、运行 `python3 wechat_setup.py test` |
| 环境变量不生效 | 重启终端或重新登录系统 |
| 消息格式不对 | 检查是否使用了 `message_type="markdown"` |
| 导入错误 | 确保 config.py 和 notifier.py 在同一目录 |
| Webhook 过期 | 重新从企业微信后台复制 URL |

---

## 📞 支持的消息类型

### 文本消息（纯文本）
```python
notifier.send_wechat("标题", "内容", message_type="text")
```

### Markdown 消息（推荐）
```python
notifier.send_wechat("标题", "## 内容\n...", message_type="markdown")
```

---

## 📚 相关文件

- [wechat_setup.py](wechat_setup.py) - 配置助手和测试工具
- [wechat_integration_guide.py](wechat_integration_guide.py) - 集成指南
- [notifier.py](notifier.py) - 通知模块（包含微信发送代码）
- [config.py](config.py) - 配置管理
- [NOTIFICATION_SETUP.md](NOTIFICATION_SETUP.md) - 通知完整指南

---

## 🎯 总结

| 步骤 | 时间 |
|------|------|
| 注册企业微信 | 2 分钟 |
| 创建应用和 Webhook | 2 分钟 |
| 配置环境变量 | 1 分钟 |
| 修改配置文件 | 1 分钟 |
| 测试 | 1 分钟 |
| **总计** | **7 分钟** |

现在您可以每天自动收到最新的 AI+WiFi 研究文献报告了！🎉
