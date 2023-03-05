doc = "1.txt"
def main(doc):
    f = open(doc, 'r')
    a = f.readlines()
    a = [i.split(" ") for i in a]
    for i in range(0, len(a)):
        a[i][10] = a[i][10].rstrip("\n")
    return a
# print(len(main(doc)))
n1=645
n2=11
data = [[] for _ in range(n1)]
list = [[] for _ in range(n2)]

for column in range(1, n1+1):
    for row in range(1, n2+1):
        list[row-1] = '0
    data[column-1]=list
    list = [[] for _ in range(n2)]
print(data)

wjm = '2.txt'
def mainw(wjm, h):
    file_handle = open(wjm, mode='w')
    for j in range(0, len(h)):
        for i in range(0, 7):


            file_handle.writelines([h[j][i] + ' '])
        file_handle.writelines([data[j][10] + ' '])
        file_handle.writelines([data[j][9] + ' '])
        file_handle.writelines([data[j][8] + ' '])
        file_handle.writelines([data[j][7] + '\n'])

            # print(h[0][i])

    file_handle.close()

# print(mainw(wjm,main(doc)))
mm = mainw(wjm, main(doc))