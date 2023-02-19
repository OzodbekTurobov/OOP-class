class AirPods:
    def __init__(self,nomi, rangi, narxi, yili,chidamliligi):
        self.nomi = nomi
        self.rangi = rangi
        self.narxi=narxi
        self.yili=yili
        self.chidamliligi=chidamliligi
    def shifr(self):
        print(self.nomi, self.rangi, self.narxi,self.yili,self.chidamliligi)

o1=AirPods("MI", "qora", 450, 2022, "zo`r")
o2=AirPods("Mir7", "kulrang", 200, 2023, "yaxshi")
o3=AirPods("V68", "jigari", 350, 2021, "yaxshi")
o4=AirPods("BT SPEAKER", "ko`k", 500, 2021, "zo`r")
o5=AirPods("AirpodsPro", "oq", 650, 2023, "Daxshat")

o1.shifr()
o2.shifr()
o3.shifr()
o4.shifr()
print(o5.shifr())

# Bu ikkinchi class

class Mashina:
    def __init__(self,nomi, rangi, chidamliligi, yili,narxi):
        self.nomi = nomi
        self.rangi = rangi
        self.chidamliligi = chidamliligi
        self.yili = yili
        self.narxi = narxi
    def mash(self):
        print(self.nomi, self.rangi, self.chidamliligi,self.yili,self.narxi)

o1=Mashina("Malibu", "oq", "bo`ladi", 2023, "300 mllion")
o2=Mashina("Ferrari", "sariq", "daxshat", 2023, "2milliard")
o3=Mashina("Cobalt", "ko`k", "zo`r", 2023, "130million")
o4=Mashina("Lambo", "qizil", "yaxshi", 2023, "2,5millliard")
o5=Mashina("2 Yoneks", "qora", "zo`r", 2023, "450million")

o1.mash()
o2.mash()
o3.mash()
o4.mash()
print(o5.mash())

# Bu uchinchi class

class Uylar:
    def __init__(self,xonasi, narxi, rangi, manzili, qavati):
        self.xonasi = xonasi
        self.narxi = narxi
        self.rangi=rangi
        self.manzili=manzili
        self.qavati=qavati
    def uy(self):
        print(self.xonasi, self.narxi, self.rangi,self.manzili,self.qavati)

o1=Uylar("11 xona", "2milliard", "xarxil", "ayronchi", "2qavat")
o2=Uylar("13 xona", "1,5mil", "qizil", "baliqchi", "3qavat")
o3=Uylar("7 xona", "1mil", "ko`k qizil", "xatirchi", "1qavat")
o4=Uylar("3 xona", "3mil", "oq qara", "tuman", "4qavat")
o5=Uylar("8 xona", "ko`p", "sariq oq", "olachi", "qavati ko`p")

o1.uy()
o2.uy()
o3.uy()
o4.uy()
print(o5.uy())

# Bu to`rtinchi class

class Odam:
    def __init__(self,ismi, fam, yoshi, ishjoyi, noutbooki):
        self.ismi = ismi
        self.fam = fam
        self.yoshi=yoshi
        self.ishjoyi=ishjoyi
        self.noutbooki=noutbooki
    def od(self):
        print(self.ismi, self.fam, self.yoshi, self.ishjoyi,self.noutbooki)

o1=Odam("Ubaydullo", "Jumayev", 21, "SUSYS.ACADEMY", "APPLE")
o2=Odam("Ozodbek", "Turobov", 15, "o`qiydi", "HONOR")
o3=Odam("Maruf", "Alimov", 15, "o`qiydi", "VIKTUS")
o4=Odam("Abduxmon", "Isroilov", 10, "o`qiydi", "VIKTUS")
o5=Odam("Firdavs", "Normurodov", 12, "o`qiydi", "ACER")

o1.od()
o2.od()
o3.od()
o4.od()
print(o5.od())

# Bu beshinchi class

class Noutbook:
    def __init__(self,nomi, rangi, narxi, yili, chidamliligi):
        self.nomi = nomi
        self.rangi = rangi
        self.narxi=narxi
        self.yili=yili
        self.chidamliligi=chidamliligi
    def nou(self):
        print(self.nomi, self.rangi, self.narxi,self.yili,self.chidamliligi)

