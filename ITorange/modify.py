import pickle
new_data=open('compdb.pkl','wb')
data_path=open('ITOcomp.pkl','rb')
complist=pickle.load(data_path)
for company in complist:
	for i in range(6):
		company[i]=company[i].strip()
pickle.dump(complist,new_data)
new_data.close()
data_path.close()
