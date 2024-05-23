# val = int(input('ne qeder kredit isteyirsiniz?: '))

# if val<2000:
#     print('2000nin altinda kredit verilmir')
# elif 2000 < val and val< 10000:
#     print('5faiz kredit vere bilirik')
# elif val<15000:
#     print('3faiz vere bilirik')
# else:
#     print('15000den yuxari kredit vermirik')

# val = 'ajfewlnfk'.i salpha()
# val = 'sijfj33efeij'.isnumeric()
# val = 'dfgnskjdfse4oj390efe'.isalnum()
# val = 'sdfhs/ə sjfw'.isascii()

# telebe = 'Sayyar'
# uni = 'BDU'
# kurs = 'IV'
# data = '{} {}-da {} kurs telebesidir'
# print(data.format(telebe,uni,kurs))

password = input('kodu daxil et: ')
if not len(password)>8 and len(password)<40:
    print('Ən az 8 və ən çox 40 characterdən ibarət olmalıdır')
elif not password.isascii():
    print('ancaq ingilis shriftlerinden istifade olunmalidir')
elif not password.isalnum():
    print('ancaq herf ve reqemden ibaret olmalidir')
elif password.isupper() or password.islower():
    print('Mütləq şəkildə ən az bir kicik ve bir boyuk herf olmalidir')
elif password.isalpha() and password.isalnum():
    print('en az bir herf ve bir reqem olmalidir')
else:
    print('Sifre qebul edildi')