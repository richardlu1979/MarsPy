# -- coding: utf-8 --
# 进行回测，输入一个回测用的DateFrame,算出第1天上涨概率，第N天上涨概率
import tushare as  ts 
import pandas as pd


"""
   getOpenPrice得到一支股票在一个日期里面的开盘价或收盘价

   Args:
        stockname: 股票名
        sdate: 指定日期
        
    Returns:
        指定日期里面的股票的开盘价
        For example: 59

    Raises:
        IOError: An error occurred accessing the bigtable.Table object.
    """
def getOpenPrice(stockname,sdate,stype='o'):
    tmpDf = ts.get_k_data(stockname,start=sdate,end=sdate,ktype='D')
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
    
    stockK = ts.get_k_data('600036',start='2018-02-01',end='2018-02-01',ktype='D')
    a = getOpenPrice('600036','2018-02-01',stype='o')
    print(a)
    
    print(stockK)
    print(a)