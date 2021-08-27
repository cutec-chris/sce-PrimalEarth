import sys,sce
class Purlovia_Character_BP(sce.Dinos):
   def __init__(self):
       super().__init__(self)
       name = 'Purlovia'
       blueprintPath = '/Game/PrimalEarth/Dinos/Purlovia/Purlovia_Character_BP.Purlovia_Character_BP'
       fullStatsRaw = [[275, 0.2, 0.27, 0.5, 0], [300, 0.1, 0.1, 0, 0], [500, 0.06, 0, 0.5, 0], [150, 0.1, 0.1, 0, 0], [4000, 0.1, 0.1, 0, 0], None, None, [400, 0.02, 0.04, 0, 0], [1, 0.05, 0.1, 0.5, 0.4], [1, 0, 0.01, 0, 0], None, None]
       immobilizedBy = ['Chain Bola', 'Large Bear Trap', 'Plant Species Y']
       breeding = {'gestationTime': 15037.594, 'incubationTime': 0, 'maturationTime': 175438.596, 'matingCooldownMin': 64800, 'matingCooldownMax': 172800}
       colors = [{'name': 'Main Body', 'colors': ['BigFoot0', 'BigFoot5', 'Black', 'Dark Grey', 'DarkWolfFur', 'Dino Dark Brown', 'Dino Dark Orange', 'Dino Dark Red', 'Dino Darker Grey', 'Dino Medium Brown']}, None, None, None, {'name': 'Belly', 'colors': ['Dark Grey', 'DarkWolfFur', 'Dino Dark Brown', 'Dino Dark Red', 'Dino Darker Grey', 'Dino Medium Brown', 'None']}, {'name': 'Highlights', 'colors': ['BigFoot4', 'Black', 'Dino Light Brown', 'Dino Light Orange', 'Dino Medium Brown', 'Light Grey', 'WolfFur']}]
       taming = {'nonViolent': False, 'violent': True, 'tamingIneffectiveness': 3.125, 'affinityNeeded0': 2250, 'affinityIncreasePL': 100, 'torporDepletionPS0': 0.3, 'foodConsumptionBase': 0.001543, 'foodConsumptionMult': 288.0392}
       TamedBaseHealthMultiplier = 1
       displayedStats = 927
