import sys,sce
class Gigant_Character_BP_TekCave(sce.BaseCreature):
   def __init__(self):
       super().__init__(self)
       name = 'Giganotosaurus'
       blueprintPath = '/Game/PrimalEarth/Dinos/Giganotosaurus/Gigant_Character_BP_TekCave.Gigant_Character_BP_TekCave'
       variants = ['Cave', 'TekCave']
       fullStatsRaw = [[80000, 0.0005, 0.002, -63000, 0], [400, 0.0005, 0.01, 0, 0], [10000, 0.06, 0, 0, 0], [150, 0.0025, 0.025, 0, 0], [4000, 0.0025, 0.025, 0, 0], None, None, [700, 0.01, 0.01, 0, 0], [1, 0.05, 0.05, -0.8, 0], [1, 0, 0.0031, 0, 0], None, None]
       immobilizedBy = ['Large Bear Trap']
       breeding = {'gestationTime': 0, 'incubationTime': 179985.601, 'eggTempMin': 43, 'eggTempMax': 44, 'maturationTime': 1010101.01, 'matingCooldownMin': 64800, 'matingCooldownMax': 172800}
       colors = [{'name': 'Unknown', 'colors': ['Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Dark Green', 'Dino Dark Red', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Light Brown', 'Dino Light Green', 'Dino Light Yellow', 'Dino Medium Brown', 'Dino Medium Green', 'Light Grey']}, None, None, None, {'name': 'Unknown', 'colors': ['Black', 'Dino Dark Red', 'Dino Light Brown', 'Dino Light Green', 'Dino Light Yellow', 'Dino Medium Brown', 'Dino Medium Green', 'Light Grey']}, {'name': 'Unknown', 'colors': ['Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Dark Green', 'Dino Dark Red', 'Dino Darker Grey', 'Dino Medium Brown', 'Dino Medium Green']}]
       taming = {'nonViolent': False, 'violent': False, 'tamingIneffectiveness': 1.25, 'affinityNeeded0': 5000, 'affinityIncreasePL': 160, 'foodConsumptionBase': 0.002314, 'foodConsumptionMult': 160.0563}
       TamedBaseHealthMultiplier = 1
       displayedStats = 927