o1=Noutbook("Apple", "kurang", 24, 2023, "zo`r")
o2=Noutbook("Honor", "kumushrang", 13, 2023, "zo`r")
o3=Noutbook("Victus", "qora", 11, 2023, "yaxshi")
o4=Noutbook("HP", "oq", 12, 2023, "bo`ladi")
o5=Noutbook("Acer", "jigari", 9, 2023, "zo`r")

o1.nou()
o2.nou()
o3.nou()
o4.nou()
print(o5.nou())

# Bu oltinchi class

class Hayvon:
    def __init__(self,nomi, yili, yashashi, rangi):
        self.nomi = nomi
        self.yili = yili
        self.yashashi=yashashi
        self.rangi=rangi
    def shifr(self):
        print(self.nomi, self.yili, self.yashashi,self.rangi)

o1=Hayvon("Sher", 2021, "afrika", "jigari")
o2=Hayvon("Jrafa", 2022, "afrika", "kulrang")
o3=Hayvon("Begimot", 2023, "afrika", "kumushrang")
o4=Hayvon("chayon", 2022, "afrika", "oq")
o5=Hayvon("ilon", 2022, "afrika", "qora")

o1.shifr()
o2.shifr()
o3.shifr()
o4.shifr()
print(o5.shifr())

# Bu yettinchi class

class Hasharot:
    def __init__(self,nomi, turi, yili, rangi):
        self.nomi = nomi
        self.turi = turi
        self.yili = yili
        self.rangi= rangi
    def shifr(self):
        print(self.nomi, self.turi, self.yili,self.rangi)

o1=AirPods("MI", "qora", 450, 2022, "zo`r")
o2=AirPods("Mir7", "kulrang", 200, 2023, "yaxshi")
o3=AirPods("V68", "jigari", 350, 2021, "yaxshi")
o4=AirPods("BT SPEAKER", "ko`k", 500, 2021, "zo`r")
o5=AirPods("AirpodsPro", "oq", 650, 2023, "Daxshat")

o1.shifr()
o2.shifr()
o3.shifr()
o4.shifr()
o5.shifr()


# Bu sakkizinchi class

class AirPods:
    def __init__(self,nomi, rangi, narxi, yili,chidamliligi):
        self.nomi = nomi
        self.rangi = rangi
        self.narxi=narxi
        self.yili=yili
        self.chidamliligi=chidamliligi
    def shifr(self):
        print(self.nomi, self.rangi, self.narxi,self.yili,self.chidamliligi)

o1=AirPods("MI", "qora", 450, 2022, "zo`r")
o2=AirPods("Mir7", "kulrang", 200, 2023, "yaxshi")
o3=AirPods("V68", "jigari", 350, 2021, "yaxshi")
o4=AirPods("BT SPEAKER", "ko`k", 500, 2021, "zo`r")
o5=AirPods("AirpodsPro", "oq", 650, 2023, "Daxshat")

o1.shifr()
o2.shifr()
o3.shifr()
o4.shifr()
o5.shifr()


# Bu to`qqizinchi class

class Nout:
    def __init__(self,ismchasi, yili, rangi):
        self.ismchasi = ismchasi
        self.yili=yili
        self.rangi=rangi
    def no(self):
        print(self.ismchasi, self.yili, self.rangi)
    
o1=Nout("Acer", 2023, "pushti")
o2=Nout("Honor", 2023, "oq")
o3=Nout("Huawe", 2023,"qora")
o4=Nout("Samsung", 2023, "qizil" )
o5=Nout("Del", 2023, "benafsha")

o1.no()
o2.no()
o3.no()
o4.no()
print(o5.no())


# Bu o`ninchi class

class Tel:
    def __init__(self,nomi, rangi, yili):
        self.nomi = nomi
        self.rangi=rangi
        self.yili=yili
    def shifr(self):
        print(self.nomi, self.rangi, self.yili)
    
o1=Tel("Iphone", "kulrang", 2023)
o2=Tel("Honor", "qora", 2023)
o3=Tel("Huawe", "Crimson", 2023)
o4=Tel("Samsung", "ko`k", 2023 )
o5=Tel("Nokia", "jigari", 2024)

o1.shifr()
o2.shifr()
o3.shifr()
o4.shifr()
print(o5.shifr())

# O`nta classs bo`lli