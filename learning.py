# Function هيا نفسها الدالة وتعني وظيفة ويمكنك انشاء دالة خاصة بك واستعمالها في اي مكان في البرنامج

# المتغيرات varibles هي عبارة عن مكان لتخزين البيانات مثل النصوص والأرقام

# string هي عبارة عن نصوص يمكن تخزينها في المتغيرات

# integer هي عبارة عن أرقام صحيحة يمكن تخزينها في المتغيرات


# float هي عبارة عن أرقام عشرية يمكن تخزينها في المتغيرات

# هاذه المتغيرات عادية وكيفية كباعتها
# name="yassin"
# print("hello " + name + " your number phone is " + namberphone)

# يعطيك قيمة الموجودة في المتغير مثل نص أو عدد صحيح أو اي قيمة اخرى
# s = "yassin"
# print(type(s))

# len تعطيك عدد الأحرف الموجودة في المتغير
# y="hello world iam yassin iam 25 yours ould "
# print(len(y))


# upper يحول جميع الأحرف الى حروف كبيرة
# x="hello"
# x.upper()
# print(x.upper())

# lower يحول جميع الأحرف الى حروف صغيرة
# x="HELLO"
# x.lower()
# print(x.lower())

# تفيد دالة format في تحويل المنغيرات الى نصوص و يمكن طباعتها معا
# f= 34
# print("hello " + format(f))

# replace هي عبارة عن دالة تقوم باستبدال نصوص معينة في المتغيرات
# r= "hi yasine how are you"
# print(r.replace("y" ,"t"))

# t="hello world iam yassin iam 25 yours ould "
# e= t.replace("25" ,"10")
# print(t)
# print(e)

# count هي عبارة عن دالة تقوم بعدد مرات تكرار نصوص معينة في المتغيرات
# name = "yassin ziane is fine and good and big"
# fn = name.count("and")
# print(fn)

# تجربة عملية على دالة count بستخدام input
# name = "yassine ziane is fine and good and big and nice and smart "
# r= name.count(input("enter the word you want to count: "))
# print(r)

# str هي عبارة عن دالة تقوم بتحويل اي قيمة الى نصوص ويمكن تعريف الجالة با casting
# x= 34
# y= str(x)
# print(y)

# boolean هي عبارة عن دالة تقوم باعطاء قيمة صحيحة او خاطئة
# f = 1 > 0
# print("task1 " + str(f))
# s = 1 < 0
# print("task2 " + str(s))
# s = 1 == 5
# print("task2 " + str(s))

# if هي عبارة عن دالة تقوم باعطاء قيمة صحيحة او خاطئة حسب الشرط الذي وضعته في الدالة    
# مثلا الدالة if  تعني اذا تحقق الشرط و الجالة else تعني اذا لم يتحقق الشرط
# yassine = 37
# mohamed = 37
# s = yassine
# e = mohamed
# if s < e:
#    print("mohamed is oldest then yassine")
# else هيا نفسهاالدلة if مثلا اذا لم تتحقق الدالة if  تعطي ناتج اخر
# elif s == e:
#    print("Mohammed is the same age as Yassin")
# else:
#    print("yassine is oldest then mohamed")

# list هي عبارة عن دالة تقوم بتخزين مجموعة من القيم في متغير واحد ويمكنك اضافة قيم اخرى الى المتغير
# papole = ["ahmed","yassine",]
# print(papole)
# طباعة عنصر معين من القائمة
# papole = ["ahmed","yassine","abobaker","ali"," sid ali"]
# print(papole[3])
# طباعة محموعة من العناصر المعينة من القائمة
# papole = ["ahmed","yassine","abobaker","ali"," sid ali"]
# print(papole[1:3])


# peipel = ["yassine","sidali","adodaker","lamia"]
# if peipel[0] == "sidali":
# 	print("no your name is not " + peipel[0])
# elif peipel[1] == "sidali":
# 	print("yes rour name is " + peipel[1])
# else:
# 	print("yes your name is " + peipel[0])

# name= "yassine"
# name1= "yassine"
# name2= "yasine"
# if name == name1 or name==name2:
# 	print("true")
# else:
# 	print("false")

# name= "yassine"
# age= 27
# if name == name and age==20:
#        print("true")
# else:
#        print("false")

# هاذا الكود يقوم بطباعة اسماء الاشخاص الذين لديهم نفس الاسم في القائمة
# name= "yassine"
# age=20
# if name =="yassine":
# 	if age == 20:
# 		print("true")
# 	else:
# 		print("false")
# else:
# 	print("false")

