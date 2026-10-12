import json
import os
import urllib.request
from datetime import datetime, timezone
from html import escape
from pathlib import Path

USER = 'mdabuhanif230'
ROOT = Path(__file__).resolve().parents[1]

def api(path):
    headers = {'Accept': 'application/vnd.github+json', 'User-Agent': 'Hanif-Profile', 'X-GitHub-Api-Version': '2022-11-28'}
    if os.environ.get('GH_TOKEN'):
        headers['Authorization'] = 'Bearer ' + os.environ['GH_TOKEN']
    with urllib.request.urlopen(urllib.request.Request('https://api.github.com' + path, headers=headers), timeout=30) as response:
        return json.load(response)

def main():
    user = api('/users/' + USER)
    repos = []
    page = 1
    while True:
        batch = api(f'/users/{USER}/repos?per_page=100&page={page}')
        repos.extend(batch)
        if len(batch) < 100:
            break
        page += 1
    original = [r for r in repos if not r['fork']]
    languages = {}
    for repo in original:
        if repo['language']:
            languages[repo['language']] = languages.get(repo['language'], 0) + 1
    top = sorted(languages.items(), key=lambda item: (-item[1], item[0]))[:5]
    values = [('PUBLIC REPOS', user['public_repos']), ('FOLLOWERS', user['followers']), ('STARS EARNED', sum(r['stargazers_count'] for r in original)), ('ORIGINAL REPOS', len(original))]
    svg = ['<svg xmlns="http://www.w3.org/2000/svg" width="1100" height="275" viewBox="0 0 1100 275"><title>Md Abu Hanif public GitHub statistics</title><rect width="1100" height="275" rx="22" fill="#0d1626"/><rect x="1" y="1" width="1098" height="273" rx="22" fill="none" stroke="#203752"/><g font-family="DejaVu Sans,Arial,sans-serif"><text x="35" y="42" fill="#58d6ff" font-size="21" font-weight="bold">GITHUB / LIVE SNAPSHOT</text>']
    for index, (label, value) in enumerate(values):
        x = 35 + index * 270
        svg.append(f'<text x="{x}" y="108" fill="#f3f8ff" font-size="40" font-weight="bold">{value}</text><text x="{x}" y="139" fill="#90a9c5" font-size="13">{label}</text>')
    summary = '  /  '.join(f'{name}: {count}' for name, count in top) or 'No repository languages yet'
    svg.append(f'<text x="35" y="192" fill="#d2e5fa" font-size="14">Primary language by original public repository: {escape(summary)}</text>')
    svg.append(f'<text x="35" y="236" fill="#90a9c5" font-size="12">Updated {datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")} · Public data only · Fork stars excluded</text></g></svg>')
    (ROOT / 'assets' / 'github-stats.svg').write_text(''.join(svg), encoding='utf-8')

if __name__ == '__main__':
    main()
