
import pandas as pd
import string



number = 13;

filename1 = "data/input/ehime_kiji_0{0}.csv".format(number)

filename2 = "data/output/train/midasi1-13/midasi_{0}.csv".format(number)
filename3 = "data/output/train/honbun1-13/honbun_{0}.csv".format(number)
filename4 = "data/output/train/youyaku1-13/youyaku_{0}.csv".format(number)

filename5 = "data/output/test/midasi1-13/midasi_{0}.csv".format(number)
filename6 = "data/output/test/honbun1-13/honbun_{0}.csv".format(number)

#　CSVファイル読み込み
df = pd.read_csv(filename1)

#　特定の列だけ抽出
df2 = df.loc[:,"midasi"]
df3 = df.loc[:,"honbun"]
df4 = df.loc[:,["midasi","honbun"]]


#　特定の行を削除
df4 = df4.query('not midasi.str.contains("病院")', engine='python')
df4 = df4[~df4['midasi'].str.contains("［")] 
df4 = df4[~df4['honbun'].str.contains("<")] 

#本文から改行文字を削除
df4["honbun"] = df4['honbun'].str.replace('\r\n',"")


# 閾値を設定してリード文がありそうな本文を分ける 閾値を仮に1200としてるので良い感じに変更すること
df5 = df4.query('honbun.str.len() <= 1200', engine='python' )
df6 = df4.query('honbun.str.len() > 1200', engine='python' )


# honbunの先頭3文を抽出
df5["youyaku"] = df5["honbun"].str.extract('(^.+?。.+?。.+?。)')

#空白行を削除
df5 = df5.dropna()


#　データを各カラム毎に分ける
df7 = df5.loc[:,"midasi"]
df8 = df5.loc[:,"honbun"]
df9 = df5.loc[:,"youyaku"]

df10 = df6.loc[:,"midasi"]
df11 = df6.loc[:,"honbun"]
#df12 = df6.loc[:,"youyaku"]



#　CSVファイル書き出し(インデックスなし)
df7.to_csv(filename2 , encoding="utf_8_sig", index = False)
df8.to_csv(filename3, encoding="utf_8_sig",index = False)
df9.to_csv(filename4, encoding="utf_8_sig" ,index = False)

df10.to_csv(filename5 , encoding="utf_8_sig", index = False)
df11.to_csv(filename6 , encoding="utf_8_sig",index = False)