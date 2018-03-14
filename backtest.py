# -- coding: utf-8 --

# 进行回测，输入一个回测用的DateFrame,算出第1天上涨概率，第N天上涨概率
import tushare as  ts 
import pandas as pd
import datetime
import time


"""
   getPriceByStep得到一支股票在一个指定开始日期后step个日子后的开盘价或收盘价
   
   Args:
        stockname: 股票名
        beginday: 指定开始日期
        step:从开始日期后的天数,0是第一条，step+1条
        stype: 价格类型 o 开盘价  c 收盘价  h 最高价 l 最低价
        
    Returns:
        指定日期里面的股票的开盘价
        For example: 59
        如果该时间内没价格价格为 0

    Raises:
        IOError: An error occurred accessing the bigtable.Table object.
    """
def getPriceByStep(stockname,beginday,step=0,stype='o'):
    #算法：从得到begindate对应的记录后，向后读取step条记录
    Df = ts.get_k_data(stockname,start=beginday,ktype='D')
    tmpDf = Df[step:step+1]
    

    if stype == 'o':
        if tmpDf.iloc[:,0].size > 0 :
            return tmpDf.values[0][1]
        
    elif stype == 'c':
        if tmpDf.iloc[:,0].size > 0 :
            return tmpDf.values[0][2]
        
    elif stype == 'h':
        if tmpDf.iloc[:,0].size > 0 :
            return tmpDf.values[0][3]
        
    elif stype == 'l':
        if tmpDf.iloc[:,0].size > 0 :
            return tmpDf.values[0][4]
        
    else:
        return 0

    



#main函数

if __name__ == "__main__":

    #此处
    dfcomment = pd.DataFrame([['2018-02-01','600028'],
                             ['2018-02-03','000028'],
                             ['2018-02-11','300028']],columns=['enterdate','stockname'])  
    
    stockK = ts.get_k_data('600036',start='2018-02-01',end='2018-02-15',ktype='D')
    a = getPriceByStep('600036','2018-02-01',3,stype='o')
    print(a)
    #print(stockK)
    
    print('===================')

    #遍历dfcomment
    for indexs in dfcomment.index:
        print(dfcomment[indexs:indexs+1].values[0][1])
    #print(stockK[0:1])
    
    