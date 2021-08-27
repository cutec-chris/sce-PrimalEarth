import sys,sce
class Basilosaurus_Character_BP(sce.Dinos):
   def __init__(self):
       super().__init__(self)
       name = 'Basilosaurus'
       blueprintPath = '/Game/PrimalEarth/Dinos/Basilosaurus/Basilosaurus_Character_BP.Basilosaurus_Character_BP'
       fullStatsRaw = [[2400, 0.2, 0.243, 0.3, 0], [300, 0.1, 0.1, 0, 0], [2000, 0.06, 0, 0.5, 0], [150, 0.1, 0.1, 0, 0], [8000, 0.1, 0.1, 0, 0.15], None, None, [700, 0.02, 0.04, 0, 0], [1, 0.05, 0.1, 0.9, 0.4], [1, 0, 0.01, 0, 0], None, None]
       immobilizedBy = []
       breeding = {'gestationTime': 28571.4286, 'incubationTime': 0, 'maturationTime': 416666.667, 'matingCooldownMin': 64800, 'matingCooldownMax': 172800}
       colors = [{'name': 'Body Main', 'colors': ['Black', 'Dino Dark Blue', 'Dino Dark Orange', 'Dino Dark Red', 'Dino Dark Yellow', 'Dino Light Blue', 'Dino Light Orange', 'Dino Light Red', 'Dino Light Yellow']}, None, None, None, None, {'name': 'Belly', 'colors': ['Black', 'Dino Albino', 'Dino Light Blue', 'Dino Light Brown', 'Dino Light Orange', 'Dino Light Yellow', 'Dino Medium Brown', 'Light Grey']}]
       taming = {'nonViolent': True, 'violent': False, 'tamingIneffectiveness': 2.5, 'affinityNeeded0': 6600, 'affinityIncreasePL': 250, 'wakeAffinityMult': 1.6, 'wakeFoodDeplMult': 5, 'foodConsumptionBase': 0.002929, 'foodConsumptionMult': 420}
       TamedBaseHealthMultiplier = 1
       displayedStats = 919