# هاذا الكود يقوم بطباعة اسماء الاشخاص الذين لديهم نفس الاسم في القائمة
# athat = ["chier","daske","non"]
# pris = [50,50,0,100]
# users = ["yassine","sidali","abobaker","lamia"]
# if users[0] == athat[0]:
# 	print(users[0] + " he hase " + athat[0] + " he spand " + str(pris[0]))
# elif users[1] == athat[1]:
#         print(users[1] + " he hase " + athat[1] + " he spand " + str(pris[1]))
# elif users[2] == athat[2]:
#         print(users[2] + " he hase " + athat[0]+ athat[1] +"he spand " + str(pris[3]))
# else:
# 	print(users[3] + " he hase " + athat[2] +" he spand " + str(pris[2]))

# هاذا الكود يقوم بتغيير عنصر معين في القائمة
# list = [21,34,56,45,32,87,32]
# list[2] = 320
# print(list)

# هاذا الكود يقوم بتغيير مجموعة من العناصر في القائمة
# list= [18,26,90,53,827]
# list[0:2]= [30,100]
# print(list)

# append هي عبارة عن دالة تقوم بإضافة عنصر معين الى القائمة في اخر القائمة
# user= ["yassine","sidali"]
# add= input("enter your name: ")
# user.append(add)
# print(user)

# insert هي عبارة عن دالة تقوم بإضافة عنصر معين الى القائمة ويمكنك تحديد مكان العنصر الذي تريد اضافته
# user= ["yassine","sidali"]
# add= input("enter your name: ")
# user.insert(0, add)
# print(user)

# pop هي عبارة عن دالة تقوم بحذف عنصر معين من القائمة ويمكنك تحديد العنصر الذي تريد حذفه
# user= ["yassine","sidali","abobaker","lamia"]
# user.pop(3)
# print(user)

# remove هي عبارة عن دالة تقوم بحذف عنصر معين من القائمة ويمكنك تحديد العنصر الذي تريد حذفه
# user= ["yassine","sidali","abobaker","lamia","ahmed","ali","mohamed"]
# add= input("enter your name: ")
# user.remove(add)
# print(user)

# تحدي
# numbers = [10,20,40,15]
# numbers.insert(1 , 30)
# numbers.insert(3 , 60)
# numbers.insert(5 , 55)
# print (numbers)


# numbers = [10,20,40,15]
# add30 = numbers[0] + numbers[1]
# add60 = numbers[1] + numbers[2]
# add55 = numbers[2] + numbers[3]
# numbers.insert(1 , add30)
# numbers.insert(3 , add60)
# numbers.insert(5, add55)
# print (numbers)

# for x in ["yassine" , "hi", "good"]:
#     print()

# مهمة هاذا الكوج هيا اذا كان في الجدول قيمة اصغر من 30 يطبعها و اذا كانت القيمة تساوي اة اقل لا يقوم با طباعتها
# myarray = [10,20,50,30,70,17]
# for i in myarray:
#     if i < 30 :
#         print(i)

# وهاذا يطبع اذا كانت تسوي او اقل
# myarray = [10,20,50,30,70,17]
# for i in myarray:
#     if i <= 30 :
#         print(i)

# continue هيا عبارة عن دالة تقوم بتخطي القيمة التي لا تحقق الشرط و تذهب الى القيمة التي تليه
# myarray = [10,20,50,30,70,17]
# for i in myarray:
#     if i <= 30 :
#         continue
#     print(i)

# break هيا عبارة عن دالة تقوم بانهاء الحلقة فور تحقق الشرط
# myarray = [10,20,50,0,30,70,17]
# for i in myarray:
#     if i == 0:
#         break
#     print(i)

# في هاذا الكود قمنا با برمجة يقوم با البحث عن الاسم اذا كان موجود فيطبع نعم موجود و يتوقف عن البحث 
# name = ["yassine","sidali","abobaker","mimo"]
# bak = "mimo"
# boolian = False
# for names in name :
#     if names == bak:
#         boolian = True
#         break
# if boolian:
#     print("yes is here")
# else:
#     print("no is not here")
        
# تحدي
# users = ["yassine","sidali","abobaker","mimo"]
# nmber = 1
# for u in users :
#     print("is nmber " + str(nmber) + " " + u)
#     nmber = nmber + 1

# for phone in range(0,10):
#     print(phone)


# name = "yassine ouldziane"
# finallystr = ""
# for n in name:
#     finallystr = finallystr + n
# print(finallystr)


