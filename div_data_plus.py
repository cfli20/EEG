import shutil
import os
import datetime
import random

# path='/home/lcf/Desktop/LCF_txtdata-2021-7/Esentense/Have a nice weekday/listen/'
# path='/home/lcf/Desktop/LCF_txtdata-2021-7/句子/周末愉快/listen/'

category = 'Ephrase/Ephrase-think/Ephrase-6-2-7'   #listen  think    speak    Ephrase/Ephrase-think/Ephrase-5-2-7
path='/home/lcf/Desktop/12/'
test_path='/home/lcf/Desktop/TBME/'+category+'/test/'
train_path='/home/lcf/Desktop/TBME/'+category+'/train/'
val_path='/home/lcf/Desktop/TBME/'+category+'/val/'
list_path='/home/lcf/Desktop/TBME/'+category+'/'
txt_path ='/home/lcf/Desktop/TBME/'+category+'/'

txt_name='all_channles'


# name = ['你','去','天','头','来','水','说']
# name = ['chair','come','cup','go','sit','stand','water']
# name=['apple','book','come','cup','go','head','stand','water','you']
# name = ['go out','close the window','good morning','happy birthday','open the door','pick up','sit down','slow down','stand up']

# name = ['have a nice weekday','How is the weather today','I have a lot of problems','It is time to get up','long time no see',
#              'please call me before you come','you win some ,you lose some']
#train
train_file_names=[]
for filename in os.listdir(train_path):
    train_file_names.append(filename)
# print(len(train_file_names))
random.shuffle(train_file_names)

test_file_names=[]
for filename in os.listdir(test_path):
    test_file_names.append(filename)
# print(len(train_file_names))
random.shuffle(test_file_names)
# with open(txt_path+'{}.txt'.format(txt_name),'w') as f:
#     for name in train_file_names :
#         if name.find('chair')!=-1:
#             f.write(name+'    '+'train'+'    '+'0'+'\n')
#         elif name.find('come')!=-1:
#             f.write(name + '    ' + 'train' + '    ' + '1' + '\n')
#         elif name.find('cup')!=-1:
#             f.write(name + '    ' + 'train' + '    ' + '2' + '\n')
#         elif name.find('go')!=-1:
#             f.write(name + '    ' + 'train' + '    ' + '3' + '\n')
#         elif name.find('sit')!=-1:
#             f.write(name + '    ' + 'train' + '    ' + '4' + '\n')
#         elif name.find('stand')!=-1:
#             f.write(name + '    ' + 'train' + '    ' + '5' + '\n')
#
#         else:
#             f.write(name + '    ' + 'train' + '    ' + '6' + '\n')
#
#
#     for name in test_file_names :
#         if name.find('chair')!=-1:
#             f.write(name+'    '+'test'+'    '+'0'+'\n')
#         elif name.find('come')!=-1:
#             f.write(name + '    ' + 'test' + '    ' + '1' + '\n')
#         elif name.find('cup')!=-1:
#             f.write(name + '    ' + 'test' + '    ' + '2' + '\n')
#         elif name.find('go')!=-1:
#             f.write(name + '    ' + 'test' + '    ' + '3' + '\n')
#         elif name.find('sit')!=-1:
#             f.write(name + '    ' + 'test' + '    ' + '4' + '\n')
#
#         elif name.find('stand')!=-1:
#             f.write(name + '    ' + 'test' + '    ' + '5' + '\n')
#
#         else:
#             f.write(name + '    ' + 'test' + '    ' + '6' + '\n')


# with open(txt_path+'{}.txt'.format(txt_name),'w') as f:
#     for name in train_file_names :
#         if name.find('你')!=-1:
#             f.write(name+'    '+'train'+'    '+'0'+'\n')
#         elif name.find('去')!=-1:
#             f.write(name + '    ' + 'train' + '    ' + '1' + '\n')
#         elif name.find('天')!=-1:
#             f.write(name + '    ' + 'train' + '    ' + '2' + '\n')
#         elif name.find('头')!=-1:
#             f.write(name + '    ' + 'train' + '    ' + '3' + '\n')
#         elif name.find('来')!=-1:
#             f.write(name + '    ' + 'train' + '    ' + '4' + '\n')
#         elif name.find('水')!=-1:
#             f.write(name + '    ' + 'train' + '    ' + '5' + '\n')
#
#         else:
#             f.write(name + '    ' + 'train' + '    ' + '6' + '\n')
#
#
#     for name in test_file_names :
#         if name.find('你')!=-1:
#             f.write(name+'    '+'test'+'    '+'0'+'\n')
#         elif name.find('去')!=-1:
#             f.write(name + '    ' + 'test' + '    ' + '1' + '\n')
#         elif name.find('天')!=-1:
#             f.write(name + '    ' + 'test' + '    ' + '2' + '\n')
#         elif name.find('头')!=-1:
#             f.write(name + '    ' + 'test' + '    ' + '3' + '\n')
#         elif name.find('来')!=-1:
#             f.write(name + '    ' + 'test' + '    ' + '4' + '\n')
#
#         elif name.find('水')!=-1:
#             f.write(name + '    ' + 'test' + '    ' + '5' + '\n')
#
#         else:
#             f.write(name + '    ' + 'test' + '    ' + '6' + '\n')



