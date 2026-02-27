#!/bin/bash
# GitHub Actions 定时爬虫脚本
# 这个脚本可以通过 GitHub Actions 每天自动运行

set -e

echo "开始运行 AI+WiFi 研究文献爬虫..."
cd "$(dirname "$0")" || exit 1

# 安装依赖
pip install -q -r requirements.txt

# 运行爬虫
python3 crawler.py

echo "爬虫运行完成！"

# 如果需要，可以在这里添加提交更改到Git
if [ "$AUTO_COMMIT" = "true" ]; then
    git add -A
    git commit -m "daily: update AI+WiFi research literature - $(date +%Y-%m-%d)" || true
    git push
fi
