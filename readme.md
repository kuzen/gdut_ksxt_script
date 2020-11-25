# 广工安全准入考试脚本

1秒100分！简单易用！  
适用平台：天津晟科思的考试平台  
适合考试：2020年秋季自动化学院实验室安全准入考试（考试代号484）
         2020年‘广电杯’校园安全知识暨创意设计大赛活动的通知(考试代号545)
         理论上全考试通用


测试平台：python 3.8, requests, json


# 使用方法

chrome登陆考试平台，f12打开开发者工具，在application中找到cookies,找到KSXTSESSID，复制这个值

修改lab.py文件第九行,改为你的值
```
KSXTSESSID = 'ST-xxxxxx-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx-xxxx-cas'
```
最后
```
python lab.py
```
体验1秒100分的快感吧

# 同平台其他考试
理论上来说只需要修改lab.py文件第11行即可
```
examination_no = 484  #484 是 2020年秋季自动化学院实验室安全准入考试
```

