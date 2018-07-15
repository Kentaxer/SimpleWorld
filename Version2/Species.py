from WorldEnum import OpCode
from Instruction import Instruction

class Species:

    def __init__(self, name, instructions):
        self.__name = name
        self.__instructions = instructions
        self.__insLength = len(instructions)
    
    @property
    def name(self):
        return self.__name
    
    @property
    def instructions(self):
        return self.__instructions

    @property
    def insLength(self):
        return self.__insLength

    def runToExecutableAddr(self, inputAddr, isEnemy, isEmpty, isSame, isWall):
        '''
        execute the instruction forward
        return the address where the execution stop
        '''
        currentAddr = inputAddr
        if inputAddr >= self.__insLength or inputAddr < 0:
            currentAddr = 0

        currentIns = self.__instructions[currentAddr]
        currentInsOpCode = currentIns.opCode
        if currentInsOpCode == OpCode.HOP or  \
        currentInsOpCode == OpCode.LEFT or  \
        currentInsOpCode == OpCode.RIGHT or  \
        currentInsOpCode == OpCode.INFECT or  \
        currentInsOpCode == OpCode.INTERACT:
            return currentAddr

        elif currentInsOpCode == OpCode.GO or  \
        (currentInsOpCode == OpCode.IFSAME and isSame) or  \
        (currentInsOpCode == OpCode.IFEMPTY and isEmpty) or  \
        (currentInsOpCode == OpCode.IFENEMY and isEnemy) or  \
        (currentInsOpCode == OpCode.IFWALL and isWall):
            return self.runToExecutableAddr(currentIns.targetAddr, isEnemy, isEmpty, isSame, isWall) 

        else:
            return self.runToExecutableAddr(currentAddr + 1, isEnemy, isEmpty, isSame, isWall)

    
    def getOpcode(self, inputAddr):
        currentAddr = inputAddr
        if inputAddr >= self.__insLength or inputAddr < 0:
            currentAddr = 0
        
        return self.__instructions[currentAddr].opCode

    @staticmethod
    def createAltRoverSpecies():
        '''
ifenemy 8 If there is an enemy
ifwall 6
ifsame 6
hop
go 1
left
go 10
infect
go 1
ifenemy 17 If there is an enemy
ifwall 15
ifsame 15
hop
go 10
right
go 1
infect
go 10


The alt_rover constantly moves forward.  When it
runs into a wall or another alt_rover, it turns left and right
alternatively.
        '''

        ins0 = Instruction(OpCode.GO, 1)
        ins1 = Instruction(OpCode.IFENEMY, 10)
        ins2 = Instruction(OpCode.IFWALL, 6)
        ins3 = Instruction(OpCode.IFSAME, 6)
        ins4 = Instruction(OpCode.HOP, None)
        ins5 = Instruction(OpCode.GO, 1)
        ins6 = Instruction(OpCode.LEFT, None)
        ins7 = Instruction(OpCode.GO, 10)
        ins8 = Instruction(OpCode.INFECT, None)
        ins9 = Instruction(OpCode.GO, 1)
        ins10 = Instruction(OpCode.IFENEMY, 17)
        ins11 = Instruction(OpCode.IFWALL, 15)
        ins12 = Instruction(OpCode.IFSAME, 15)
        ins13 = Instruction(OpCode.HOP, None)
        ins14 = Instruction(OpCode.GO, 10)
        ins15 = Instruction(OpCode.RIGHT, None)
        ins16 = Instruction(OpCode.GO, 10)
        ins17 = Instruction(OpCode.INFECT, None)
        ins18 = Instruction(OpCode.GO, 10)
        inss = [ins0, ins1, ins2,ins3, ins4, ins5, ins6, ins7, ins8, ins9, ins10,  \
        ins11, ins12, ins13, ins14, ins15, ins16, ins17, ins18]
        return Species("Altrover", inss)



    @staticmethod
    def createFlyTrapSpecies():
        '''
ifenemy 4    If there is an enemy, go to step 4.
left         If no enemy, turn left.
go 1
infect
go 1

The flytrap sits in one place and spins.
It infects anything which comes in front.
Flytraps do well when they clump.
        '''

        ins0 = Instruction(OpCode.GO, 1)
        ins1 = Instruction(OpCode.IFENEMY, 4)
        ins2 = Instruction(OpCode.LEFT, None)
        ins3 = Instruction(OpCode.GO, 1)
        ins4 = Instruction(OpCode.INFECT, None)
        ins5 = Instruction(OpCode.GO, 1)
        
        inss = [ins0, ins1, ins2,ins3, ins4, ins5]
        return Species("Flytrap", inss)

    @staticmethod
    def createFoodSpecies():
        '''
left
go 1


Food just sits there and spins but doesn't infect anyone.
        '''

        ins0 = Instruction(OpCode.GO, 1)
        ins1 = Instruction(OpCode.LEFT, None)
        ins2 = Instruction(OpCode.GO, 1)
        inss = [ins0, ins1, ins2]
        return Species("Food", inss)


    @staticmethod
    def createHopSpecies():
        '''
hop
go 1


This just hops forward blindly,
it's good for testing that your program works at all.
        '''

        ins0 = Instruction(OpCode.GO, 1)
        ins1 = Instruction(OpCode.HOP, None)
        ins2 = Instruction(OpCode.GO, 1)
        inss = [ins0, ins1, ins2]
        return Species("Hop", inss)

    @staticmethod
    def createLandmineSpecies():
        '''
ifwall 5
ifsame 5
infect
go 1
left
go 1


The Land Mine turns until it is not facing a wall and then
just infects. It's lazy -- taking no risks and expending no
energy. The existence of Food does not favor the LandMine
since it will never move to find the food.
        '''

        ins0 = Instruction(OpCode.GO, 1)
        ins1 = Instruction(OpCode.IFWALL, 5)
        ins2 = Instruction(OpCode.IFSAME, 5)
        ins3 = Instruction(OpCode.INFECT, None)
        ins4 = Instruction(OpCode.GO, 1)
        ins5 = Instruction(OpCode.LEFT, None)
        ins6 = Instruction(OpCode.GO, 1)
        inss = [ins0, ins1, ins2,ins3, ins4, ins5, ins6]
        return Species("Landmine", inss)


    @staticmethod
    def createLroverSpecies():
        '''
ifenemy 8 If there is an enemy
ifwall 6
ifsame 6
hop
go 1
left
go 1
infect
go 1


The lrover constantly moves forward.  When it
runs into a wall or another lrover, it turns left.
        '''

        ins0 = Instruction(OpCode.GO, 1)
        ins1 = Instruction(OpCode.IFENEMY, 8)
        ins2 = Instruction(OpCode.IFWALL, 6)
        ins3 = Instruction(OpCode.IFSAME, 6)
        ins4 = Instruction(OpCode.HOP, None)
        ins5 = Instruction(OpCode.GO, 1)
        ins6 = Instruction(OpCode.LEFT, None)
        ins7 = Instruction(OpCode.GO, 1)
        ins8 = Instruction(OpCode.INFECT, None)
        ins9 = Instruction(OpCode.GO, 1)
        
        inss = [ins0, ins1, ins2,ins3, ins4, ins5, ins6, ins7, ins8, ins9]
        return Species("Lrover", inss)


    @staticmethod
    def createPathFinderSpecies():
        '''
ifempty 4
left
go 1
hop
go 1

The path_finder is more intelligent than the hop. If the square it faces is
not empty, it turns left. Otherwise, it moves forward.
        '''

        ins0 = Instruction(OpCode.GO, 1)
        ins1 = Instruction(OpCode.IFEMPTY, 4)
        ins2 = Instruction(OpCode.LEFT, None)
        ins3 = Instruction(OpCode.GO, 1)
        ins4 = Instruction(OpCode.HOP, None)
        ins5 = Instruction(OpCode.GO, 1)
        
        inss = [ins0, ins1, ins2,ins3, ins4, ins5]
        return Species("PathFinder", inss)


    @staticmethod
    def createRroverSpecies():
        '''
ifenemy 8 If there is an enemy
ifwall 6
ifsame 6
hop
go 1
right
go 1
infect
go 1


The rrover constantly moves forward.  When it
runs into a wall or another rrover, it turns right.
        '''

        ins0 = Instruction(OpCode.GO, 1)
        ins1 = Instruction(OpCode.IFENEMY, 8)
        ins2 = Instruction(OpCode.IFWALL, 6)
        ins3 = Instruction(OpCode.IFSAME, 6)
        ins4 = Instruction(OpCode.HOP, None)
        ins5 = Instruction(OpCode.GO, 1)
        ins6 = Instruction(OpCode.RIGHT, None)
        ins7 = Instruction(OpCode.GO, 1)
        ins8 = Instruction(OpCode.INFECT, None)
        ins9 = Instruction(OpCode.GO, 1)
        
        inss = [ins0, ins1, ins2,ins3, ins4, ins5, ins6, ins7, ins8, ins9]
        return Species("Rrover", inss)



    @staticmethod
    def createHumanSpecies():
        '''
Totally control by human
        '''

        ins0 = Instruction(OpCode.GO, 1)
        ins1 = Instruction(OpCode.INTERACT, None)
        ins2 = Instruction(OpCode.GO, 1)
        
        inss = [ins0, ins1, ins2]
        return Species("Humanbeing", inss)



    @staticmethod
    def createSemiHumanSpecies():
        '''
Some case control by Human
        '''

        ins0 = Instruction(OpCode.GO, 1)
        ins1 = Instruction(OpCode.IFENEMY, 9)
        ins2 = Instruction(OpCode.IFWALL, 7)
        ins3 = Instruction(OpCode.IFSAME, 7)
        ins4 = Instruction(OpCode.IFEMPTY, 11)
        ins5 = Instruction(OpCode.INTERACT, None)
        ins6 = Instruction(OpCode.GO, 1)
        ins7 = Instruction(OpCode.RIGHT, None)
        ins8 = Instruction(OpCode.GO, 1)
        ins9 = Instruction(OpCode.INFECT, None)
        ins10 = Instruction(OpCode.GO, 1)
        ins11 = Instruction(OpCode.HOP, None)
        ins12 = Instruction(OpCode.GO, 1)
        
        inss = [ins0, ins1, ins2,ins3, ins4, ins5, ins6, ins7, ins8, ins9, ins10, ins11, ins12]
        return Species("SHumanBeing", inss)



if __name__ == "__main__":
    ins1 = Instruction(OpCode.HOP, None)
    ins2 = Instruction(OpCode.IFEMPTY, 10)
    inss = [ins1, ins2]
    spec = Species("FLYTRAP", inss)
    print(spec.name)
    print(spec.insLength)
    print(spec.instructions)
