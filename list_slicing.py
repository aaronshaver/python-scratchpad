l = [1, 2, 3, 4]

def pl(list_print, guess):
    print(str(list_print), "I thought it would be: " + str(guess))

pl(l[0:], '1234')
pl(l[1:], '234')
pl(l[-2:], '34')
pl(l[3:], '4')
pl(l[6:], '')
pl(l[:4], '1234')
pl(l[:-4], '')
pl(l[:-2], '12')
pl(l[:-1], '123')
pl(l[::2], '13')
pl(l[::3], '14')
pl(l[1:4:1], '234')
pl(l[::-1], '4321')

m = 'aaron'

pl(m[1:4], 'aro')
