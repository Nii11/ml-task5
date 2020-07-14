# %%
import pandas as pd

# %%
import numpy as np


# %%
data=pd.read_csv('datafile.csv')

# %%
data


# %%
from sklearn.preprocessing import StandardScaler 

# %%
from sklearn.preprocessing import LabelEncoder , OneHotEncoder

# %%
I= data.iloc[: , :]

# %%
I = I.to_numpy()

# %%
label = LabelEncoder()

# %%
ip = label.fit_transform(I[:,0])

# %%
date=label.fit_transform(I[:,1])

# %%
error=label.fit_transform(I[:,2])

# %%
IP=pd.DataFrame(ip,columns=["IP"])

# %%
DATE=pd.DataFrame(date,columns=["TIME"])

# %%
ERR=pd.DataFrame(error,columns=["ERROR"])

# %%
ds=pd.concat([IP,DATE,ERR],axis=1)

# %%
st = StandardScaler()

# %%
data_new=st.fit_transform(ds)

# %%
from sklearn.cluster import KMeans

# %%
model=KMeans(n_clusters=3)

# %%
model.fit(data_new)

# %%
pred=model.fit_predict(data_new)

# %%
data_new=pd.DataFrame(data_new,columns=['IPS','DATE','ERROR'])

# %%
data_new['cluster name']=pred

# %%
IP_RS=pd.concat([data['ip'], ds['IP'],data[error], axis=1)

# %%
def CountFreq(ip_list,ip_label):
    freq={}
    for item in ip_list:
        if (item in freq) and (error !=200):
            freq[item]+=1
        else:
            freq[item]=1
        
    max_freq=0
    max_key=0
    for key,value in freq.items():
        if value > max_freq:
            max_freq=value
            max_ke=key
    return ip_label[ip_list.index(max_key)]

# %%
ip_r=CountFreq(IP_RS['IP'].tolist(),IP_RS['ip'].tolist(),IP_RS['error'].tolist())

# %%
rest=open("rest_ip.txt",'+a')
rest.write(ip_r)
rest.close()

# %%
