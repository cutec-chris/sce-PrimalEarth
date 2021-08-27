import sys,sce
class Deinonychus_Character_BP(sce.BaseCreature):
   def __init__(self):
       super().__init__(self)
       name = 'Deinonychus'
       blueprintPath = '/Game/PrimalEarth/Dinos/Raptor/Uberraptor/Deinonychus_Character_BP.Deinonychus_Character_BP'
       variants = ['Valguero']
       fullStatsRaw = [[200, 0.2, 0.27, 0.5, 0], [150, 0.1, 0.1, 0, 0], [180, 0.06, 0, 0.5, 0], [150, 0.1, 0.1, 0, 0], [1200, 0.1, 0.1, 0, 0], None, None, [140, 0.02, 0.04, 0, 0], [1, 0.05, 0.1, 0.5, 0.4], [1, 0, 0.015, 0.2, 0], None, None]
       immobilizedBy = ['Bola', 'Bear Trap', 'Large Bear Trap', 'Plant Species Y']
       breeding = {'gestationTime': 0, 'incubationTime': 17998.5601, 'eggTempMin': 80, 'eggTempMax': 90, 'maturationTime': 133333.333, 'matingCooldownMin': 64800, 'matingCooldownMax': 172800}
       colors = [{'name': 'Base color', 'colors': ['BigFoot0', 'BigFoot4', 'BigFoot5', 'Black', 'Dark Grey', 'DarkWolfFur', 'Dino Albino', 'Dino Dark Brown', 'Dino Dark Orange', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Medium Brown', 'DragonBase0', 'DragonBase1', 'DragonGreen0', 'DragonGreen1', 'DragonGreen2', 'DragonGreen3', 'NearBlack', 'WolfFur']}, {'name': 'Feathers accents', 'colors': ['BigFoot5', 'DarkWolfFur', 'Dino Light Blue', 'Dino Light Orange', 'Dino Light Purple', 'Dino Light Yellow', 'Dino Medium Brown', 'DragonBase0', 'DragonFire', 'DragonGreen3', 'NearBlack']}, None, {'name': 'Feathers main', 'colors': ['BigFoot0', 'BigFoot4', 'Black', 'Dark Grey', 'DarkWolfFur', 'Dino Dark Brown', 'Dino Dark Orange', 'Dino Darker Grey', 'Dino Light Blue', 'Dino Light Brown', 'Dino Light Orange', 'Dino Medium Brown', 'DragonBase0', 'DragonGreen3', 'Light Grey', 'WyvernBlue0', 'WyvernBlue1']}, {'name': 'Stripes', 'colors': ['BigFoot0', 'BigFoot5', 'Black', 'Dark Grey', 'DarkWolfFur', 'Dino Dark Brown', 'Dino Dark Orange', 'Dino Darker Grey', 'Dino Medium Brown', 'DragonGreen0', 'DragonGreen2', 'DragonGreen3', 'NearBlack', 'WyvernBlue0', 'WyvernBlue1', 'WyvernPurple0']}, {'name': 'Highlights', 'colors': ['BigFoot5', 'Black', 'Dino Albino', 'Dino Light Blue', 'Dino Light Brown', 'Dino Light Orange', 'Dino Light Yellow', 'Dino Medium Brown', 'Light Grey', 'WolfFur']}]
       taming = {'nonViolent': False, 'violent': False, 'tamingIneffectiveness': 3.125, 'affinityNeeded0': 1200, 'affinityIncreasePL': 60, 'foodConsumptionBase': 0.001543, 'foodConsumptionMult': 648.0881}
       boneDamageAdjusters = {'Cnt_Head_JNT_SKL': 3, 'Cnt_Neck_002_JNT_SKL': 3, 'Cnt_Neck_000_JNT_SKL': 3}
       TamedBaseHealthMultiplier = 1
       displayedStats = 927
