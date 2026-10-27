"""Validate a board model and build the self-contained board workspace."""
import argparse
import json
import math
import re
from pathlib import Path

KINDS = {'text','image','rect','roundrect','ellipse','triangle','diamond','polygon','line','arrow'}

def validate_project(project):
    def require(condition, message):
        if not condition:
            raise ValueError(message)
    def number(value):
        return isinstance(value, (int,float)) and not isinstance(value,bool) and math.isfinite(value)
    def embedded_image(value):
        return isinstance(value,str) and value.startswith('data:image/')
    require(isinstance(project,dict), 'Project must be an object')
    require(isinstance(project.get('id'),str) and bool(project['id']), 'Missing project id')
    require(isinstance(project.get('title'),str), 'Missing project title')
    require(all(number(project.get(k)) and project[k]>=50 for k in ('width','height')), 'Page dimensions must be finite and at least 50 mm')
    require(isinstance(project.get('nodes'),list), 'Missing nodes array')
    seen=set()
    for i,n in enumerate(project['nodes']):
        prefix=f'Element {i+1}: '
        require(isinstance(n,dict),prefix+'must be an object')
        require(isinstance(n.get('id'),str) and bool(re.fullmatch(r'[A-Za-z0-9_-]+',n['id'])) and n['id'] not in seen,prefix+'invalid or duplicate id')
        seen.add(n['id'])
        require(n.get('kind') in KINDS,prefix+'unknown kind')
        require(all(number(n.get(k)) for k in ('x','y','w','h')),prefix+'invalid geometry')
        require(n['w']>0 and (n['h']>=0 if n['kind'] in {'line','arrow'} else n['h']>0),prefix+'invalid size')
        for k in ('rotation','opacity','strokeWidth','radius','weight'):
            if k in n:
                require(number(n[k]),prefix+'invalid '+k)
        require(0<=n.get('opacity',1)<=1,prefix+'opacity must be 0–1')
        require(n.get('strokeWidth',0)>=0 and n.get('radius',0)>=0,prefix+'negative edge or radius')
        if n['kind']=='text':
            require(isinstance(n.get('text'),str),prefix+'missing text')
            require(number(n.get('fontSize')) and n['fontSize']>0,prefix+'invalid font size')
            require(number(n.get('leading',1.3)) and n.get('leading',1.3)>0,prefix+'invalid line spacing')
        if n['kind']=='image':
            require(embedded_image(n.get('src')),prefix+'embed image bytes first')
            require(n.get('fit','contain') in {'contain','cover'},prefix+'invalid image fit')
        if 'points' in n:
            pts=n['points']
            require(isinstance(pts,list) and 3<=len(pts)<=100 and all(isinstance(v,list) and len(v)==2 and all(number(x) for x in v) for v in pts),prefix+'invalid polygon points')
    require(isinstance(project.get('decorations',[]),list),'Invalid decorations')
    for d in project.get('decorations',[]):
        require(isinstance(d,dict) and isinstance(d.get('id'),str) and bool(re.fullmatch(r'[A-Za-z0-9_-]+',d['id'])),'Invalid decoration id')
        require(embedded_image(d.get('src')),'Embed decoration bytes first')
        require(all(number(d.get(k)) and d[k]>0 for k in ('w','h')),'Invalid decoration size')
        require(all(number(d.get(k,0)) for k in ('x','y')),'Invalid decoration position')
        require(isinstance(d.get('regions',[]),list) and all(isinstance(r,list) and len(r)==4 and all(number(x) for x in r) and r[2]>0 and r[3]>0 for r in d.get('regions',[])),'Invalid decoration clip regions')
    return project

def build(project, output):
    if isinstance(project, dict) and isinstance(project.get('pages'), list):
        if not project['pages']:
            raise ValueError('Missing pages')
        page_ids=set()
        for page in project['pages']:
            if not isinstance(page, dict) or not isinstance(page.get('id'), str) or page['id'] in page_ids:
                raise ValueError('Invalid or duplicate page id')
            page_ids.add(page['id'])
            nodes=page.get('nodes')
            if not isinstance(nodes, list):
                raise ValueError('Missing nodes array')
            ids=[node.get('id') for node in nodes if isinstance(node,dict)]
            if len(ids)!=len(nodes) or len(ids)!=len(set(ids)):
                raise ValueError('Invalid or duplicate element id')
            if any(node.get('kind')=='group' and
                   (not isinstance(node.get('id'),str) or not re.fullmatch(r'[A-Za-z0-9_-]+',node['id']))
                   for node in nodes):
                raise ValueError('Invalid group id')
            if any(node.get('parentId') not in ids for node in nodes if node.get('parentId')):
                raise ValueError('Unknown parent group')
            validate_project({**page, 'id': page.get('id'), 'title': page.get('title', ''),
                              'width': page.get('width'), 'height': page.get('height'),
                              'nodes': [node for node in nodes if node.get('kind')!='group']})
        if project.get('activePageId') not in page_ids:
            raise ValueError('Invalid active page id')
        count=sum(len(page['nodes']) for page in project['pages'])
    else:
        validate_project(project)
        count=len(project['nodes'])
    assets=Path(__file__).resolve().parent.parent/'assets'
    template=(assets/'editor-shell.html').read_text(encoding='utf-8')
    css=(assets/'editor.css').read_text(encoding='utf-8')
    js=(assets/'editor.js').read_text(encoding='utf-8')
    data=json.dumps(project,ensure_ascii=False,allow_nan=False).replace('<',r'\u003c')
    out=Path(output);out.parent.mkdir(parents=True,exist_ok=True)
    template=template.replace('<link rel="stylesheet" href="editor.css">',f'<style>{css}</style>')
    template=template.replace('<script src="editor.js"></script>',f'<script>{js}</script>')
    out.write_text(template.replace('__BOARD_PROJECT__',data),encoding='utf-8')
    return count

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('project');parser.add_argument('output');args=parser.parse_args()
    try:
        project=json.loads(Path(args.project).read_text())
        count=build(project,args.output)
    except (ValueError,KeyError,TypeError) as error:
        parser.exit(2,f'Invalid board project: {error}\n')
    print(f'Created editor: {count} editable elements')

if __name__=='__main__':
    main()
