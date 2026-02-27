# AI_WiFi_literature 📡

AI+WiFi 研究文献自动爬虫系统 - 每日获取最新研究工作，自动标注环境感知和重建相关的论文。

## 功能特性

✨ **自动爬虫**
- 从 arXiv 爬取最新的 AI+WiFi 研究论文
- 从 GitHub 搜索相关的开源项目
- 每天自动更新（支持本地 cron 和 GitHub Actions）

🎯 **智能标注**
- 自动识别与环境感知和重建相关的工作
- 关键词匹配和文本分析
- 按照重要性分类展示

📊 **生成报告**
- Markdown 格式的每日报告
- JSON 格式的结构化数据
- 包含论文摘要、作者、发表日期、相关链接

## 快速开始

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 运行爬虫（手动）

```bash
python3 crawler.py
```

运行后会在 `reports/` 目录生成报告：
- `report_YYYY-MM-DD.md` - Markdown 格式报告
- `data_YYYY-MM-DD.json` - JSON 格式数据

### 3. 自动运行（三种方式）

#### 方式 A：GitHub Actions（推荐）
直接推送到 GitHub，GitHub Actions 会自动每天运行爬虫并保存结果。

- 编辑 `.github/workflows/daily-crawler.yml` 中的时间设置
- 默认每天 UTC 时间 08:00 运行

#### 方式 B：本地 Cron 任务（Linux/macOS）
详见 [CRON_SETUP.md](CRON_SETUP.md)

```bash
crontab -e
# 添加：0 9 * * * cd /path/to/AI_WiFi_literature && python3 crawler.py
```

#### 方式 C：手动执行脚本
```bash
bash run_crawler.sh
```

## 文件说明

```
├── crawler.py              # 主爬虫脚本
├── requirements.txt        # Python 依赖
├── run_crawler.sh         # 运行脚本
├── CRON_SETUP.md          # Cron 任务配置说明
├── .github/
│   └── workflows/
│       └── daily-crawler.yml  # GitHub Actions 工作流
└── reports/               # 输出报告目录（自动生成）
    ├── report_2024-XX-XX.md
    └── data_2024-XX-XX.json
```

## 搜索关键词配置

在 `crawler.py` 中修改以下部分以自定义搜索：

```python
ENV_SENSING_KEYWORDS = [
    '环境感知', 'environmental sensing', 'environment reconstruction',
    '环境重建', 'scene reconstruction', '室内定位', 'activity recognition',
    # ... 添加更多关键词
]

keywords = [
    'WiFi CSI channel state information',
    'WiFi sensing',
    # ... 添加更多搜索词
]
```

## 报告示例

### 环境感知与重建相关（🎯 优先）
包含以下关键词的论文会被自动标注：
- 环境感知、环境重建
- 室内定位、姿态估计
- 活动识别、手势识别
- 占有地图、异常检测
- 存在感知、人体检测

### 其他 AI+WiFi 相关
其他 WiFi 与 AI 融合的研究工作

## 数据来源

- **arXiv**: 最新学术论文（https://arxiv.org/）
- **GitHub**: 开源项目和代码

## API 限制说明

- **arXiv API**: 无认证限制，响应可能较慢
- **GitHub API**: 免认证用户 60 次/小时，认证用户 5000 次/小时
  - 添加 GitHub Token 可以提高限制：在 `crawler.py` 中配置

## 常见问题

### Q: 如何添加自己的搜索来源？
A: 在 `crawler.py` 中添加新的搜索方法，参考现有的 `search_arxiv()` 方法。

### Q: 报告中没有显示我期望的论文？
A: 检查 `ENV_SENSING_KEYWORDS` 是否包含相关关键词。

### Q: 如何处理网络连接问题？
A: 脚本已包含异常处理，连接失败时会显示错误信息。可在脚本中增加重试机制。

## 许可证

MIT License