#
# with open(txt_path+'{}.txt'.format(txt_name),'w') as f:
#     for name in train_file_names :
#         if name.find('apple')!=-1:
#             f.write(name+'    '+'train'+'    '+'0'+'\n')
#         elif name.find('book')!=-1:
#             f.write(name + '    ' + 'train' + '    ' + '1' + '\n')
#         elif name.find('come')!=-1:
#             f.write(name + '    ' + 'train' + '    ' + '2' + '\n')
#         elif name.find('cup')!=-1:
#             f.write(name + '    ' + 'train' + '    ' + '3' + '\n')
#         elif name.find('go')!=-1:
#             f.write(name + '    ' + 'train' + '    ' + '4' + '\n')
#         elif name.find('head')!=-1:
#             f.write(name + '    ' + 'train' + '    ' + '5' + '\n')
#         elif name.find('stand')!=-1:
#             f.write(name + '    ' + 'train' + '    ' + '6' + '\n')
#         elif name.find('water')!=-1:
#             f.write(name + '    ' + 'train' + '    ' + '7' + '\n')
#         else:
#             f.write(name + '    ' + 'train' + '    ' + '8' + '\n')
#
#
#     for name in test_file_names :
#         if name.find('apple')!=-1:
#             f.write(name+'    '+'test'+'    '+'0'+'\n')
#         elif name.find('book')!=-1:
#             f.write(name + '    ' + 'test' + '    ' + '1' + '\n')
#         elif name.find('come')!=-1:
#             f.write(name + '    ' + 'test' + '    ' + '2' + '\n')
#         elif name.find('cup')!=-1:
#             f.write(name + '    ' + 'test' + '    ' + '3' + '\n')
#         elif name.find('go')!=-1:
#             f.write(name + '    ' + 'test' + '    ' + '4' + '\n')
#         elif name.find('head')!=-1:
#             f.write(name + '    ' + 'test' + '    ' + '5' + '\n')
#         elif name.find('stand')!=-1:
#             f.write(name + '    ' + 'test' + '    ' + '6' + '\n')
#         elif name.find('water')!=-1:
#             f.write(name + '    ' + 'test' + '    ' + '7' + '\n')
#         else:
#             f.write(name + '    ' + 'test' + '    ' + '8' + '\n')

# #
with open(txt_path+'{}.txt'.format(txt_name),'w') as f:
    for name in train_file_names :
        if name.find('close the window')!=-1:
            f.write(name+'    '+'train'+'    '+'0'+'\n')
        elif name.find('good mornig')!=-1:
            f.write(name + '    ' + 'train' + '    ' + '1' + '\n')
        elif name.find('go out')!=-1:
            f.write(name + '    ' + 'train' + '    ' + '2' + '\n')
        elif name.find('happy birthday')!=-1:
            f.write(name + '    ' + 'train' + '    ' + '3' + '\n')
        elif name.find('open the door')!=-1:
            f.write(name + '    ' + 'train' + '    ' + '4' + '\n')
        elif name.find('pick up')!=-1:
            f.write(name + '    ' + 'train' + '    ' + '5' + '\n')
        elif name.find('sit down')!=-1:
            f.write(name + '    ' + 'train' + '    ' + '6' + '\n')
        elif name.find('slow down')!=-1:
            f.write(name + '    ' + 'train' + '    ' + '7' + '\n')
        else:
            f.write(name + '    ' + 'train' + '    ' + '8' + '\n')


    for name in test_file_names :
        if name.find('close the window')!=-1:
            f.write(name+'    '+'test'+'    '+'0'+'\n')
        elif name.find('good moring')!=-1:
            f.write(name + '    ' + 'test' + '    ' + '1' + '\n')
        elif name.find('go out')!=-1:
            f.write(name + '    ' + 'test' + '    ' + '2' + '\n')
        elif name.find('happy birthday')!=-1:
            f.write(name + '    ' + 'test' + '    ' + '3' + '\n')
        elif name.find('open the door')!=-1:
            f.write(name + '    ' + 'test' + '    ' + '4' + '\n')
        elif name.find('pick up')!=-1:
            f.write(name + '    ' + 'test' + '    ' + '5' + '\n')
        elif name.find('sit down')!=-1:
            f.write(name + '    ' + 'test' + '    ' + '6' + '\n')
        elif name.find('slow down')!=-1:
            f.write(name + '    ' + 'test' + '    ' + '7' + '\n')
        else:
            f.write(name + '    ' + 'test' + '    ' + '8' + '\n')