# user = [
#     ["yassine","sidali","mimo","abobaker"],
#     ["zahra","anis","alhadi","mohamed"],
#     ["good","part","grin","page"],
# ]
# print(user[2][1])


# هاذا تحدي من chat gpt لختبار مستواي 
# students = ["mohamed","mhdi","yassine","sidali","abobaker"]
# nets = [15.67 , 18.56 , 8.90 , 9.20 , 15.30 , 11.40 ]
# #sersh = input("enter name of stodent : ")
# sersh = "yassine"
# if (sersh == students[0] and nets[0] >= 10) or (sersh == students[1] and nets[1] >= 10)  or (sersh == students[2] and nets[2] >= 10) or (sersh == students[3] and nets[3] >= 10) or (sersh == students[4] and nets[4] >= 10):
#     print("is najih")
# elif (sersh == students[0] and nets[0] <= 10) or (sersh == students[1] and nets[1] <= 10)  or (sersh == students[2] and nets[2] <= 10) or (sersh == students[3] and nets[3] <= 10) or (sersh == students[4] and nets[4] <= 10):
#      print(" is rasib")
# else:
#      print("not find")


# students = ["yassine", "sidali" , "abobaker" , "mimo" ]
# grades =   [ 8   , 16  ,  1    , 3]
# students[0]= grades[0]
# students[1]= grades[1]
# students[2]= grades[2]
# students[3]= grades[3]

# student = "yassine"

# for s in students :
#     students = grades
#     if student == s  :
#         if students < 10:
#             print(student + " is passed ")
#         print(student + " is not hier")
#     else:
#         print(student + " is not passed")
#         break

# else:
#     print(student + " not hier")


# students = ["yassine", "sidali" , "abobaker" , "mimo" ]
# grades =   [ 18 , 16 , 17 , 13]
# student = "sidali"
# for s in range(len(students)):
#     if student == students[s] and grades[s] < 10:
#         print (students[s] + " he Failed because "+ " he gets : " + str(grades[s]))
#         break
#     elif student == students[s] and grades[s] > 10:
#         print (students[s] + " he passed because "+ " he gets : " + str(grades[s]))
#         break
# else:
#     print(student + " is not found ! ")

# استخدام F لطباعة با شكل اسهل في print 
# students = ['yassine','sidali','abobaker','mimo']
# grades = [16.39,15.67,3.45,7.36]
# sersh =input('enter a student name : ')
# for i in range(len(students)):
#     if sersh == students[i]:
#         if grades[i] >= 10:
#             print (f'{sersh} he passed and he got {grades[i]}')
#             break
#         else:
#             print(f'{sersh} he not passed he got {grades[i]}')
#             break
# else:
#     print(f'not find')   

# استخدام upper عند ادخال البينات با خروف كبيرة أو صغيرة أو مختلطة يتم التعرف عليها
# students = ['yassine','sidali','abobaker','mimo']
# grades = [16.39,15.67,3.45,7.36]
# sersh =input('enter a student name : ')
# for i in range(len(students)):
#     if sersh.upper() == students[i].upper():
#         if grades[i] >= 10:
#             print (f'{sersh} he passed and he got {grades[i]}')
#             break
#         else:
#             print(f'{sersh} he not passed he got {grades[i]}')
#             break
# else:
#     print(f'not find')

# تحدي
# إذا كتب المستخدم اسم طالب، وبعد العثور عليه، اسأله:

# Do you want to change the grade? (yes/no)

# إذا كتب:

# yes

# اطلب الدرجة الجديدة، ثم عدّل الدرجة داخل القائمة، وبعد ذلك اطبع جميع الطلاب مع درجاتهم باستخدام حلقة for.
# students = ['yassine','sidali','abobaker','mimo']
# grades = [16.39,15.67,3.45,7.36]
# y = "yes"
# n = "no"

# search =input('Do you want to replace the student average? : ')
# for i in range(len(students)):
#     if search.upper() == y.upper():
#         name = input ('enter name of student : ')
#         if name.lower() == students[i].lower():
#             r = float(input(f'enter new grades for this  {name} : '))

#             if r <= 20 :
#                 r.replace(r, grades[i])
#                 print (f'{name} he got {r.replace}')

#             break
#         else:
#             print ('not found')
            
#     elif name == n :
#         print (f' {students}')
#         break
        
# years = int(input("enter your bherth years : "))
# age = 2026-years
# print (age)          


# def square(nmun):
#     return nmun * nmun
# for i in range(1,6):
#     print (square(i))

