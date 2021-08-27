import sys,sce
class Griffin_Character_BP(sce.Dinos):
   def __init__(self):
       super().__init__(self)
       name = 'Griffin'
       blueprintPath = '/Game/PrimalEarth/Dinos/Griffin/Griffin_Character_BP.Griffin_Character_BP'
       variants = ['Ragnarok']
       isFlyer = True
       fullStatsRaw = [[950, 0.15, 0.216, -900, 0], [225, 0.05, 0.06, 0, 0], [1500, 0.06, 0, 0.5, 0], [150, 0.1, 0.1, 0, 0], [1600, 0.1, 0.1, 0, 0.15], None, None, [280, 0.02, 0.04, 0, 0], [1, 0.05, 0.1, -0.5, 0.4], [1, 0, 0.01, 0.365, 0], None, None]
       statImprintMult = [0.2, 0, 0.2, 0, 0.2, 0.2, 0, 0.2, 0.2, 0, 0, 0]
       immobilizedBy = ['Chain Bola']
       noGender = True
       breeding = {'gestationTime': 0, 'incubationTime': 0, 'maturationTime': 333333.333, 'matingCooldownMin': 64800, 'matingCooldownMax': 172800}
       colors = [{'name': 'Wing and Main Body', 'colors': ['BigFoot0', 'BigFoot5', 'Dark Grey', 'DarkWolfFur', 'Dino Albino', 'Dino Dark Brown', 'Dino Darker Grey', 'Dino Light Brown', 'Dino Medium Brown', 'DragonBase0', 'DragonBase1', 'WolfFur']}, None, None, None, {'name': 'Fur', 'colors': ['BigFoot0', 'BigFoot4', 'BigFoot5', 'Dark Grey', 'DarkWolfFur', 'Dino Dark Brown', 'Dino Light Brown', 'Dino Medium Brown', 'DragonBase1', 'Light Grey', 'WolfFur']}, {'name': 'Feather Highlights', 'colors': ['BigFoot0', 'BigFoot4', 'BigFoot5', 'Dark Grey', 'Dino Light Brown', 'Dino Light Orange', 'Dino Medium Brown', 'Light Grey', 'NearWhite', 'WolfFur']}]
       taming = {'nonViolent': False, 'violent': True, 'tamingIneffectiveness': 3.125, 'affinityNeeded0': 2200, 'affinityIncreasePL': 100, 'torporDepletionPS0': 2.1333332, 'foodConsumptionBase': 0.002066, 'foodConsumptionMult': 150}
       TamedBaseHealthMultiplier = 1
       displayedStats = 927
