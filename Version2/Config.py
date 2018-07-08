class Config:
    MAXHEIGHT = 6
    MAXWIDTH = 6
    HILLSKIPROUND = 1 #how many round would be hang by the hill

    #The generating possibility for creature
    CREATURE_Y = 1 #Have creature
    CREATURE_N = 5 #No creature

    #The generating possibility for species
    SPECIES_S = 0 #Attach enemy only
    SPECIES_E = 0 #Escape if found enemy
    SPECIES_K = 0 #Attack all
    SPECIES_N = 0 #Attack non empty
    SPECIES_H = 0 #Hop all
    SPECIES_AL = 5
    SPECIES_FL = 5
    SPECIES_FO = 5
    SPECIES_HO = 5
    SPECIES_LA = 5
    SPECIES_LR = 5
    SPECIES_PA = 5
    SPECIES_RR = 5

    #The generating possibility for terrian
    TERRIAN_H = 1 #Hill
    TERRIAN_P = 5 #Plain
    TERRIAN_L = 2 #Lake
    TERRIAN_F = 3 #Forest

    #The generating possibility for ability
    ABILITY_FA = 1 #Fly + Archesry
    ABILITY_F = 3 #Fly
    ABILITY_A = 2 #Archesry
    ABILITY_ = 5 #No ability



if __name__ == "__main__":
    print(Config.MAXHEIGHT)
    print(Config.MAXWIDTH)
