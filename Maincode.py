

def getindex(filelist):
#print(filelist)
    tar='.SUBCKT'
    tarend='.ENDS'
    sublist=[]
    endlist=[]
    for k in range(0,len(filelist)):#sublist&endlist
        lk=filelist[k]
        if tar in lk:
            sublist.append(k)
        if tarend in lk:
            endlist.append(k)
    return sublist,endlist
#print(len(endlist),endlist)
#print(len(sublist),sublist)


def defrange(sublist,endlist,filelist):
    inslist=[]
    for j in range(0,len(sublist)):#.sub~.end
        ins1=filelist[sublist[j]:endlist[j]+1]
        #print(ins1)
        inslist.append(ins1)
    #print(inslist)
    return inslist


def insdict(inslist,newfile):
    for i in range(0,len(inslist)):#build dict
        d={}
        li=inslist[i]
        key=li[0].split()[1]
        d[key]=[]
        for m in range(1,len(li)):#inslist
            lm=li[m]
            L1=lm.split()

            if L1!=[] and 'XI' in L1[0]:#判斷[]＝0 and XI in []
                inst=L1[-1]
            #print(L1[-1])
                if inst not in d[key]:
                    d[key].append(inst)


        newfile.write(str(d)+'\n')
    newfile.close()

def main():
    file=open('test.txt','r')
    newfile=open('result.txt', 'a')
    filestring=file.read().replace('\n+','')
    filelist=filestring.split('\n')

    sublist,endlist=getindex(filelist)
    print(sublist,endlist)

    inslist=defrange(sublist,endlist,filelist)
    print(inslist)

    insdict(inslist,newfile)


if __name__ == '__main__':
    main()
        




