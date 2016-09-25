import urllib.request,re

header = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}

def ipCrawl():
        print("哎呦，IP代理池空了，准备一些吧")
        proxylist = []
        page = 1
        while page <= 2:
                urls = "http://www.xicidaili.com/nn/%d"%page
        #        urls = "http://www.kuaidaili.com/proxylist/%d/"%page
                request = urllib.request.Request(urls,headers =header)
                content = urllib.request.urlopen(request)
                
                buff = content.read().decode('utf-8')
                print(buff)
                reprox = re.compile(r'<td class="country"><img.*?<td>(.+?)</td>.*?<td>(.+?)</td><td class.*?<td>(.+?)</td>.*?</tr>',re.S)
                #reprox = re.compile(r'<td data-title="IP">(.+?)</td>.*?<td data-title="PORT">(.+?)</td>.*?<td data-title="匿名度">(.+?)</td>.*?<td data-title="类型">(.+?)</td>.*?<td data-title="get/post支持">(.+?)</td>.*?<td data-title="位置">(.+?)</td>.*?<td data-title="响应速度">(.+?)</td>.*?<td data-title="最后验证时间">(.+?)</td>',re.S)
                proxlist = re.findall(reprox,buff)
                for prox in proxlist:
                        proxylist.append(prox)
                        for each in prox:
                                print(each)
                page+=1
        print("大量IP准备完毕")
        httplist = [httpprox for httpprox in proxylist if 'HTTPS' not in httpprox[3]]
        for each in httplist:
                for eac in each:
                        print(eac,end='\t')
                print("\n")  
        return httplist


ipCrawl()
