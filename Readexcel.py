
# -*- coding: utf-8 -*-

import os
import xlrd
import glob
import xlwt
from numpy import *
import os
import sys
import xdrlib




def xls_merge(folder,header,filename):
     fileList = []
     for fileName in glob.glob(folder + "*.xls"):
         fileList.append(fileName)
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
     fileName = xlsxwriter.Workbook(folder + filename + ".xls")
     sheet = fileName.add_worksheet("merged")
     for i in range(len(header)):
         sheet.write(0,i,header[i])
     rowIndex = 1
     for fileIndex in range(fileNum):
         for j in range(len(matrix[fileIndex])):
             for colIndex in range (len(matrix[fileIndex][j])):
                 sheet.write(rowIndex,colIndex,matrix[fileIndex][j][colIndex])
             rowIndex += 1
     print("已完成%d個文檔的合併"%fileNum)
     fileName.close()
	fileName.save(output)
 
 xlsx_merge(file_location,header,output)
