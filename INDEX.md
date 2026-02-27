# 📚 项目文件索引和快速参考

完整的 AI+WiFi 研究文献爬虫系统文件导图。

## 🗂️ 项目结构

```
AI_WiFi_literature/
├── 📖 文档文件
│   ├── README.md ......................... 项目完整说明（必读）
│   ├── QUICK_START.md ................... 5分钟快速开始（入门推荐）
│   ├── WECHAT_SETUP.md .................. 微信企业号配置（本文档相关）
│   ├── NOTIFICATION_SETUP.md ............ 邮件/钉钉/微信通知完整指南
│   ├── CRON_SETUP.md .................... 本地定时任务配置
│   └── SAMPLE_REPORT.md ................. 报告示例
│
├── 🐍 Python 核心脚本
│   ├── crawler.py ....................... 主爬虫脚本（核心）
│   ├── config.py ........................ 配置管理
│   ├── notifier.py ...................... 通知模块（邮件/钉钉/微信）
│   ├── setup.py ......................... 初始化和测试工具
│   ├── wechat_setup.py .................. 微信企业号配置助手
│   └── wechat_integration_guide.py ...... 微信集成指南
│
├── 🔧 配置和部署
│   ├── requirements.txt ................. Python 依赖
│   ├── run_crawler.sh ................... 运行脚本
│   ├── .github/workflows/
│   │   └── daily-crawler.yml ............ GitHub Actions 工作流
│   └── .gitignore ....................... Git 忽略规则
│
└── 📊 输出目录（自动生成）
    └── reports/
        ├── report_YYYY-MM-DD.md ........ 每日 Markdown 报告
        └── data_YYYY-MM-DD.json ........ 每日 JSON 数据
```

---

## 🎯 按使用场景快速导航

### 🚀 **我想快速开始**
→ [QUICK_START.md](QUICK_START.md) - 5分钟快速入门

### 📱 **我要配置微信企业号通知**
→ [WECHAT_SETUP.md](WECHAT_SETUP.md) - 7分钟完整配置指南

### 📧 **我要配置邮件/钉钉/微信通知**
→ [NOTIFICATION_SETUP.md](NOTIFICATION_SETUP.md) - 综合通知指南

### ⏰ **我要每天自动运行爬虫**
→ [CRON_SETUP.md](CRON_SETUP.md) - 定时任务配置

### 🔍 **我想了解项目的完整信息**
→ [README.md](README.md) - 完整项目说明

### 💻 **我想自定义爬虫参数**
→ [config.py](config.py) - 配置文件

### 🎨 **我想自定义消息格式**
→ [notifier.py](notifier.py) - 通知模块

---

## ⚡ 最常用的命令

```bash
# 首次安装
pip install -r requirements.txt

# 检查环境和测试
python3 setup.py

# 手动运行爬虫
python3 crawler.py

# 配置微信企业号
python3 wechat_setup.py

# 测试微信配置
python3 wechat_setup.py test

# 查看集成指南
python3 wechat_integration_guide.py

# 查看最新报告
cat reports/report_$(date +%Y-%m-%d).md

# 启用 GitHub Actions（推送到 GitHub）
git push
```

---

## 📋 文件功能速览

| 文件 | 类型 | 用途 | 修改建议 |
|------|------|------|--------|
| [crawler.py](crawler.py) | 🐍 脚本 | 主爬虫逻辑 | 修改搜索关键词/来源 |
| [config.py](config.py) | ⚙️ 配置 | 所有配置管理 | 启用/禁用通知 |
| [notifier.py](notifier.py) | 📮 模块 | 邮件/钉钉/微信通知 | 自定义消息格式 |
| [setup.py](setup.py) | 🔧 工具 | 环境检查和初始化 | 一般不需修改 |
| [wechat_setup.py](wechat_setup.py) | 🎯 工具 | 微信配置助手 | 测试配置 |
| [wechat_integration_guide.py](wechat_integration_guide.py) | 📖 工具 | 集成指南显示 | 一般不需修改 |
| [requirements.txt](requirements.txt) | 📦 依赖 | Python 包依赖 | 添加新依赖 |
| [run_crawler.sh](run_crawler.sh) | 🔨 脚本 | 运行脚本 | 一般不需修改 |
| [daily-crawler.yml](/.github/workflows/daily-crawler.yml) | ⚙️ 工作流 | GitHub Actions 配置 | 修改运行时间/环境 |

