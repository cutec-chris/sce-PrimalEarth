import sys,sce
class Mammoth_Character_BP(sce.Dinos):
   def __init__(self):
       super().__init__(self)
       name = 'Mammoth'
       blueprintPath = '/Game/PrimalEarth/Dinos/Mammoth/Mammoth_Character_BP.Mammoth_Character_BP'
       fullStatsRaw = [[850, 0.2, 0.27, 0.5, 0], [330, 0.1, 0.1, 0, 0], [550, 0.06, 0, 0.5, 0], [150, 0.1, 0.1, 0, 0], [5000, 0.1, 0.1, 0, 0], None, None, [500, 0.02, 0.04, 0, 0], [1, 0.05, 0.1, 0.5, 0.4], [1, 0, 0.015, 1, 0], None, None]
       immobilizedBy = ['Chain Bola', 'Large Bear Trap']
       breeding = {'gestationTime': 28571.4286, 'incubationTime': 0, 'maturationTime': 296296.296, 'matingCooldownMin': 64800, 'matingCooldownMax': 172800}
       colors = [{'name': 'Fur Main', 'colors': ['BigFoot0', 'BigFoot4', 'BigFoot5', 'Brown', 'Dark Grey', 'DarkWarmGray', 'DarkWolfFur', 'Dino Albino', 'Dino Dark Brown', 'Dino Darker Grey', 'Dino Light Brown', 'Dino Medium Brown', 'Light Grey', 'LightWarmGray', 'MediumWarmGray', 'NearBlack', 'WolfFur']}, {'name': 'Highlights', 'colors': ['BigFoot0', 'BigFoot4', 'BigFoot5', 'Brown', 'Dark Grey', 'DarkWarmGray', 'DarkWolfFur', 'Dino Albino', 'Dino Dark Brown', 'Dino Darker Grey', 'Dino Light Brown', 'Dino Medium Brown', 'Light Grey', 'LightWarmGray', 'MediumWarmGray', 'NearBlack', 'WolfFur']}, {'name': 'Tusks and Toes', 'colors': ['BigFoot0', 'BigFoot5', 'Dino Light Brown', 'LightWarmGray', 'WolfFur']}, None, {'name': 'Fur Accent', 'colors': ['BigFoot0', 'BigFoot4', 'BigFoot5', 'Brown', 'Dark Grey', 'DarkWarmGray', 'DarkWolfFur', 'Dino Albino', 'Dino Dark Brown', 'Dino Darker Grey', 'Dino Light Brown', 'Dino Medium Brown', 'Light Grey', 'LightWarmGray', 'MediumWarmGray', 'NearBlack', 'WolfFur']}, {'name': 'Underside', 'colors': ['BigFoot0', 'BigFoot4', 'BigFoot5', 'Brown', 'Dark Grey', 'DarkWarmGray', 'DarkWolfFur', 'Dino Albino', 'Dino Dark Brown', 'Dino Darker Grey', 'Dino Light Brown', 'Dino Medium Brown', 'Light Grey', 'LightWarmGray', 'MediumWarmGray', 'NearBlack', 'WolfFur']}]
       taming = {'nonViolent': False, 'violent': True, 'tamingIneffectiveness': 0.12, 'affinityNeeded0': 5000, 'affinityIncreasePL': 250, 'torporDepletionPS0': 0.3, 'foodConsumptionBase': 0.004133, 'foodConsumptionMult': 192.0278}
       TamedBaseHealthMultiplier = 1
       displayedStats = 927
