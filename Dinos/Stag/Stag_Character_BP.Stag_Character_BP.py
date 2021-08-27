import sys,sce
class Stag_Character_BP(sce.Dinos):
   def __init__(self):
       super().__init__(self)
       name = 'Megaloceros'
       blueprintPath = '/Game/PrimalEarth/Dinos/Stag/Stag_Character_BP.Stag_Character_BP'
       fullStatsRaw = [[300, 0.2, 0.27, 0.5, 0], [280, 0.1, 0.1, 0, 0], [175, 0.06, 0, 0.5, 0], [150, 0.1, 0.1, 0, 0], [1200, 0.1, 0.1, 0, 0], None, None, [220, 0.02, 0.04, 0, 0], [1, 0.05, 0.1, 0.5, 0.4], [1, 0, 0.01, 0.2, 0], None, None]
       immobilizedBy = ['Bola', 'Bear Trap', 'Large Bear Trap', 'Plant Species Y']
       breeding = {'gestationTime': 21978.022, 'incubationTime': 0, 'maturationTime': 256410.256, 'matingCooldownMin': 64800, 'matingCooldownMax': 172800}
       colors = [{'name': 'Body', 'colors': ['BigFoot0', 'BigFoot4', 'BigFoot5', 'Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Dark Orange', 'Dino Darker Grey', 'Dino Light Brown', 'Dino Light Orange', 'Dino Medium Brown', 'Light Grey']}, None, {'name': 'Antlers', 'colors': ['BigFoot0', 'BigFoot4', 'BigFoot5', 'Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Dark Orange', 'Dino Darker Grey', 'Dino Light Brown', 'Dino Light Orange', 'Dino Medium Brown', 'Light Grey']}, None, {'name': 'Patterning', 'colors': ['BigFoot0', 'BigFoot4', 'BigFoot5', 'Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Dark Orange', 'Dino Darker Grey', 'Dino Light Brown', 'Dino Light Orange', 'Dino Medium Brown', 'Light Grey']}, None]
       taming = {'nonViolent': False, 'violent': True, 'tamingIneffectiveness': 0.5, 'affinityNeeded0': 1200, 'affinityIncreasePL': 60, 'torporDepletionPS0': 0.2915, 'foodConsumptionBase': 0.001543, 'foodConsumptionMult': 432.0587}
       boneDamageAdjusters = {'c_neck1': 2.5, 'c_neck2': 2.5, 'c_jaw': 2.5}
       TamedBaseHealthMultiplier = 1
       displayedStats = 927
