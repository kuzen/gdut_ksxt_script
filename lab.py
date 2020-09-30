# -*- coding: utf-8 -*-

import requests
import time
import json
import time

# 修改这一个cookies
KSXTSESSID = 'ST-xxxxxx-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-xxxx-cas'
cookies = 'KSXTSESSID='+KSXTSESSID
examination_no = 484

header = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Connection": "keep-alive",
    "Cookie": cookies,
    "DNT": "1",
    "Host": "222.200.97.188",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"
}
post_url = 'http://222.200.97.188/gdut_ksxt/Center/Exam/endExam.html'
exam_url = 'http://222.200.97.188/gdut_ksxt/Center/Exam/beginExam.html?examination_no='+str(examination_no)

# http://222.200.97.188/gdut_ksxt/Center/Question/getQuestionDetail.html?question_no=205335
# answer_url = "http://222.200.97.188/gdut_ksxt/Center/Question/getQuestionDetail.html?question_no="
option_d = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
}

def getAnswer(sess, question_no):
    answer_url = "http://222.200.97.188/gdut_ksxt/Center/Question/getQuestionDetail.html?question_no=" + str(question_no)
    res = sess.get(answer_url) 
#     print(res.content.decode())
    res = json.loads(res.content.decode())
#     print(res)
    if res['data']['answer']=='正确':
        return  '"1"'
    elif res['data']['answer']=='错误':
        return '"0"'
    answer = []
    for o in res['data']['answer'].split(','):
        answer.append('"'+res['data']['question_result'][option_d[o]]['choice']+'"')
        
    return answer

def startAnswer(sess, paper):
    examination_no = paper['data']['exam']['examination_no']
    paper_no = paper['data']['exam']['paper_no']
    starttime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    post_data = {
        'examination_no': examination_no,
        'paper_no': paper_no,
        'starttime': starttime,
    }
    i = 0
    for list_no in (paper['data']['paper']['list']):
        question_no = paper['data']['paper']['list'][list_no]['question_no']
        ans = getAnswer(sess, question_no)
#         print(ans)
        post_data['answer['+str(i)+'][list_no]'] = list_no
        a = '['+ "".join(ans)+']'
        a = a.replace('""','","')
        post_data['answer['+str(i)+'][answer]'] = a
        i = i + 1
    return post_data

def getPaper(sess):
    res = sess.get(exam_url)
    res = json.loads(res.content.decode())
    return res

sess = requests.Session()
sess.headers = header
paper = getPaper(sess)
# print(paper)
post_data = startAnswer(sess, paper)
ret = sess.post(post_url, post_data)
print(ret.content.decode())