import urllib.request
import re
import pickle
headers = {  
           'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'  
        } 

def main():
	data=open('3dlot.pkl','wb')
	amount = int(input("Please enter the pages:"))
	lotlot =[]
	for i in range(1,amount+1):
		urls='http://kaijiang.ssqzj.com/3d/index.php?topage=%s'%str(i)
		req=urllib.request.Request(urls,headers=headers)
		cont = urllib.request.urlopen(req)
		buf = cont.read().decode('GBK')
		recomp=re.compile(r'<td class="qihao">(.+?)</td>.*?<td class="time">(.+?)</td>.*?<input type="button" value=(.+?)class=.*?value=(.+?)class.*?value=(.+?)class.*?<td class="t_center">(.+?)</td>.*?<td class="t_center">(.+?)</td>.*?<td class="t_center">(.+?)</td>.*?<td class="t_center">(.+?)</td>.*?<td class="t_center">',re.S)
		lotlist=re.findall(recomp,buf)
		for lot in lotlist:
			form=[lot[0],lot[1],lot[2]+lot[3]+lot[4],lot[5],lot[6],lot[7],lot[8]]
			lotlot.append(form)
			print(form)	
	pickle.dump(lotlot,data)
	data.close()	

main()
