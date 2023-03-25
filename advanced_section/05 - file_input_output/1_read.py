stream = open('demo.txt', 'r')

print('\nIs this readable?' + str(stream.readable()))
# print('\nRead one character?' + stream.read(1))
# print('\nRead to end of line?' + stream.readline())
print('\nRead all lines:\n' + str(stream.readlines()))
# print(stream)