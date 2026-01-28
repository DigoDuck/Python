# Maintaining states within the class

class Cam:
    def __init__(self, name, filming=False):
        self.name = name
        self.filming = filming
        
    def film(self):
        if self.filming:
            print(f"{self.name} alredy filming")
            return
        
        print(f"{self.name} is filming...")
        self.filming = True
    
    def stop_film(self):
        if not self.filming:
            print(f"{self.name} is not filming")
            return
        
        print(f"{self.name} is not filming...")
        self.filming = False
        
    def photograph(self):
        if self.filming:
            print((f"{self.name} cannot take photos while filming"))
            return

        print(f"{self.name} is taking a photo")
        
c1 = Cam("Cannon")
c2 = Cam("Sony")
c1.film()
c1.film()
c1.stop_film()
c1.photograph()

c2.stop_film()