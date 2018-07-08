class Config:
    MAXHEIGHT = 6
    MAXWIDTH = 6
    HILLSKIPROUND = 1 #how many round would be hang by the hill

    #The generating possibility for creature
    CREATURE_Y = 2 #Have creature
    CREATURE_N = 5 #No creature

    #The generating possibility for species
    SPECIES_S = 0 #Attach enemy only
    SPECIES_E = 0 #Escape if found enemy
    SPECIES_K = 0 #Attack all
    SPECIES_N = 0 #Attack non empty
    SPECIES_H = 0 #Hop all
    SPECIES_AL = 1 #Altrover
    SPECIES_FL = 0 #Flytrap
    SPECIES_FO = 3 #Food
    SPECIES_HO = 0 #Hop
    SPECIES_LA = 0 #Landmine
    SPECIES_LR = 1 #Lrover
    SPECIES_PA = 3 #Pathfinder
    SPECIES_RR = 1 #Rrover

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
