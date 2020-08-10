flist = ['result0000.txt','result0001.txt','result0002.txt','result0003.txt','result0004.txt','result0005.txt']
ofile = open('result.txt','w')
for fr in flist:
    for txt in open(fr,'r'):
        ofile.write(txt)
ofile.close()

#注意：所有文件必须是txt格式的，如果不是，就打开后另存为txt