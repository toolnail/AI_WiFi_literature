# 本地 Cron 任务配置说明

如果你想在本地每天运行爬虫，可以使用以下方式：

## Linux/macOS 系统

编辑 cron 任务表:
```bash
crontab -e
```

添加以下行（每天早上 9 点运行）:
```
0 9 * * * cd /path/to/AI_WiFi_literature && /usr/bin/python3 crawler.py >> /var/log/ai_wifi_crawler.log 2>&1
```

或者使用更完整的脚本：
```
0 9 * * * cd /path/to/AI_WiFi_literature && bash run_crawler.sh >> /var/log/ai_wifi_crawler.log 2>&1
```

## Windows 系统

使用任务计划程序：

1. 打开"任务计划程序"
2. 创建基本任务
3. 设置触发条件：每天上午 9:00
4. 操作：运行程序
   - 程序：`python.exe`
   - 参数：`C:\path\to\crawler.py`
   - 开始于：`C:\path\to\AI_WiFi_literature`

## 配置选项

在运行爬虫之前，可以编辑 `crawler.py` 中的配置：

- `ENV_SENSING_KEYWORDS`: 修改环境感知相关的关键词
- `max_results`: 调整返回的最大结果数
- `output_dir`: 更改报告保存目录

## 查看日志

```bash
# 查看最近的报告
ls -la reports/

# 查看最新的报告内容
cat reports/report_$(date +%Y-%m-%d).md

# 监视cron日志（macOS）
log stream --predicate 'process == "cron"' --level debug
```
