import re
import pickle
import urllib.request

headers = {  
           'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}

def main():
	print("* * * * * Welcome to  Crawler * * * * * ")
	collegelist=[]	
	urls="http://rankings.betteredu.net/usnews/best-graduate-schools/top-engineering-schools/2017/eng-rankings.html"
	req = urllib.request.Request(urls,headers=headers)
	cont = urllib.request.urlopen(req)
	buf = cont.read().decode('utf-8')
	print(buf)
	recomp=re.compile(r'<tr>.*?<td>(.+?)</td>.*?<td>(.+?)</td>.*?<td>(.+?)</td>.*?<td>(.+?)</td>.*?<td>(.+?)</td>.*?</tr>',re.S)
	colllist=re.findall(recomp,buf)
	for coll in colllist:
		print(coll)
	a=open('EngineGrad.pkl','wb')
	pickle.dump(colllist,a)
	a.close()
main()


