import random

class Person:
    def __init__(self, name, age, health, status):
      self.name = name
      self.age = age
      self.health = health
      self.status=status
      
    def introduce(self):
        "Comment"
        print("Hello, my name is {} and I am {} years old".format(self.name, self.age))
        
    def emote(self):
        emotion = random.randrange(1,3)
        if emotion == 1:
          print("{} is happy today".format(self.name))
        elif emotion == 2:
          print("{} is sad today".format(self.name))
          
    def status_change(self):
        if self.health == 100:
          print("{} is totally healthy!".format(self.name))
        elif self.health > 50:
          print("{} needs some medicine!".format(self.name))
        else:
            print("{} is gonna die :(".format(self.name))
            
Maria = Person("Maria", 30, 80, True)
Juan = Person("Juan", 45, 79, True)
Rosa = Person("Rosa", 21, 34, True)

Maria.introduce()
Juan.introduce()
Rosa.introduce()

Maria.status_change()

Juan.emote()


class Enemy(Person):
  def __init__(self, weapon, name, age, health, status):
    super().__init__(name, age, health, status)
    self.weapon=weapon
  
  def introduce(self):
     print("You are my mortal enemy!!!")
  
  def hurt(self, other):
    if self.weapon == 'rock':
      other.health -= 10
    elif self.weapon == 'stick':
      other.health -= 5
    print(other.health)
    
  def insult(self, other):
    if other.health <= 80:
      print("{}, you are tired and weak".format(other.name))
  
  def steal(self, other):
    print("Ha ha ha {}, I have your stuff".format(other.name))
    if other.status == True:
      other.status = False
      
      
Alex = Enemy('rock', "Alex", 24, 75, False)

Alex.introduce()
Alex.hurt(Maria)
Alex.insult(Juan)
Alex.steal(Rosa)



