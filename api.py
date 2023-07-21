from flask import Flask
from typing import Dict, Union, Tuple, Any
import json
import csv
import re
import trie
import os
import sys

def get_file_or_empty(filename: str):
    string = ""
    try:
        with open(os.path.join(filename), "r") as f:
            string = f.read()
    except Exception as e:
        sys.stderr.write(f"Error: Cannot read the file, {filename}.: {e}")

    return string

# 객체 초기화
app = Flask(__name__)
tr = trie.Trie()

# 트라이 초기화 함수
def trie_insert(filename):
    file = open(filename,'r',encoding = 'utf8')
    reader = csv.reader(file)
    for line in reader:
        # TODO
        name = line[0][:-1]
        job = "한국사회적기업진흥원 선정"  if line[0][-1] else "K-RE100 참여기업"

        tr.insert(name, job)
    file.close()

# 트라이에 데이터 삽입
trie_insert(os.path.join('data', 'data.csv'))
# trie_insert(os.path.join('data', 'pro_name_data.csv'))
# trie_insert(os.path.join('data', 'pro_KRE_data.csv'))

# 유저스크립트 제공
@app.route('/userscript.user.js')
def userscript():
    return get_file_or_empty("gmarket_highlighter.user.js")

# api 제공
@app.route('/api/<string:vendor>')
def api(vendor):
    global tr
    # cleaning
    pattern = r'\([^)]*\)'
    pro_vendor = re.sub(pattern=pattern, repl='', string= vendor).replace("㈜","").replace("유)","").replace("주)","").replace("사)","").replace(" ","").replace("주식회사","").replace("사단법인","")
    pro_pro_vendor = f"{pro_vendor}7"
    # 트라이에 있으면
    serch = tr.search(pro_vendor)
    if serch is not None:
        return serch, 200
    else:
        return "NOP", 404

@app.route('/style.css')
def css():
    return get_file_or_empty("style.css")
    
if __name__ == "__main__":
    app.run(port=5000)


