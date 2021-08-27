import sys,sce
class Megalodon_Character_BP(sce.Dinos):
   def __init__(self):
       super().__init__(self)
       name = 'Megalodon'
       blueprintPath = '/Game/PrimalEarth/Dinos/Megalodon/Megalodon_Character_BP.Megalodon_Character_BP'
       fullStatsRaw = [[600, 0.2, 0.27, 0.3, 0], [320, 0.1, 0.1, 0, 0], [800, 0.06, 0, 0.5, 0], [150, 0.1, 0.1, 0, 0], [2000, 0.1, 0.1, 0, 0.15], None, None, [250, 0.02, 0.04, 0, 0], [1, 0.05, 0.1, 1, 0.4], [1, 0, 0.01, 0, 0], None, None]
       immobilizedBy = []
       breeding = {'gestationTime': 21978.022, 'incubationTime': 0, 'maturationTime': 256410.256, 'matingCooldownMin': 64800, 'matingCooldownMax': 172800}
       colors = [{'name': 'Body', 'colors': ['Black', 'Dino Dark Blue', 'Dino Dark Orange', 'Dino Dark Red', 'Dino Dark Yellow', 'Dino Light Blue', 'Dino Light Orange', 'Dino Light Red', 'Dino Light Yellow']}, None, None, None, {'name': 'Stripes', 'colors': ['Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Dark Green', 'Dino Dark Orange', 'Dino Dark Red', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Medium Brown', 'Dino Medium Green']}, {'name': 'Belly', 'colors': ['Black', 'Dino Albino', 'Dino Light Blue', 'Dino Light Brown', 'Dino Light Orange', 'Dino Light Yellow', 'Dino Medium Brown', 'Light Grey']}]
       taming = {'nonViolent': False, 'violent': True, 'tamingIneffectiveness': 1.875, 'affinityNeeded0': 2000, 'affinityIncreasePL': 100, 'torporDepletionPS0': 0.3, 'foodConsumptionBase': 0.001852, 'foodConsumptionMult': 199.984}
       TamedBaseHealthMultiplier = 1
       displayedStats = 919
