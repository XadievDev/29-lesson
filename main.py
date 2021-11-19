#XadievDev
#29-lesson.Objectlar bilan ishlash

#-------------------------------------------------#

# class Talaba:
#     """Talaba nomli klass yaratamiz"""
#     def __init__(self,ism,familiya,tyil):
#         """Talabaning xususiyatlari"""
#         self.ism = ism
#         self.familiya = familiya
#         self.tyil = tyil
#         self.bosqich = 1

#     def set_bosqich(self,bosqich):
#         """Talabaning kursini yangilovchi metod"""
#         self.bosqich = bosqich
        
#     def update_bosqich(self):
#         """Talabanining bosqichini 1taga ko'paytirish"""
#         self.bosqich += 1    
    
#     def get_info(self):
#         """Talaba haqida ma'lumot"""
#         return f"{self.ism} {self.familiya}. {self.bosqich}-bosqich talabasi "
    
#     def get_name(self):
#         """Talabaning ismini qaytaradi"""
#         return self.ism
    
#     def get_lastname(self):
#         """Talabaning familiyasini qaytaradi"""
#         return self.familiya
    
#     def get_fullname(self):
#         """Talabaning ism-familiyasini qaytaradi"""
#         return f"{self.ism} {self.familiya}"
    
#     def get_age(self,yil):
#         """Talabaning yoshini qaytaradi"""
#         return yil-self.tyil


# talaba1 = Talaba("Alijon","Valiyev",2000)
# print(talaba1.get_info())   

# talaba1.bosqich= 2
# print(talaba1.bosqich)

# talaba1 = Talaba("Alijon","Valiyev",2000)
# talaba1.set_bosqich(3)
# print(talaba1.get_info())    

# talaba1 = Talaba("Alijon","Valiyev",2000)
# print(talaba1.get_info())

# talaba1.update_bosqich() # 1 bosqichga oshiramiz
# print(talaba1.get_info())

# talaba1.update_bosqich() # 1 bosqichga oshiramiz
# print(talaba1.get_info())

# #----------------------------------------------------#

# class Fan():
#     """Fan nomli klass"""
#     def __init__(self,nomi):
#         self.nomi = nomi
#         self.talabalar_soni = 0
#         self.talabalar = []
    
#     def add_student(self,talaba):
#         """Fanga talabalar qo'shish"""
#         self.talabalar.append(talaba)
#         self.talabalar_soni += 1
    
#     def get_name(self):
#         """Fan nomi"""
#         return self.nomi
    
#     def get_students(self):
#         """Fanga yozilgan talabalar haqida ma'lumot"""
#         return [x.get_info() for x in self.talabalar]
    
#     def get_students_num(self):
#         """Fanga yozilgan talabalar soni"""
#         return self.talabalar_soni


# mat_talabalar = matematika.get_students()
# print(mat_talabalar)

# matematika = Fan("Oliy Matematika")
# talaba1 = Talaba("Alijon","Valiyev",2000)
# talaba2 = Talaba("Hasan","Alimov",2001)
# talaba3 = Talaba("Akrom","Boriyev",2001)

# matematika.add_student(talaba1)
# matematika.add_student(talaba2)
# matematika.add_student(talaba3)

# print(matematika.talabalar_soni)
# print(matematika.talabalar)

# #----------------------------------------------------#

# dir(Talaba)

# def see_methods(klass):
#     return [method for method in dir(klass) if method.startswith('__') is False]

# print(see_methods(Talaba))

# print(talaba1.__dict__)

#-----------------------------------------------------------------------#

#1.Avto degan yangi klass yarating. Unga avtomobillarga doir bo'lgan bir nechta xususiyatlar (model, rang, korobka, narh va hokazo) # # # qo'shing. Ayrim xususiyatlarga standart qiymat bering (masalan, kilometer=0)
#2.Avto ga oid obyektning xususiyatlarini qaytaradigan metodlar yozing
# get_info() metodi avto haqida to'liq ma'lumotni matn ko'rinishida qaytarsin
#3.Avto ga oid obyektning xususiyatlarini yangilaydigan metodlar yozing.
# update_km() metodi son qabul qilib olib, avtomobilning yurgan kilometrajini yangilab borsin


# class Avto:
#     """Avtolar haqida ma'lumotlar"""
#     def __init__(self , model , rang , karobka = 'avtomat' , narh = None):
#         """Avtolar xususiyatlari"""
#         self.model = model
#         self.rang = rang
#         self.karobka = karobka
#         self.narh = narh
#         self.kilo = 0

#     def get_model(self):
#         """Avtoning modelini qaytaradi"""
#         return self.model

#     def get_rang(self):
#         """Avtoning rangini qaytaradi"""
#         return self.rang

#     def get_karobka(self):
#         """Avtoning karobkasini qaytaradi"""
#         return self.karobka
    
#     def get_narh(self):
#         """Avtoning narhini qaytaradi"""
#         return self.narh
    
#     def get_kilo(self):
#         """Avtoning yurgani qaytaradi"""
#         return self.kilo

#     def get_avto_info(self):
#         """Avtoning ma'lumotlarini qaytaradi"""
#         return f"{self.rang.title()} rangli {self.model}.Karobka {self.karobka}.Narhi {self.narh}$."

#     def update_km(self):
#         """Avtoning yurganini yangilaydi"""
#         self.kilo = int(input("Necha kilometr yuridi?\n>>>"))

#     def update_narh(self):
#         """Avtoning narhini yangilaydi"""
#         self.narh = int(input("Narhini o'zgartiring:"))

# avto1 = Avto('BMW','qora','avtomat',100000)
# print(avto1.get_avto_info())

#-----------------------------------------------------------------------#

#1.Yangi, Avtosalon degan klass yarating va kerakli xususiyatlar bilan to'ldiring (salon nomi, manzili, sotuvdagi avtomobillar va hokazo)
#2.Avtosalonga yangi avtomobillar qo'shish uchun metod yozing
#3.Avtosalondagi avtomobillar haqida ma'lumot qaytaruvchi metod yozing
#4.Yuqoridagi obyektlar va ularga tegishli metodlarni tekshirib ko'ring
# dir() funksyasi va __dict__ metodi yordamida o'zingiz yozgan va Pythondagi turli klass va obyektlarning xususiyatlari va metodlarini # toping (dir(str), dir(int) va hokazo)

# class Avto_salon:
#     """Avtosalon"""
#     def __init__(self,salon_nomi,manzili):
#         """Avtosalon """
#         self.salon_nomi = salon_nomi
#         self.manzili = manzili
#         self.sot_avtolar = []
#         self.soni_avtolar = 0

#     def get_salon_nomi(self):
#         return self.salon_nomi
    
#     def get_manzili(self):
#         return self.manzili
    
#     def get_sot_avtolar(self):
#         return self.sot_avtolar
    
#     def get_soni_avtolar(self):
#         return self.kel_avtolar
    
#     def qosh_sot_avtolar(self,avto):
#         self.sot_avtolar.append(avto)
#         self.soni_avtolar +=1

# salon1 = Avto_salon('SAMIPhone','USA')
    

    


    