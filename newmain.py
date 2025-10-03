#this is student marks place enter your id number and name and it show your relut

#enter id
id = int(input('enter ID code:_ _ _ _ '))
# code number of student mean ID number
code_no = {
    101,
    102,
    103
}

# name dectionary
names ={
    1:'alisha',
    2:'shah',
    3:'chal'
}

# if id is var and if id have a codes to print this and else print bey 
if id in code_no:
    print("next name ")

# input user take a  name 
    name = input('enter your name:')
# id name names have a this input name to print this and else print no sir
    if name in names:
        print('oky this is your reulte!')
    
    else:
        print('no sir')
else:
    ("bey sir")
# subject of student
subjuct = {
    1:'english',
    2:'urdu',
    3:'math',
    4:'computer',
    5:'pst',
    6:'physics'
    }

# if user enter name and show relute
if name == names [1]:
    print(f'This is your marks and your resulte\n{subjuct[1]}:67\n{subjuct[2]}:50\n{subjuct[3]}:42\n{subjuct[4]}:99\n{subjuct[5]}:80\n{subjuct[6]}:60 \n your are all : pass✔') 

if name == names [2]:
    print(f'This is your marks and your resulte\n{subjuct[1]}:56\n{subjuct[2]}:80\n{subjuct[3]}:22\n{subjuct[4]}:59\n{subjuct[5]}:20\n{subjuct[6]}:90 \n your fail in one subject 😔\n pass') 

if name == names [3]:
    print(f'This is your marks and your resulte\n{subjuct[1]}:67\n{subjuct[2]}:55\n{subjuct[3]}:72\n{subjuct[4]}:49\n{subjuct[5]}:56\n{subjuct[6]}:75\n your are all :pass ✔ ') 