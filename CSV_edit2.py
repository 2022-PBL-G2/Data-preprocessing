
import pandas as pd
import string



#　CSVファイル読み込み

df = pd.read_csv("./data/input/test_honbun.csv")

dfa = pd.read_csv("./data/input/midasi1-13/midasi_01.csv")
df1 = pd.read_csv("./data/input/midasi1-13/midasi_02.csv")
df2 = pd.read_csv("./data/input/midasi1-13/midasi_02.csv")
df3 = pd.read_csv("./data/input/midasi1-13/midasi_03.csv")
df4 = pd.read_csv("./data/input/midasi1-13/midasi_04.csv")
df5 = pd.read_csv("./data/input/midasi1-13/midasi_05.csv")
df6 = pd.read_csv("./data/input/midasi1-13/midasi_06.csv")
df7 = pd.read_csv("./data/input/midasi1-13/midasi_07.csv")
df8 = pd.read_csv("./data/input/midasi1-13/midasi_08.csv")
df9 = pd.read_csv("./data/input/midasi1-13/midasi_09.csv")
df10 = pd.read_csv("./data/input/midasi1-13/midasi_10.csv")
df11 = pd.read_csv("./data/input/midasi1-13/midasi_11.csv")
df12 = pd.read_csv("./data/input/midasi1-13/midasi_12.csv")
df13 = pd.read_csv("./data/input/midasi1-13/midasi_13.csv")
df14 = pd.read_csv("./data/input/midasi1-13/test_midasi.csv")


df_concat = pd.concat([dfa,df2,df3,df4,df5,df6,df7,df8,df9,df10,df11,df12,df13,df14])


df["midashi"] = df_concat



#　特定の行を削除
df = df.query('not honbun.str.contains("名簿の見方")', engine='python')
df = df[~df['honbun'].str.contains("［")] 
df = df[~df['honbun'].str.contains("<")] 
df = df[~df['honbun'].str.contains("旧任")]

#本文から改行文字を削除
df["honbun"] = df['honbun'].str.replace('\r\n',"")


# honbunの先頭3文を抽出
df["youyaku"] = df["honbun"].str.extract('(^.+?。.+?。.+?。)')

#空白行を削除
df = df.dropna()

dfA = df.loc[:,"honbun"]
dfB = df.loc[:,"youyaku"]
dfC = df.loc[:,"midashi"]



#　CSVファイル書き出し(インデックスなし)
dfA.to_csv("./data/output/test/test_honbun.csv", encoding="utf_8_sig", index = False)
dfB.to_csv("./data/output/test/test_youyaku.csv", encoding="utf_8_sig",index = False)
dfC.to_csv("./data/output/test/test_midashi.csv", encoding="utf_8_sig",index = False)



