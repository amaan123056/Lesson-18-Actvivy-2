import random
import time
def grd(sd,ed):
    print("random date between",sd,"and",ed)
    rg=random.random()
    df="%m/%d/%Y"
    st=time.mktime(time.strptime(sd,df))   
    et=time.mktime(time.strptime(ed,df))
    rt=st+rg*(et-st)
    rd=time.strftime(df,time.localtime(rt))
    return rd
print("random date is ",grd("1/1/2016","12/12/2018"))