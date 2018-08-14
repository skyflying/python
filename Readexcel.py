
# -*- coding: utf-8 -*-

import os
import xlrd
import glob
import xlwt
from numpy import *
import os
import sys
# 指定要列出所有檔案的目錄
mypath = "D:\data"

# 遞迴列出所有子目錄與檔案
fileList = []
#for root, dirs, files in walk(mypath+ "*.xls"):
  #print("路徑：", root)
  #print("  目錄：", dirs)
  #print("  檔案：", files)


for fileName in glob.glob('D:\data\*\*.xls'):
     fileList.append(fileName)
print("在目錄下下有%d個xls文件" %len(fileList))
  
  
fileNum = len(fileList)
matrix = [None] * fileNum


for i in range(fileNum):
     fileName = fileList[i]
     workBook = xlrd.open_workbook(fileName)
     try:
         sheet = workBook.sheet_by_index(0)
     except Exception as e:
         print(e)
     nRows = sheet.nrows
     matrix[i] = [0]*(nRows - 1)
     nCols = sheet.ncols
     for m in range(nRows - 1):
         matrix[i][m] = ["0"]* nCols
     for j in range(1,nRows):
         for k in range(nCols):
             matrix[i][j-1][k] = sheet.cell(j,k).value
fileName = xlwt.Workbook()
sheet = fileName.add_sheet("combine")
for i in range(len(header)):
     sheet.write(0,i,header[i])
rowIndex = 1
for fileIndex in range(fileNum):
     for j in range(len(matrix[fileIndex])):
         for colIndex in range (len(matrix[fileIndex][j])):
             sheet.write(rowIndex,colIndex,matrix[fileIndex][j][colIndex])
         rowIndex += 1
print("已將%d個文件合併"%fileNum)
fileName.save(mypath + date + ".xls")
