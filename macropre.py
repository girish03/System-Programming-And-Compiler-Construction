import numpy as np
code=open('maccode.txt','r')
intcode=open('mpre/intcode.txt','w')
macrolist=open('mpre/macrolist.txt','w')
count=0
ind=0
for line in code:
    pline=line.replace(',',' ').split()
    if pline[0]=='MEND':
        count+=1
intcode=open('mpre/intcode.txt','a')
macrolist=open('mpre/macrolist.txt','a')
code=open('maccode.txt','r')
for line in code:
    pline=line.replace(',',' ').split()
    if pline[0]=='MEND':
        macrolist.write(line)
        count-=1
        continue
    if count>0:
        macrolist.write(line)
    if count==0:
        intcode.write(line)
intcode.close()
macrolist.close()
def getArgs(line):
    pline=line.replace(',',' ').split()
    for i in range(len(pline[1:])):
        alamname.append(pline[0])
        ala.append(pline[i+1])
        alaind.append(i+1)
    mnt.append(pline[0])
mnt=[]
mdt=[]
ala=[]
alamname=[]
alaind=[]
mntind=[]
index=0
mntflag=0
mdtflag=0
macrocode=open('mpre/macrolist.txt','r')
for line in macrocode:
    if 'MACRO' in line:
        mntflag=1
        mdtflag=1
        continue
    if mntflag==1:
        mntind.append(index+1)
        getArgs(line)
        mntflag=0
    if mdtflag==1:
        if 'MEND' in line:
            mdt.append(line.strip())
            mdtflag=0
            index+=1
            continue
        else:
            mdt.append(line.strip())
            index+=1
macrocode.close()
print('PASS - 1')
print('--------')
print('Intermediate source file generated by Pass-I')
print('--------------------------------------------\n')
a=open('mpre/intcode.txt','r')
for line in a:
    print(line)
print('Macro Name Table (MNT) created by Pass-I')
print('----------------------------------------\n')
print('Index\tMacro Name\tMDT Index\n')
for i in range(len(mnt)):
    print('',i+1,'\t',mnt[i],'\t\t',mntind[i])
print('Argument List Array (ALA) created by Pass-I')
print('----------------------------------------\n')
for i in range(len(mnt)):
    print('ALA : ',mnt[i])
    print('Index','\t\t','Argument')
    for j in range(len(ala)):
        if alamname[j]==mnt[i]:
            print(alaind[j],'\t\t',ala[j])
print('\nMacro Data Table (MDT) created by Pass-I')
print('----------------------------------------\n')
print('Index\t\tLine Data\n')
for i in range(len(mdt)):
    for j in range(len(ala)):
        if ala[j] in mdt[i]:
            if i==0 or mdt[i-1]=='MEND':
                continue
            else:
                mdt[i]=mdt[i].replace(ala[j],'#'+str(alaind[j]))
    print('',i+1,'\t\t',mdt[i])
def replace_macDef(line):
    index=0
    line=line.replace(',',' ').split()
    for j in range(len(mdt)):
        if line[0] in mdt[j]:
            index=j
    for j in range(index+1,len(mdt)):
        if mdt[j]=='MEND':
            break
        else:
            intline=mdt[j].replace(',',' ').split()
            for i in range(len(intline)):
                if '#' in intline[i]:
                    index=int(intline[i].replace('#',''))
                    intline[i]=line[index]
                    for x in intline:
                        print(x,'\t',end='')
                    for i in range(len(ala)):
                        if alamname[i]==line[0] and alaind[i]==index:
                            ala[i]=line[alaind[i]]
        print('\n')
flag=0
print('PASS-2')
print('Intermediate Code generated by Pass 2')
print('-------------------------------------\n')
a=open('mpre/intcode.txt','r')
for line in a:
    for i in range(len(mnt)):
        if mnt[i] in line:
            flag=1
            replace_macDef(line)
            break
    if flag==1:
        flag=0
        continue
    if flag==0:
        print(line)
print('Argument List Array (ALA) created by Pass-II')
print('--------------------------------------------\n')
for i in range(len(mnt)):
    print('ALA : ',mnt[i])
    print('Index','\t\t','Argument')
    for j in range(len(ala)):
        if alamname[j]==mnt[i]:
            print(alaind[j],'\t\t',ala[j])