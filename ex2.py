import numpy as np
import sklearn.svm as svm
xx,yy=open('train_sample.txt','r'),open('train_sample_label.txt','r')
s_data=np.array(list(map(lambda x:list(map(lambda x:float(x),x.strip().split())),xx.readlines())))
s_label=np.array(list(map(lambda x:int(x.strip()),yy.readlines())))
xx.close();yy.close()
bord=svm.LinearSVC()
bord.fit(s_data,s_label)
xx,yy=open('test_sample.txt','r'),open('test_sample_label.txt','r')
t_data=np.array(list(map(lambda x:list(map(lambda x:float(x),x.strip().split())),xx.readlines())))
t_label=np.array(list(map(lambda x:int(x.strip()),yy.readlines())))
xx.close();yy.close()
t_otc=((t_data.dot(bord.coef_.T)+bord.intercept_)>0).T
print(t_otc)
print('准确率=',(t_otc==t_label).sum()/len(t_label),sep='')
print('查全率=',(t_otc&t_label).sum()/(t_label==1).sum(),sep='')