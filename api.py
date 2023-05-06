from flask import Flask
from typing import Dict, Union, Tuple, Any
import json
import csv
import re
import trie
import suffixtree
import os
import sys

app = Flask(__name__)
tr = trie.Trie()
st = suffixtree.SFXTree()

def trie_insert(filename):
    file = open(filename,'r')
    reader = csv.reader(file)
    for line in reader:
        tr.insert(line[0])
    file.close()

trie_insert(os.path.join('data', 'pro_name_data.csv'))
trie_insert(os.path.join('data', 'pro_KRE_data.csv'))

@app.route('/userscript.user.js')
def userscript():
    str = ""
    try:
        with open(os.path.join('gmarket_highlighter.user.js'), "r") as f:
            str = f.read()
    except Exception as e:
        sys.stderr.write(f"Warning: Cannot read userscript file.: ", e)

    return str

@app.route('/api/<string:vendor>')
def api(vendor):
    global tr
    pattern = r'\([^)]*\)'
    pro_vendor = re.sub(pattern=pattern, repl='', string= vendor).replace("㈜","").replace("유)","").replace("주)","").replace("사)","").replace(" ","").replace("주식회사","").replace("사단법인","")
    if tr.search(pro_vendor):
        return "YEP"
    else:
        return "NOP"
    
if __name__ == "__main__":
    app.run(port=8081)
