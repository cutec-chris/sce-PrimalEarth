import sys,sce
class Yutyrannus_Character_BP(sce.Dinos):
   def __init__(self):
       super().__init__(self)
       name = 'Yutyrannus'
       blueprintPath = '/Game/PrimalEarth/Dinos/Yutyrannus/Yutyrannus_Character_BP.Yutyrannus_Character_BP'
       fullStatsRaw = [[1100, 0.2, 0.27, 0.5, 0], [420, 0.1, 0.1, 0, 0], [1550, 0.06, 0, 0.5, 0], [150, 0.1, 0.1, 0, 0], [3000, 0.1, 0.1, 0, 0], None, None, [500, 0.02, 0.04, 0, 0], [1, 0.05, 0.1, 0.5, 0.4], [1, 0, 0.01, 0, 0], None, None]
       immobilizedBy = ['Chain Bola', 'Large Bear Trap']
       breeding = {'gestationTime': 0, 'incubationTime': 17998.5601, 'eggTempMin': 32, 'eggTempMax': 34, 'maturationTime': 666666.667, 'matingCooldownMin': 64800, 'matingCooldownMax': 172800}
       colors = [{'name': 'Body Main', 'colors': ['BigFoot0', 'Black', 'Dark Grey', 'DarkWolfFur', 'Dino Dark Brown', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Medium Brown', 'DragonGreen2', 'White', 'WolfFur']}, {'name': 'Facial crest', 'colors': ['BigFoot4', 'Black', 'Dark Grey', 'DarkWolfFur', 'Dino Dark Brown', 'Dino Dark Orange', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Medium Brown', 'DragonBase0']}, None, None, {'name': 'Facial Highlights and Stripes', 'colors': ['Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Dark Orange', 'Dino Darker Grey', 'Dino Medium Brown', 'DragonBase1', 'DragonFire', 'DragonGreen1', 'DragonGreen3', 'White']}, {'name': 'Feet and Hands', 'colors': ['Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Medium Brown', 'DragonBase0', 'DragonBase1', 'White', 'WyvernPurple0']}]
       taming = {'nonViolent': False, 'violent': True, 'tamingIneffectiveness': 1.25, 'affinityNeeded0': 4250, 'affinityIncreasePL': 175, 'torporDepletionPS0': 0.725, 'foodConsumptionBase': 0.002314, 'foodConsumptionMult': 180.0634}
       TamedBaseHealthMultiplier = 1
       displayedStats = 927
