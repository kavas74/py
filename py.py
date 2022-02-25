#modulok

#osztalyok



class Bolygo:

  # ---------------
  # konstruktor :
  # ---------------
  def __init__(self,s):
    elemek = s.strip('/n').split(';')

    self.megnev = elemek[0]          # bolygó megnevezése
    self.a = float(elemek[1])        # főtengely [CSE]
    self.e = float(elemek[2])        # excentritás
    self.fi = float(elemek[3])       # pályaelhajlás [fok]
    self.Y_szid = float(elemek[4])   # sziderikus év [nap]
    self.Y_szin = float(elemek[5])   # szinódikus év [nap]
    self.r_e = float(elemek[6])      # egyenlítő sugara [km]
    self.l = float(elemek[7])        # lapultság
    self.m = float(elemek[8])        # tömeg [földtömeg]
    self.ro = float(elemek[9])       # sűrűség [g/cm3]
    self.g = float(elemek[10])       # gravitációs gyorsulás [m/s2]
    self.P = float(elemek[11])       # felszíni nyomás [bar]

  # -----------------



#fuggvenyek

def feltolt(a):
    f = open("bolygok.txt","r", encoding="utf8")
    n = 0
    
    while True:
        sor = f.readline()
        if sor == "":
            break
        else:
            a.append(Bolygo(sor))
            n += 1
    f.close()
    return(n)


def osszegzes(a,n):
    s = 0
    for i in range(0,n):
        s += a[i].m
    return(s*5.972e24)


def rendezes(a,n):
    for i in range(0,n-1):
        for j in range(i+1,n):
            if(a[i].r_e > a[j].r_e):
                s = a[i]
                a[i] = a[j]
                a[j] = s

    f = open("kimutatas.txt","w")
    for i in range(0,n):
        print("A {0} bolygok egyenlitői sugara : {1} km.".format(a[i].megnev, a[i].r_e))
        f.write("A {0} bolygok egyenlitői sugara : {1} km.".format(a[i].megnev, a[i].r_e))
    f.close()
        
#programtörzs
    
n = 0
bolygok = []
n = feltolt(bolygok)
print("A bolygók tömegeinek összege : {0} kg.".format(osszegzes(bolygok,n)))
rendezes(bolygok,n)
