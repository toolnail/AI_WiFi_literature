# 快速开始指南 🚀

## 5 分钟快速启动

### 1. 安装依赖 (30 秒)

```bash
pip install -r requirements.txt
```

### 2. 首次运行 (1 分钟)

```bash
python3 setup.py    # 检查环境
python3 crawler.py  # 运行爬虫
```

查看报告：
```bash
cat reports/report_$(date +%Y-%m-%d).md
```

### 3. 设置自动化 (2 分钟)

选择以下任一方式：

#### 方式 A: GitHub Actions（推荐）
直接 `git push` 到 GitHub 即可，爬虫会自动每天运行

#### 方式 B: Linux/macOS Cron
```bash
crontab -e
# 添加这一行（每天 09:00 运行）
0 9 * * * cd /path/to/AI_WiFi_literature && python3 crawler.py
```

#### 方式 C: Windows 任务计划程序
1. 打开"任务计划程序"
2. 创建基本任务
3. 设置触发时间：每天上午 9:00
4. 操作：运行程序 `python.exe`，参数 `crawler.py`

### 4. (可选) 配置通知 (1 分钟)

设置环境变量并修改 `config.py`：

**钉钉（推荐中国用户）：**
```bash
export DINGTALK_WEBHOOK="https://oapi.dingtalk.com/robot/send?access_token=xxx"
```

**邮件：**
```bash
export SMTP_PASSWORD="xxxx xxxx xxxx xxxx"
# 修改 config.py 中的 EMAIL_FROM 和 EMAIL_TO
```

详见 [NOTIFICATION_SETUP.md](NOTIFICATION_SETUP.md)

---

## 📊 查看报告

### 最新报告
```bash
cat reports/report_$(date +%Y-%m-%d).md
```

### 所有历史报告
```bash
ls -la reports/
```

### 搜索特定主题
```bash
grep -r "环境感知\|room reconstruction" reports/
```

---

## 🔍 自定义搜索关键词

编辑 `config.py` 中的 `CrawlerConfig` 类：

```python
ENV_SENSING_KEYWORDS = [
    '您的关键词1', 'your-keyword-1',
    '您的关键词2', 'your-keyword-2',
    # ...
]

SEARCH_KEYWORDS = [
    'WiFi your-topic',
    'CSI your-topic',
    # ...
]
```

---

## 🐛 故障排查

### 命令运行失败？
```bash
# 检查 Python 版本
python3 --version  # 需要 3.6+

# 检查依赖
pip list | grep -E "feedparser|requests"

# 重新安装依赖
pip install -r requirements.txt --upgrade
```

### 网络连接问题？
- 检查 arXiv 是否在您的地区可用
- 使用 VPN 或梯子 (需要自行配置)
- 检查防火墙设置

### 报告为空？
- 等待爬虫完成执行
- 检查 `reports/` 目录
- 查看是否有 JSON 文件生成

---

## 📚 完整文档

- [README.md](README.md) - 项目完整说明
- [SAMPLE_REPORT.md](SAMPLE_REPORT.md) - 报告示例
- [NOTIFICATION_SETUP.md](NOTIFICATION_SETUP.md) - 通知配置详细指南
- [CRON_SETUP.md](CRON_SETUP.md) - 精品计划任务配置

---

## 💡 使用建议

### 订阅工具推荐
- 💌 邮件：Gmail + SMTP（需要应用密码）
- 📱 钉钉：企业版或免费版均可（推荐中国用户）
- 💬 微信：企业微信（适合企业团队）

### 报告查看
- 📖 每日查看 Markdown 报告
- 📊 导出 JSON 进行二次分析
- 🔍 使用 grep 搜索感兴趣的主题

### 扩展建议
- 添加更多数据源（PubMed, IEEE, 等）
- 集成文献管理工具（Mendeley, Zotero）
- 自动生成文献综述
- 设置每周/月度汇总报告

---

## 📞 需要帮助？

检查以下几项：

1. ✅ Python 版本 >= 3.6
2. ✅ 依赖已安装：`pip install -r requirements.txt`
3. ✅ 网络连接正常
4. ✅ 查看报告目录：`ls -la reports/`
5. ✅ 查看日志输出确认运行状态

---

**祝您使用愉快！👋**
