val = int(input('ne qeder kredit isteyirsiniz?: '))

if val<2000:
    print('2000nin altinda kredit verilmir')
elif 2000 < val and val< 10000:
    print('5faiz kredit vere bilirik')
elif val<15000:
    print('3faiz vere bilirik')
else:
    print('15000den yuxari kredit vermirik')