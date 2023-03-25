out = open('write.txt', 'wt')

print('\nCan I write this file?' + str(out.writable()))

# out.write('H')
stream = open('demo.txt', 'r')
alllines = stream.readlines()

out.write('Add a new line\n')

out.writelines(alllines)

out.close()