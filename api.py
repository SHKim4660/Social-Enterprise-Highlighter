from flask import Flask, request
from typing import Dict, Union, Tuple, Any
import json
import csv
import re
import trie
import os
import sys
import datetime
import random
import os.path   

hostname = "127.0.0.1:5000"
shutoff = False 

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
        if "백산" in name or "다원" in name:
            print(line, line[0][-1])
        job = "한국사회적기업진흥원 선정"  if line[0][-1] == "0" else "K-RE100 참여기업"

        tr.insert(name, job)
    file.close()

# 트라이에 데이터 삽입
trie_insert(os.path.join('data', 'data.csv'))

if os.path.isfile('exdata.csv'):
    trie_insert(os.path.join('exdata', 'exdata.csv'))
else : pass
# trie_insert(os.path.join('data', 'pro_name_data.csv'))
# trie_insert(os.path.join('data', 'pro_KRE_data.csv'))

# 유저스크립트 제공
@app.route('/gmarket-userscript.user.js')
def g_userscript():
    return get_file_or_empty("gmarket_highlighter.user.js").replace("$HOST", hostname)

@app.route('/coupang-userscript.user.js')
def c_userscript():
    return get_file_or_empty("coupang_highlighter.user.js").replace("$HOST", hostname)

@app.route('/11st-userscript.user.js')
def e_userscript():
    return get_file_or_empty("11st_highlighter.user.js").replace("$HOST", hostname)

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
    if serch is not None and not shutoff:
        return serch, 200
    elif not shutoff:
        return "NOP", 404
    else:
        return "NOP", 404
        

@app.route('/style.css')
def css():
    return get_file_or_empty("style.css")

tzinfo = datetime.timezone(datetime.timedelta(hours=+9.0)) # Korea is UTC+9:00

@app.route('/track/<vendor>', methods=['POST'])
def track(vendor):
    timestamp = datetime.datetime.now(tzinfo)
    ip = request.remote_addr

    is_social = tr.search(vendor)
    
    social = "0"
    if is_social:
        social = "1"

    with open("log.txt", "a") as f:
        f.write(f"[{timestamp}] {ip}: {social}, {shutoff}, {vendor}\n")

    return "Success!", 200

@app.route('/')
def index():
    return get_file_or_empty("index.html")
    
if __name__ == "__main__":
    if len(sys.argv) >= 2:
        hostname = sys.argv[1]
    if len(sys.argv) >= 3:
        shutoff = sys.argv[2] == "shutoff"
    
    from waitress import serve
    serve(app, host="0.0.0.0", port=5000)
    # app.run(port=5000)

