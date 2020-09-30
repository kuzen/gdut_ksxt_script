# 广工安全准入考试脚本

1秒100分！简单易用！  
适用平台：天津晟科思的考试平台


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
examination_no = 484
```

