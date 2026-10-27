"""Regression checks for board-model errors and lossless HTML serialization."""
import copy
import json
import tempfile
import unittest
from pathlib import Path
from build_editor import build, validate_project


class ModelTests(unittest.TestCase):
    def setUp(self):
        self.project = {'id':'test','title':'中文<标题>','width':297,'height':420,
                        'nodes':[{'id':'a','kind':'text','x':12,'y':12,'w':100,
                                  'h':20,'fontSize':12,'text':'<文字> & </script> 中文 😀'}]}

    def test_lossless_serialization(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory)/'board.html'
            build(self.project,path)
            payload = path.read_text().split('<script id="projectData" type="application/json">',1)[1].split('</script>',1)[0]
            self.assertEqual(json.loads(payload),self.project)

    def test_invalid_properties(self):
        for field,value in [('fontSize',float('nan')),('weight',float('inf')),
                            ('opacity',2),('h',-1),('x',True),('kind','unknown')]:
            with self.subTest(field=field):
                project = copy.deepcopy(self.project)
                project['nodes'][0][field]=value
                with self.assertRaises(ValueError): validate_project(project)

    def test_duplicate_ids(self):
        self.project['nodes'].append(copy.deepcopy(self.project['nodes'][0]))
        with self.assertRaises(ValueError): validate_project(self.project)

    def test_horizontal_arrow(self):
        self.project['nodes']=[{'id':'arrow','kind':'arrow','x':0,'y':0,'w':60,'h':0}]
        validate_project(self.project)

    def test_workspace_pages_and_group(self):
        page={'id':'page1','title':'第一页','width':420,'height':297,'nodes':[
            {'id':'shape1','kind':'rect','x':10,'y':10,'w':30,'h':20,'parentId':'group1'},
            {'id':'group1','kind':'group','name':'图层组'}]}
        project={'schema':2,'id':'demo','title':'多页展板','activePageId':'page1',
                 'pages':[page,{'id':'page2','title':'第二页','width':297,'height':420,'nodes':[]}]}
        with tempfile.TemporaryDirectory() as directory:
            path=Path(directory)/'workspace.html'
            self.assertEqual(build(project,path),2)
            html=path.read_text(encoding='utf-8')
            self.assertIn('"activePageId": "page1"',html)
            self.assertIn('拖动绘制形状',html)
            self.assertNotIn('<script src="editor.js">',html)

    def test_invalid_polygon(self):
        self.project['nodes']=[{'id':'polygon','kind':'polygon','x':0,'y':0,'w':60,'h':40,'points':[[0,0],[1,1]]}]
        with self.assertRaises(ValueError): validate_project(self.project)


if __name__=='__main__': unittest.main()
