import sys,sce
class Alpha_Leedsichthys_Character_BP(sce.Alphas):
   def __init__(self):
       super().__init__(self)
       name = 'Alpha Leedsichthys'
       blueprintPath = '/Game/PrimalEarth/Dinos/Leedsichthys/Alpha_Leedsichthys_Character_BP.Alpha_Leedsichthys_Character_BP'
       variants = ['Mega']
       fullStatsRaw = [[4400, 0.12, 0.243, 0.3, 0], [500, 0.1, 0.1, 0, 0], [4500, 0.06, 0, 0.5, 0], [150, 0.1, 0.1, 0, 0], [8000, 0.1, 0.1, 0, 0.15], None, None, [1800, 0.02, 0.04, 0, 0], [1, 0, 0.1, 0.9, 0.4], [1, 0, 0.01, 0, 0], None, None]
       immobilizedBy = []
       colors = [{'name': 'Main Body', 'colors': ['Dino Albino']}, None, None, None, {'name': 'Body Highlights', 'colors': ['Dino Albino']}, {'name': 'Underbelly', 'colors': ['Dino Albino']}]
       taming = {'nonViolent': False, 'violent': False, 'tamingIneffectiveness': 0.06, 'affinityNeeded0': 11000, 'affinityIncreasePL': 600, 'foodConsumptionBase': 0.005, 'foodConsumptionMult': 180.0011}
       TamedBaseHealthMultiplier = 1
       displayedStats = 919