#
#
# with open(txt_path+'{}.txt'.format(txt_name),'w') as f:
#     for name in train_file_names :
#         if name.find('come')!=-1:
#             f.write(name+'    '+'train'+'    '+'0'+'\n')
#         elif name.find('head')!=-1:
#             f.write(name + '    ' + 'train' + '    ' + '1' + '\n')
#         elif name.find('water')!=-1:
#             f.write(name + '    ' + 'train' + '    ' + '2' + '\n')
#
#         else:
#             f.write(name + '    ' + 'train' + '    ' + '3' + '\n')
#
#
#     for name in test_file_names :
#         if name.find('来')!=-1:
#             f.write(name+'    '+'test'+'    '+'0'+'\n')
#         elif name.find('头')!=-1:
#             f.write(name + '    ' + 'test' + '    ' + '1' + '\n')
#         elif name.find('水')!=-1:
#             f.write(name + '    ' + 'test' + '    ' + '2' + '\n')
#
#         else:
#             f.write(name + '    ' + 'test' + '    ' + '3' + '\n')



# with open(txt_path+'{}.txt'.format(txt_name),'w') as f:
#     for name in train_file_names :
#         if name.find('have a nice')!=-1:
#             f.write(name+'    '+'train'+'    '+'0'+'\n')
#         elif name.find('How is the weather')!=-1:
#             f.write(name + '    ' + 'train' + '    ' + '1' + '\n')
#         elif name.find('I have a lot')!=-1:
#             f.write(name + '    ' + 'train' + '    ' + '2' + '\n')
#         elif name.find('It is time to')!=-1:
#             f.write(name + '    ' + 'train' + '    ' + '3' + '\n')
#         elif name.find('long time no')!=-1:
#             f.write(name + '    ' + 'train' + '    ' + '4' + '\n')
#         elif name.find('please call me')!=-1:
#             f.write(name + '    ' + 'train' + '    ' + '5' + '\n')
#         # elif name.find('you win some')!=-1:
#         #     f.write(name + '    ' + 'train' + '    ' + '6' + '\n')
#         # elif name.find('water')!=-1:
#         #     f.write(name + '    ' + 'train' + '    ' + '7' + '\n')
#         else:
#             f.write(name + '    ' + 'train' + '    ' + '6' + '\n')
#
#
#     for name in test_file_names :
#         if name.find('have a nice')!=-1:
#             f.write(name+'    '+'test'+'    '+'0'+'\n')
#         elif name.find('How is the weather')!=-1:
#             f.write(name + '    ' + 'test' + '    ' + '1' + '\n')
#         elif name.find('I have a lot')!=-1:
#             f.write(name + '    ' + 'test' + '    ' + '2' + '\n')
#         elif name.find('It is time to')!=-1:
#             f.write(name + '    ' + 'test' + '    ' + '3' + '\n')
#         elif name.find('long time no')!=-1:
#             f.write(name + '    ' + 'test' + '    ' + '4' + '\n')
#         elif name.find('please call me')!=-1:
#             f.write(name + '    ' + 'test' + '    ' + '5' + '\n')
#         # elif name.find('stand')!=-1:
#         #     f.write(name + '    ' + 'test' + '    ' + '6' + '\n')
#         # elif name.find('water')!=-1:
#         #     f.write(name + '    ' + 'test' + '    ' + '7' + '\n')
#         else:
#             f.write(name + '    ' + 'test' + '    ' + '6' + '\n')

