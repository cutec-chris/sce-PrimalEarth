import sys,sce
class Dolphin_Character_BP(sce.Dinos):
   def __init__(self):
       super().__init__(self)
       name = 'Ichthyosaurus'
       blueprintPath = '/Game/PrimalEarth/Dinos/Dolphin/Dolphin_Character_BP.Dolphin_Character_BP'
       fullStatsRaw = [[275, 0.05, 0.0675, 0.3, 0], [300, 0.2, 0.2, 0, 0], [300, 0.06, 0, 0.5, 0], [150, 0.1, 0.1, 0, 0], [1000, 0.1, 0.1, 0, 0.15], None, None, [250, 0.02, 0.04, 0, 0], [1, 0.05, 0.05, 1, 0.4], [1, 0, 0.015, 0, 0], None, None]
       immobilizedBy = []
       breeding = {'gestationTime': 28571.4286, 'incubationTime': 0, 'maturationTime': 208333.333, 'matingCooldownMin': 64800, 'matingCooldownMax': 172800}
       colors = [{'name': 'Body', 'colors': ['Black', 'Dino Dark Blue', 'Dino Dark Orange', 'Dino Dark Red', 'Dino Dark Yellow', 'Dino Light Blue', 'Dino Light Orange', 'Dino Light Red', 'Dino Light Yellow']}, None, None, None, {'name': 'Back and Fins', 'colors': ['Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Dark Green', 'Dino Dark Orange', 'Dino Dark Red', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Medium Brown', 'Dino Medium Green']}, {'name': 'Belly', 'colors': ['Black', 'Dino Albino', 'Dino Light Blue', 'Dino Light Brown', 'Dino Light Orange', 'Dino Light Yellow', 'Dino Medium Brown', 'Light Grey']}]
       taming = {'nonViolent': True, 'violent': False, 'tamingIneffectiveness': 2.5, 'affinityNeeded0': 1500, 'affinityIncreasePL': 75, 'wakeAffinityMult': 1.6, 'wakeFoodDeplMult': 2.5, 'foodConsumptionBase': 0.001929, 'foodConsumptionMult': 420}
       TamedBaseHealthMultiplier = 1
       displayedStats = 919
