import sys,sce
class Leedsichthys_Character_BP(sce.Dinos):
   def __init__(self):
       super().__init__(self)
       name = 'Leedsichthys'
       blueprintPath = '/Game/PrimalEarth/Dinos/Leedsichthys/Leedsichthys_Character_BP.Leedsichthys_Character_BP'
       fullStatsRaw = [[4400, 0.12, 0.243, 0.3, 0], [500, 0.1, 0.1, 0, 0], [4500, 0.06, 0, 0.5, 0], [150, 0.1, 0.1, 0, 0], [8000, 0.1, 0.1, 0, 0.15], None, None, [1800, 0.02, 0.04, 0, 0], [1, 0, 0.1, 0.9, 0.4], [1, 0, 0.01, 0, 0], None, None]
       immobilizedBy = []
       colors = [{'name': 'Main Body', 'colors': ['Black', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Light Blue', 'Dino Light Yellow', 'Dino Medium Brown', 'DragonGreen0', 'DragonGreen3', 'WyvernBlue0', 'WyvernBlue1']}, None, None, None, {'name': 'Body Highlights', 'colors': ['Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Medium Brown', 'DragonGreen0', 'DragonGreen1', 'WyvernBlue0']}, {'name': 'Underbelly', 'colors': ['Black', 'Dino Albino', 'Dino Light Blue', 'Dino Light Brown', 'Dino Light Purple', 'Dino Light Yellow', 'Dino Medium Brown', 'Light Grey']}]
       taming = {'nonViolent': False, 'violent': False, 'tamingIneffectiveness': 0.06, 'affinityNeeded0': 11000, 'affinityIncreasePL': 600, 'foodConsumptionBase': 0.005, 'foodConsumptionMult': 180.0011}
       TamedBaseHealthMultiplier = 1
       displayedStats = 919
