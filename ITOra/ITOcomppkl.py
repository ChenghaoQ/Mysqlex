import urllib.request
import re
import pickle
import time,random

headers = {
	'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
	}

'''
def compcrawl():
	compnum = 0
	print("* * * * * Welcome to IT Orange(company) Crawler * * * * * ")
	pages = int(input("Please enter the pages you want:"))
	companylist=[]
	for i in range(1,pages+1):
		urls="http://www.itjuzi.com/company?page=%d"%i
		request = urllib.request.Request(urls,headers = headers)
		content = urllib.request.urlopen(request)
		buff = content.read().decode('utf-8')
		recomp = re.compile(r'<p class="title">.*?<span>(.+?)</span>.*?<p class="des"><span>(.+?)</span>.*?<a href=.*?>(.+?)</a>.*?<a href=.*?>(.+?)</a>.*?<i class="cell date">(.+?)</i>.*?<span class=.*?>(.+?)</span>',re.S)
		complist = re.findall(recomp,buff)
		for company in complist:
			compform = [company[0]+'\n',company[1]+'\n',company[2]+'\t',company[3]+'\t',company[4].strip()+'\t','\t'+company[5]+'\n\n\n']
			print("No.%d company info crawled"%compnum)
			companylist.append(compform)
			compnum += 1
		
	compdata = open("ITOcompany.pkl",'wb')
	pickle.dump(companylist,compdata)
'''
def compcrawl():
	compnum = 0
	print("* * * * * Welcome to IT Orange(company) Crawler * * * * * ")
	pages = int(input("Please enter the pages you want:"))
	companylist=[]
	page=1
	while page<=pages:
		urls="http://www.itjuzi.com/company?page=%d"%page
		try:
			request = urllib.request.Request(urls,headers = headers)
			content = urllib.request.urlopen(request)
		except:
			if page<=pages:
				sand = random.randint(200,500)
				time.sleep(sand)
			else:
				break
		buff = content.read().decode('utf-8')
		recomp = re.compile(r'<p class="title">.*?<span>(.+?)</span>.*?<p class="des"><span>(.+?)</span>.*?<a href=.*?>(.+?)</a>.*?<a href=.*?>(.+?)</a>.*?<i class="cell date">(.+?)</i>.*?<span class=.*?>(.+?)</span>',re.S)
		complist = re.findall(recomp,buff)
		for company in complist:
			compform = [company[0]+'\n',company[1]+'\n',company[2]+'\t',company[3]+'\t',company[4].strip()+'\t','\t'+company[5]+'\n\n\n']
			print("No.%d company info crawled"%compnum)
			companylist.append(compform)
			compnum += 1
	
		print('------------Page %d finished------------------'%page)
		page+=1
		sand = random.randint(1,3)
		time.sleep(sand)

	compdata = open("ITOcompany.pkl",'wb')
	pickle.dump(companylist,compdata)

compcrawl()
