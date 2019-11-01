import urllib3
import re
http = urllib3.PoolManager()
urllib3.disable_warnings()
url = "https://edu.csdn.net/course/detail/"
i = 10000
for i in range(i,10100):
    data = http.request('get',"https://edu.csdn.net/course/detail/"+str(i)).data.decode()
    pat = 'class="mr10" target="_blank">(.*?)</a>'
    result = re.findall(pat,data)
    print(result)
    print(i)
