import urllib.request
import re

headers = {  
           'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'  
        } 
def main():
	j=0
	f = open("ITOcompany.md",'w')
	f.close()
	f = open("ITOcompany.md",'a')
	print("* * * * * Welcome to IT Orange(company) Crawler * * * * * ")
	amount=int(input("Please enter the pages you want:"))
	
	for i in range(1,amount+1):
		urls="http://www.itjuzi.com/company?page=%d"%i
		req = urllib.request.Request(urls,headers=headers)
		cont = urllib.request.urlopen(req)
		buf = cont.read().decode('utf-8')
		recomp = re.compile(r'<i class="cell maincell">.*?<p class="title">.*?<span>(.+?)</span>.*?<p class="des"><span>(.+?)</span>.*?<span class="tags.*?<a href.*?>(.+?)</a>.*?<span class="loca.*?<a href=.*?>(.+?)</a>.*?<i class="cell date">(.+?)</i>.*?<i class="cell round">.*?<span class.*?>(.+?)</span>',re.S)
		complist = re.findall(recomp,buf)
		for company in complist:
			form = [company[0]+'\n',company[1]+'\n',company[2]+'\t',company[3]+'\t',company[4].strip()+'\t','\t'+company[5]+'\n\n\n']

			print("No.%d company info crawled"%j)
			f.writelines(form)
			j+=1
main()
