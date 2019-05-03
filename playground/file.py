#
#
# open(path)


with open('/etc/hosts') as hosts:
    fileContent = hosts.read()
    print(fileContent)

    # end of file after last read
    print(hosts.tell())

print('closed ?' + str(hosts.closed))    

print('-' * 30)
with open('/etc/hosts') as hostFile:
    for line in hostFile:
        print(line.rsplit())

# mode: +, t (text), b (binary)
