
a = ['1','2','3','4','5','6','7','8','9']
b = ['q','w','e','r','t','y','u','i','o']
c = ['a','s','d','f','g','h','j','k','l']
h = [a,b,c]

wjm = '1.txt'

def mainw(wjm, h):
    file_handle = open(wjm, mode='w')


    for j in range(0, len(h)):

        for i in range(0, len(a)):
            if i == len(a)-1:
                file_handle.writelines([h[j][i] + '\n'])
            else:
                file_handle.writelines([h[j][i]+' '])

    file_handle.close()

mm = mainw(wjm, h)