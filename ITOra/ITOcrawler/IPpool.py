import urllib.request,re

header = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}

def ipCrawl():
	proxylist = []
	page = 1
	while page <= 5:
		urls = "http://www.kuaidaili.com/proxylist/%d/"%page
		print('123')
		request = urllib.request.Request(urls,headers =header)
		content = urllib.request.urlopen(request)
		print(content)
 
		buff = content.read().decode('utf-8')
		reprox = re.compile(r'<td data-title="IP">(.+?)</td>.*?<td data-title="PORT">(.+?)</td>.*?<td data-title="匿名度">(.+?)</td>.*?<td data-title="类型">(.+?)</td>.*?<td data-title="get/post支持">(.+?)</td>.*?<td data-title="位置">(.+?)</td>.*?<td data-title="响应速度">(.+?)</td>.*?<td data-title="最后验证时间">(.+?)</td>',re.S)
		proxlist = re.findall(reprox,buff)
		for prox in proxlist:
			print(prox)	
			proxylist.append(prox)
		page+=1
	return proxylist	
