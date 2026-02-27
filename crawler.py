#!/usr/bin/env python3
"""
AI+WiFi Literature Crawler
每日爬取最新的AI和WiFi融合研究工作
特别标注与环境感知和重建相关的论文
"""

import requests
import json
import os
from datetime import datetime, timedelta
import feedparser
from pathlib import Path

# 环境感知和重建相关的关键词
ENV_SENSING_KEYWORDS = [
    '环境感知', 'environmental sensing', 'environment reconstruction',
    '环境重建', 'scene reconstruction', 'scene understanding',
    '室内定位', 'indoor localization', 'indoor positioning',
    '姿态估计', 'pose estimation', 'human pose',
    '活动识别', 'activity recognition', 'gesture recognition',
    '占有地图', 'occupancy mapping', 'occupancy detection',
    '异常检测', 'anomaly detection',
    '存在感知', 'presence detection', '人体检测', 'human detection',
]

class WiFiAICrawler:
    def __init__(self):
        self.results = {
            'env_sensing': [],
            'general': [],
            'timestamp': datetime.now().isoformat()
        }
        
    def search_arxiv(self, keywords, max_results=50):
        """从arXiv搜索相关论文"""
        print(f"📡 正在从arXiv搜索: {keywords}")
        
        base_url = 'http://export.arxiv.org/api/query?'
        search_query = ' OR '.join(keywords)
        
        params = {
            'search_query': f'cat:cs.AI OR cat:cs.NI OR cat:eess.SP AND ({search_query})',
            'start': 0,
            'max_results': max_results,
            'sortBy': 'submittedDate',
            'sortOrder': 'descending'
        }
        
        try:
            response = requests.get(base_url, params=params, timeout=10)
            response.raise_for_status()
            
            feed = feedparser.parse(response.content)
            
            for entry in feed.entries:
                paper = {
                    'title': entry.title,
                    'authors': [author.name for author in entry.authors],
                    'summary': entry.summary.replace('\n', ' '),
                    'arxiv_id': entry.id.split('/abs/')[-1],
                    'published': entry.published,
                    'link': entry.id,
                    'categories': entry.get('arxiv_primary_category', {}).get('term', 'N/A'),
                }
                
                # 检查是否与环境感知和重建相关
                full_text = (paper['title'] + ' ' + paper['summary']).lower()
                is_env_sensing = any(keyword.lower() in full_text for keyword in ENV_SENSING_KEYWORDS)
                
                if is_env_sensing:
                    self.results['env_sensing'].append(paper)
                else:
                    self.results['general'].append(paper)
                    
            print(f"✓ 找到 {len(feed.entries)} 篇论文")
            
        except Exception as e:
            print(f"✗ arXiv搜索出错: {e}")
    
    def search_github(self, keywords, max_results=30):
        """从GitHub搜索相关项目"""
        print(f"🔍 正在从GitHub搜索: WiFi + AI 相关项目")
        
        base_url = 'https://api.github.com/search/repositories'
        
        search_terms = ' '.join(keywords)
        params = {
            'q': f'{search_terms} sort:stars language:python',
            'per_page': max_results,
        }
        
        headers = {
            'Accept': 'application/vnd.github.v3+json',
        }
        
        try:
            response = requests.get(base_url, params=params, headers=headers, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            for repo in data.get('items', []):
                project = {
                    'name': repo['name'],
                    'owner': repo['owner']['login'],
                    'description': repo['description'] or 'N/A',
                    'url': repo['html_url'],
                    'stars': repo['stargazers_count'],
                    'updated': repo['updated_at'],
                    'language': repo['language'],
                }
                
                # 检查是否与环境感知相关
                full_text = (repo['name'] + ' ' + (repo['description'] or '')).lower()
                is_env_sensing = any(keyword.lower() in full_text for keyword in ENV_SENSING_KEYWORDS)
                
                if is_env_sensing:
                    self.results['env_sensing'].append(project)
                else:
                    self.results['general'].append(project)
                    
            print(f"✓ 找到 {len(data.get('items', []))} 个项目")
            
        except Exception as e:
            print(f"✗ GitHub搜索出错: {e}")
    
    def save_report(self, output_dir='./reports'):
        """生成并保存每日报告"""
        Path(output_dir).mkdir(exist_ok=True)
        
        # 生成Markdown报告
        date_str = datetime.now().strftime('%Y-%m-%d')
        report_path = f"{output_dir}/report_{date_str}.md"
        
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(f"# AI+WiFi 研究文献每日报告\n")
            f.write(f"**生成时间:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            
            # 环境感知和重建相关
            if self.results['env_sensing']:
                f.write(f"## 🎯 环境感知与重建相关 ({len(self.results['env_sensing'])} 篇)\n\n")
                for idx, item in enumerate(self.results['env_sensing'][:20], 1):
                    if 'arxiv_id' in item:
                        f.write(f"### {idx}. {item['title']}\n")
                        f.write(f"**作者:** {', '.join(item['authors'][:3])}{'...' if len(item['authors']) > 3 else ''}\n")
                        f.write(f"**类别:** {item['categories']}\n")
                        f.write(f"**发表:** {item['published'][:10]}\n")
                        f.write(f"**摘要:** {item['summary'][:300]}...\n")
                        f.write(f"**链接:** [{item['arxiv_id']}]({item['link']})\n\n")
                    elif 'owner' in item:
                        f.write(f"### {idx}. [{item['name']}]({item['url']})\n")
                        f.write(f"**所有者:** {item['owner']} | **Stars:** {item['stars']}\n")
                        f.write(f"**描述:** {item['description']}\n")
                        f.write(f"**更新:** {item['updated'][:10]}\n\n")
            
            # 通用AI+WiFi相关
            if self.results['general']:
                f.write(f"## 📚 其他AI+WiFi相关研究 ({len(self.results['general'])} 篇)\n\n")
                for idx, item in enumerate(self.results['general'][:20], 1):
                    if 'arxiv_id' in item:
                        f.write(f"### {idx}. {item['title']}\n")
                        f.write(f"**作者:** {', '.join(item['authors'][:3])}{'...' if len(item['authors']) > 3 else ''}\n")
                        f.write(f"**类别:** {item['categories']}\n")
                        f.write(f"**发表:** {item['published'][:10]}\n")
                        f.write(f"**摘要:** {item['summary'][:300]}...\n")
                        f.write(f"**链接:** [{item['arxiv_id']}]({item['link']})\n\n")
            
            f.write(f"---\n")
            f.write(f"**统计:** \n")
            f.write(f"- 环境感知与重建相关: {len(self.results['env_sensing'])}\n")
            f.write(f"- 其他AI+WiFi相关: {len(self.results['general'])}\n")
        
        # 保存JSON数据供后续处理
        json_path = f"{output_dir}/data_{date_str}.json"
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(self.results, f, ensure_ascii=False, indent=2)
        
        print(f"✓ 报告已保存到: {report_path}")
        return report_path

def main():
    print("=" * 60)
    print("🚀 AI+WiFi 研究文献爬虫")
    print("=" * 60)
    print()
    
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
    crawler.search_arxiv(keywords, max_results=100)
    crawler.search_github(keywords[:2], max_results=30)
    
    # 生成报告
    report_path = crawler.save_report()
    
    print()
    print(f"📊 总计找到:")
    print(f"  - 环境感知与重建: {len(crawler.results['env_sensing'])}")
    print(f"  - 其他AI+WiFi: {len(crawler.results['general'])}")
    print()

if __name__ == '__main__':
    main()
