# ----------------------------
# 091 withステートメント
# 初めに__enter__() , 終わりに__exit__()してくれる。

# https://docs.python.org/ja/3/reference/datamodel.html?highlight=with#with-statement-context-managers

# ファイルopenをwithを使ってを行うと自動でcloseをしてくれる
# ----------------------------

# ファイルの指定をGUIで実施
# __file_daialog

# ファイル名
fileName = r"test.txt"

# close不要
with open(fileName, "w") as f:
    f.write("test\n")
