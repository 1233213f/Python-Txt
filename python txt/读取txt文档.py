doc = "1.txt"
def main(doc):
    f = open(doc, 'r')

    a = f.readlines()

    a = [i.split(" ") for i in a]
    print(a)
# for line in a:  #打开文件
#
#     rs = line.rstrip('\n')

    for i in range(0, len(a)):
        a[i][10] = a[i][10].rstrip("\n")

    return a

print(main(doc))