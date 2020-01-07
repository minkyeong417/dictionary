file = input("Enter file:")
handle = open(file,'r')
address = dict()
for line in handle:
    if line.startswith('From '):
        linelst = line.split()
        address[linelst[1]] = address.get( linelst[1] , 0) + 1

bigadd = None
bigcount = None
for key in address:
    if bigcount is None or address[key] > bigcount:
        bigcount = address[key]
        bigadd = key
print(bigadd,bigcount)
