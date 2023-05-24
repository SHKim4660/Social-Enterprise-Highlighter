from flask import Flask
from typing import Dict, Union, Tuple, Any
import json
import csv
import re
import trie
import os
import sys

# 객체 초기화
app = Flask(__name__)
tr = trie.Trie()

# 트라이 초기화 함수
def trie_insert(filename):
    file = open(filename,'r')
    reader = csv.reader(file)
    for line in reader:
        tr.insert(line[0])
    file.close()

# 트라이에 데이터 삽입
trie_insert(os.path.join('data', 'pro_name_data.csv'))
trie_insert(os.path.join('data', 'pro_KRE_data.csv'))

# 유저스크립트 제공
@app.route('/userscript.user.js')
def userscript():
    str = ""
    try:
        with open(os.path.join('gmarket_highlighter.user.js'), "r") as f:
            str = f.read()
    except Exception as e:
        sys.stderr.write(f"Warning: Cannot read userscript file.: ", e)

    return str

# api 제공
@app.route('/api/<string:vendor>')
def api(vendor):
    global tr
    # cleaning
    pattern = r'\([^)]*\)'
    pro_vendor = re.sub(pattern=pattern, repl='', string= vendor).replace("㈜","").replace("유)","").replace("주)","").replace("사)","").replace(" ","").replace("주식회사","").replace("사단법인","")
    # 트라이에 있으면
    if tr.search(pro_vendor):
        return "YEP"
    else:
        return "NOP"
    
if __name__ == "__main__":
    app.run(port=8081)











