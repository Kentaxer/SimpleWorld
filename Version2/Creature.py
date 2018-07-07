from WorldEnum import Ability, Direction, OpCode
from Position import Position
from Species import Species
from Config import Config
from Instruction import Instruction

class Creature:

    def __init__(self, species, direction, abilities, position):
        self.__species = species
        self.__direction = direction
        self.__abilities = abilities
        self.__position = position
        self.__currentAddr = 0
        self.__skipRound = 0

    @property
    def canFly(self):
        if self.__abilities == None:
            return False

        return Ability.FLY in self.__abilities

    @property
    def canArc(self):
        if self.__abilities == None:
            return False

        return Ability.ARCH in self.__abilities

    @property
    def speciesName(self):
        return self.__species.name
    
    @property
    def position(self):
        return self.__position

    @property
    def direction(self):
        return self.__direction

    def getNextOpcode(self, isEnemy, isEmpty, isSame, isWall):
        if self.__skipRound > 0: # Skip this round and do nothing
            self.__skipRound -= 1
            return None

        executableAddr = self.__species.runToExecutableAddr(self.__currentAddr, isEnemy, isEmpty, isSame, isWall)
        opCode = self.__species.getOpcode(executableAddr)
        self.__currentAddr = executableAddr + 1 # move to next line
        return opCode

    def hop(self):
        if(self.__direction == Direction.EAST):
            self.__position.row += 1
        elif(self.__direction == Direction.WEST):
            self.__position.row -= 1
        elif(self.__direction == Direction.NORTH):
            self.__position.column -= 1
        elif(self.__direction == Direction.SOUTH):
            self.__position.column += 1

    
    def turnRight(self):
        if(self.__direction == Direction.EAST):
            self.__direction = Direction.SOUTH
        elif(self.__direction == Direction.WEST):
            self.__direction = Direction.NORTH
        elif(self.__direction == Direction.NORTH):
            self.__direction = Direction.EAST
        elif(self.__direction == Direction.SOUTH):
            self.__direction = Direction.WEST

    def turnLeft(self):
        if(self.__direction == Direction.EAST):
            self.__direction = Direction.NORTH
        elif(self.__direction == Direction.WEST):
            self.__direction = Direction.SOUTH
        elif(self.__direction == Direction.NORTH):
            self.__direction = Direction.WEST
        elif(self.__direction == Direction.SOUTH):
            self.__direction = Direction.EAST

    def infected(self, sourceCreature):
        self.__species = sourceCreature.__species

    def enterHill(self):
        if self.canFly:
            return

        self.__skipRound = Config.HILLSKIPROUND



if __name__ == "__main__":
    ins0 = Instruction(OpCode.IFENEMY, 8)
    ins1 = Instruction(OpCode.IFSAME, 6)
    ins2 = Instruction(OpCode.IFWALL, 6)
    ins3 = Instruction(OpCode.IFEMPTY, 4)
    ins4 = Instruction(OpCode.HOP, None)
    ins5 = Instruction(OpCode.GO, 0)
    ins6 = Instruction(OpCode.RIGHT, None)
    ins7 = Instruction(OpCode.GO, 0)
    ins8 = Instruction(OpCode.INFECT, None)
    ins9 = Instruction(OpCode.GO, 0)

    inss = [ins0, ins1, ins2,ins3, ins4, ins5, ins6, ins7, ins8, ins9]
    spec = Species("FLYTRAP", inss)
    creature = Creature(spec, Direction.EAST, [Ability.FLY, Ability.ARCH], Position(1,1))
    opcode = creature.getNextOpcode(False, False, True, True)
    assert(opcode == OpCode.RIGHT)
    opcode = creature.getNextOpcode(True, False, True, True)
    assert(opcode == OpCode.INFECT)