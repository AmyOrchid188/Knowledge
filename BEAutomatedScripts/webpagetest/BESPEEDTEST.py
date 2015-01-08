# -*- coding: utf-8 -*- 
import  xdrlib ,sys
import xlrd
import xlwt

def open_excel(file):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception,e:
        print str(e)

#根据名称获取Excel表格中的数据   参数:file：Excel文件路径     colnameindex：表头列名所在行的索引，by_name：Sheet1名称
def get_rows_cols_count_from_excel(file= 'D:\\be\\webpagetest\\testurl.xls',by_name=u'Sheet1'):
    data = open_excel(file)
    table = data.sheet_by_name(by_name)
    return table
  
def get_url_from_excel():
    table = get_rows_cols_count_from_excel()
    nrows = table.nrows #行数 
#    print nrows
    list =[]
    for rownum in range(1,nrows):
        URL = table.cell(rownum,1).value
        list.append(URL)
    return list


