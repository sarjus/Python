data = 'From sarju.s@sjcetpalai.ac.in Sat Jan 5 09:14:16 2008'
atpos = data.find('@')
print(atpos)
hostpos=data.find(' ',atpos)
print(data[atpos+1:hostpos])
