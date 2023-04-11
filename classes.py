#classlar-sınıflar

class human: 
    #def talk(self):
        #print("Human is talking..")
    # def talk(self,sentence):
    #     print(f"Human: {sentence}")
    name = "Deniz"
    
    def _init_(self, name):
        self.name = name
        print("Bir human instance'i üretildi.")
    def _str_(self):
        return f"str fonk. dönen değer: {self.name}"

    def talk(self,sentence):
        print(f"{self.name}: {sentence}")
    def walk(self):
        print(f"{self.name} is walking..")

#instance:example

human1 = human("Deniz")   
#human1.name="Zuhal"    
#human1.talk()
human1.walk()
human1.talk("Hi")
print(human1)

human2 =human("Deniz")
#human2.name = "Cemre"
human2.talk("Hi")
human2.walk()
print(human2)