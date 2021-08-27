import sys,sce
class Liopleurodon_Character_BP(sce.Dinos):
   def __init__(self):
       super().__init__(self)
       name = 'Liopleurodon'
       blueprintPath = '/Game/PrimalEarth/Dinos/Liopleurodon/Liopleurodon_Character_BP.Liopleurodon_Character_BP'
       fullStatsRaw = [[3200, 0.2, 0.27, 0.3, 0], [800, 0.1, 0.1, 0, 0], [800, 0.06, 0, 0.5, 0], [150, 0.1, 0.1, 0, 0], [2000, 0.1, 0.1, 0, 0.15], None, None, [1000, 0.02, 0.04, 0, 0], [1, 0.05, 0.1, 1, 0.4], [1, 0, 0.01, 0, 0], None, None]
       immobilizedBy = []
       colors = [{'name': 'Body Main', 'colors': ['Black', 'DarkWolfFur', 'Dino Dark Blue', 'Dino Dark Brown', 'Dino Dark Yellow', 'Dino Light Blue', 'Dino Light Yellow', 'DragonGreen3', 'WyvernPurple0']}, None, None, None, {'name': 'Body Spots', 'colors': ['Dino Dark Orange', 'Dino Dark Yellow', 'Dino Light Red', 'Dino Medium Blue', 'DragonBase1', 'DragonGreen3', 'WyvernBlue0', 'WyvernPurple0', 'WyvernPurple1']}, {'name': 'Body Highlights', 'colors': ['Black', 'Dino Albino', 'Dino Light Brown', 'Dino Medium Brown', 'DragonGreen0', 'DragonGreen3', 'Light Grey', 'NearBlack', 'WyvernBlue1']}]
       taming = {'nonViolent': True, 'violent': False, 'tamingIneffectiveness': 1.875, 'affinityNeeded0': 2000, 'affinityIncreasePL': 100, 'wakeAffinityMult': 1.6, 'wakeFoodDeplMult': 4, 'foodConsumptionBase': 0.001852, 'foodConsumptionMult': 199.984}
       TamedBaseHealthMultiplier = 1
       displayedStats = 919