---

## 🎓 学习路径

### 初学者路径（20 分钟）
1. 阅读 [QUICK_START.md](QUICK_START.md)
2. 运行 `python3 setup.py`
3. 运行 `python3 crawler.py`
4. 查看 `reports/` 中的报告

### 进阶用户路径（1 小时）
1. 阅读 [README.md](README.md)
2. 修改 [config.py](config.py) 自定义搜索
3. 配置通知方式 [NOTIFICATION_SETUP.md](NOTIFICATION_SETUP.md)
4. 推送到 GitHub 启用自动化

### 微信企业号专区（15 分钟）
1. 阅读 [WECHAT_SETUP.md](WECHAT_SETUP.md)
2. 运行 `python3 wechat_setup.py`
3. 运行 `python3 wechat_setup.py test`
4. 集成到爬虫中

---

## 🔗 外部链接

- **企业微信官网**: https://work.weixin.qq.com/
- **arXiv API 文档**: https://arxiv.org/help/api
- **GitHub API 文档**: https://docs.github.com/en/rest
- **企业微信 API 文档**: https://work.weixin.qq.com/api/doc

---

## ❓ 常见问题速查表

| 问题 | 文档 | 命令 |
|------|------|------|
| 如何开始? | [QUICK_START.md](QUICK_START.md) | `python3 setup.py` |
| 如何配置微信? | [WECHAT_SETUP.md](WECHAT_SETUP.md) | `python3 wechat_setup.py` |
| 如何配置邮件/钉钉? | [NOTIFICATION_SETUP.md](NOTIFICATION_SETUP.md) | 见文档 |
| 如何每天自动运行? | [CRON_SETUP.md](CRON_SETUP.md) | `crontab -e` 或推送到 GitHub |
| 如何修改搜索关键词? | [config.py](config.py) | 编辑 `ENV_SENSING_KEYWORDS` |
| 如何自定义消息? | [notifier.py](notifier.py) | 编辑 `generate_markdown_summary()` |
| 环境配置有问题? | [QUICK_START.md](QUICK_START.md) | `python3 setup.py` |
| 微信消息没收到? | [WECHAT_SETUP.md](WECHAT_SETUP.md) | `python3 wechat_setup.py test` |

---

## 📊 文件依赖关系

```
crawler.py
    ├── 导入 config.py
    ├── 导入 notifier.py（可选）
    └── 生成输出到 reports/

config.py
    └── 被 crawler.py 和 notifier.py 导入

notifier.py
    └── 被 crawler.py 导入（用于发送通知）

setup.py
    └── 独立工具，检查环境

wechat_setup.py
    └── 独立工具，配置微信

wechat_integration_guide.py
    └── 独立工具，显示集成指南
```

---

## 💾 备份和维护

**定期备份：**
```bash
# 备份报告
tar -czf reports_backup_$(date +%Y%m%d).tar.gz reports/

# 推送到 GitHub
git push
```

**清理旧报告：**
```bash
# 删除 30 天前的报告
find reports/ -name "*.md" -mtime +30 -delete
```

---

## 🚀 下一步建议

1. ✅ 阅读 [QUICK_START.md](QUICK_START.md)
2. ✅ 运行 `python3 setup.py` 检查环境
3. ✅ 运行 `python3 crawler.py` 获取第一份报告
4. ✅ 选择喜欢的通知方式：
   - 📱 微信企业号 → [WECHAT_SETUP.md](WECHAT_SETUP.md)
   - 🔔 钉钉 → [NOTIFICATION_SETUP.md](NOTIFICATION_SETUP.md)
   - 📧 邮件 → [NOTIFICATION_SETUP.md](NOTIFICATION_SETUP.md)
5. ✅ 推送到 GitHub 启用自动化

---

## 📞 获取帮助

1. 查看对应的文档文件
2. 运行相应的测试脚本
3. 检查浏览器开发者工具（如有错误）
4. 查看终端输出的详细错误信息

---

**祝您使用愉快！如有问题，请查阅相应文档。🎉**
