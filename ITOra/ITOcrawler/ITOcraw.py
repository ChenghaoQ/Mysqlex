import requests,pickle,random,re,time
import IPpool


def get_a_proxy(pool):
        if pool[0]:
                proxy = {"http":"http://%s:%s"%(pool[0][0],pool[0][1])}
                print("切换到ip地址:%s"%pool[0][0])
        else:
                proxy = None
        del pool[0]        
        return proxy 


def companyCrawl():
        print("* * * * * Welcome to IT Citus Crawler * * * * *")
        pages = int(input("please enter the pages you want:"))
        proxypool = IPpool.ipCrawl()
        proxy = None
        #proxy = get_a_proxy(proxypool)
        headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}        
        compnum = 0
        #Please change the base url here
        companylist = []
        page = 1
        while page <= pages:
                urls = "http://www.itjuzi.com/company?page=%d"%page
                try:
                        request = requests.get(urls,headers = headers,proxies = proxy,timeout=10)
                        if request.status_code != 200:
                                raise ConnectError("Cannot connect to server") 
                        request.encoding = 'utf8'
                        buff = request.text
                        recomp = re.compile(r'<p class="title">.*?<span>(.+?)</span>.*?<p class="des"><span>(.+?)</span>.*?<a href=.*?>(.+?)</a>.*?<a href=.*?>(.+?)</a>.*?<i class="cell date">(.+?)</i>.*?<span class=.*?>(.+?)</span>',re.S)
                        complist = re.findall(recomp,buff) 

                except:
                        if proxypool:
                                proxy = get_a_proxy(proxypool)
                                
                        else:
                                proxypool = IPpool.ipCrawl()
                                proxypool.insert(0,None)
                                print(proxypool) 
                                proxy = get_a_proxy(proxypool)
                                time.sleep(60)
                        time.sleep(5)
                        continue
                                                
                for company in complist:
                        compform = [company[0]+'\n',company[1]+'\n',company[2]+'\t',company[3]+'\t',company[4].strip()+'\t','\t'+company[5]+'\n\n\n']
                        if compform in companylist:
                                continue
                        print("No.%d company info crawled"%compnum)
                        companylist.append(compform)
                        compnum += 1
                        for each in compform:
                                print(each)                        
                print('---------------Page %d finished ------------------'%page)
                page += 1
                sand = random.randint(1,3)
                time.sleep(sand)
        compdata = open("ITOcompany.pkl","wb")
        pickle.dump(companylist,compdata)

companyCrawl()
