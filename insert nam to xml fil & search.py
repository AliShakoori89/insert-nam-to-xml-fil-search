import xml.etree.ElementTree as ET
import os.path

print("choice your options:  ")
print("                         1. enter new name in to the list:  ")
print("                         2. search name :")
print("                         3. edit field :")
print('')
print('')
print('')
print('')
A=int(input("1. enter num 1 , 2 or 3 : "))

if A==1 :
    if os.path.isfile('list.xml'):
        root=ET.parse('list.xml').getroot()
    else:
        root = ET.Element('data')

    person = ET.Element('person')
    idnumber = str(input('enter id number:'))
    person.set('id',idnumber)
    name = ET.SubElement(person,'name').text=str(input("enter name: "))
    last_name = ET.SubElement(person,'last_name').text=str(input('enter lastname: '))
    birthday = ET.SubElement(person,'birthday').text=str(input('enter birthday: '))
    root.insert(1,person)
    mydata=ET.tostring(root)
    myfile=open('list.xml','wb')
    myfile.write(mydata)

elif A==2:
    tree=ET.parse('list.xml')
    root=tree.getroot()
    switches=['name','last_name','birthday']
    textsearch=str(input('enter id num for search : '))
    for elem in root:
        if elem.get('id')==textsearch:
            #print(elem.get('id'))
            for sub in elem:
                if sub.tag in switches:
                    print(sub.text)

elif A==3:
    tree=ET.parse('list.xml')
    root=tree.getroot()
    print('1. change id number: ')
    print('2. change name last name or birthday: ')
    B=int(input('enter choice 1 or 2 : '))
    if B==1:
        idnumber = str(input('enter id num for search : '))
        for elem in root.iter('person'):
            if elem.get('id')==idnumber:
                asd=str(input('enter new id : '))
                elem.set('id',asd)

                tree.write('list.xml')
    elif B==2:
        idnumber = str(input('enter id num for search : '))
        textfind=str(input('enter text: '))
        newtext=str(input('enter new text: '))
        for elem in root.iter('person'):
            if elem.get('id')==idnumber:
        #textfind=str(input('enter text: '))
                #for subelem in root.findall('person'):
                for sub in list(elem):
                    
                    if sub.text==textfind:
                        sub.text=newtext
                        tree.write('list.xml')
        