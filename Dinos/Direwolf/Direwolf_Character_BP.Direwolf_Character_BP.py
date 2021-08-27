import sys,sce
class Direwolf_Character_BP(sce.Dinos):
   def __init__(self):
       super().__init__(self)
       name = 'Direwolf'
       blueprintPath = '/Game/PrimalEarth/Dinos/Direwolf/Direwolf_Character_BP.Direwolf_Character_BP'
       fullStatsRaw = [[330, 0.2, 0.27, 0.66, 0], [260, 0.1, 0.1, 0, 0], [450, 0.06, 0, 0.5, 0], [150, 0.1, 0.1, 0, 0], [1200, 0.1, 0.1, 0, 0.15], None, None, [170, 0.02, 0.04, 0, 0], [1, 0.05, 0.1, 0.4, 0.35], [1, 0, 0.01, 0.3, 0], None, None]
       immobilizedBy = ['Bola', 'Bear Trap', 'Large Bear Trap', 'Plant Species Y']
       breeding = {'gestationTime': 15037.594, 'incubationTime': 0, 'maturationTime': 175438.596, 'matingCooldownMin': 64800, 'matingCooldownMax': 172800}
       colors = [{'name': 'Body', 'colors': ['Black', 'Dark Grey', 'DarkWolfFur', 'Dino Dark Brown', 'Dino Darker Grey', 'Dino Light Brown', 'Dino Light Orange', 'Dino Medium Brown', 'Light Grey', 'White', 'WolfFur']}, None, None, None, {'name': 'Tail, Back, and Face', 'colors': ['Black', 'Dark Grey', 'DarkWolfFur', 'Dino Dark Brown', 'Dino Darker Grey', 'Dino Light Brown', 'Dino Light Orange', 'Dino Medium Brown', 'Light Grey', 'White', 'WolfFur']}, {'name': 'Feet', 'colors': ['Black', 'Dark Grey', 'DarkWolfFur', 'Dino Dark Brown', 'Dino Darker Grey', 'Dino Light Brown', 'Dino Light Orange', 'Dino Medium Brown', 'Light Grey', 'White', 'WolfFur']}]
       taming = {'nonViolent': False, 'violent': True, 'tamingIneffectiveness': 3.125, 'affinityNeeded0': 1200, 'affinityIncreasePL': 60, 'torporDepletionPS0': 0.5, 'foodConsumptionBase': 0.001543, 'foodConsumptionMult': 288.0392}
       boneDamageAdjusters = {'c_head': 2.5, 'c_jaw': 2.5}
       TamedBaseHealthMultiplier = 1
       displayedStats = 927
