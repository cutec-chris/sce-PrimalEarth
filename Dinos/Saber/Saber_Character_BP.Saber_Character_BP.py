import sys,sce
class Saber_Character_BP(sce.Dinos):
   def __init__(self):
       super().__init__(self)
       name = 'Sabertooth'
       blueprintPath = '/Game/PrimalEarth/Dinos/Saber/Saber_Character_BP.Saber_Character_BP'
       fullStatsRaw = [[250, 0.2, 0.27, 0.5, 0], [200, 0.1, 0.1, 0, 0], [500, 0.06, 0, 0.5, 0], [150, 0.1, 0.1, 0, 0], [1200, 0.1, 0.1, 0, 0.15], None, None, [200, 0.02, 0.04, 0, 0], [1, 0.05, 0.1, 0.4, 0.35], [1, 0, 0.01, 0.32, 0], None, None]
       immobilizedBy = ['Bola', 'Bear Trap', 'Large Bear Trap', 'Plant Species Y']
       breeding = {'gestationTime': 15037.594, 'incubationTime': 0, 'maturationTime': 175438.596, 'matingCooldownMin': 64800, 'matingCooldownMax': 172800}
       colors = [{'name': 'Body', 'colors': ['Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Dark Orange', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Medium Brown']}, None, None, None, {'name': 'Mane and Face', 'colors': ['Black', 'Dino Light Brown', 'Dino Light Orange', 'Dino Light Yellow', 'Dino Medium Brown', 'Light Grey']}, {'name': 'Stripes', 'colors': ['Black', 'Dark Grey', 'Dino Albino', 'Dino Dark Blue', 'Dino Dark Brown', 'Dino Dark Green', 'Dino Dark Orange', 'Dino Dark Purple', 'Dino Dark Red', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Light Blue', 'Dino Light Brown', 'Dino Light Green', 'Dino Light Orange', 'Dino Light Purple', 'Dino Light Red', 'Dino Light Yellow', 'Dino Medium Brown', 'Dino Medium Green', 'Light Grey']}]
       taming = {'nonViolent': False, 'violent': True, 'tamingIneffectiveness': 3.125, 'affinityNeeded0': 1200, 'affinityIncreasePL': 60, 'torporDepletionPS0': 0.3, 'foodConsumptionBase': 0.001543, 'foodConsumptionMult': 288.0392}
       boneDamageAdjusters = {'c_head': 3, 'c_jaw': 3}
       TamedBaseHealthMultiplier = 1
       displayedStats = 927
