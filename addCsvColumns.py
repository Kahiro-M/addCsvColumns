import pathlib
import pandas as pd
import sys

def addCsvColumns(inputFile,addColumnsName,addColumnsData):
    outputFile = inputFile.rsplit('.', 1)[0] + '_add.csv'
    tmpDf = pd.read_csv(inputFile)
    tmpDf[addColumnsName] = addColumnsData
    tmpDf.fillna('').replace('nan','').to_csv(outputFile,encoding="utf_8_sig",index=False)


if __name__ == '__main__':
    if(len(sys.argv)<4):
        # 使用例
        inputFile = input("追加したいファイルのパスを入力してください: ")
        addColumnsName = input("追加したいカラム名を入力してください: ")
        addColumnsData = input("追加したいデータを入力してください: ")
    else:
        inputFile = sys.argv[1]
        addColumnsName = sys.argv[2]
        addColumnsData = sys.argv[3]

    addCsvColumns(inputFile,addColumnsName,addColumnsData)
