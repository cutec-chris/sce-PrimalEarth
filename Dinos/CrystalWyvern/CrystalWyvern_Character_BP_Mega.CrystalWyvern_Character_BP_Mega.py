import sys,sce
class CrystalWyvern_Character_BP_Mega(sce.Alphas):
   def __init__(self):
       super().__init__(self)
       name = 'Alpha Blood Crystal Wyvern'
       blueprintPath = '/Game/PrimalEarth/Dinos/CrystalWyvern/CrystalWyvern_Character_BP_Mega.CrystalWyvern_Character_BP_Mega'
       variants = ['CrystalIsles', 'Mega']
       isFlyer = True
       fullStatsRaw = [[5920, 0.15, 0.2025, -785, 0], [710, 0.05, 0.05, 0, 0], [990, 0.06, 0, 0.5, 0], [150, 0.1, 0.1, 0, 0], [1500, 0.1, 0.1, 0, 0], None, None, [300, 0.02, 0.04, 0, 0], [1, 0.05, 0.1, -0.25, 0.4], [1, 0, 0.01, 0, 0], None, None]
       statImprintMult = [0.2, 0, 0.2, 0, 0.2, 0.2, 0, 0.2, 0.2, 0, 0, 0]
       immobilizedBy = []
       breeding = {'gestationTime': 0, 'incubationTime': 0, 'maturationTime': 333333.333, 'matingCooldownMin': 64800, 'matingCooldownMax': 172800}
       colors = [{'name': 'Unknown', 'colors': ['Black', 'Dino Albino']}, None, {'name': 'Unknown', 'colors': ['Black', 'Dark Red', 'Dino Albino', 'Red']}, None, {'name': 'Unknown', 'colors': ['Black', 'Dark Red', 'Dino Albino', 'Red']}, {'name': 'Unknown', 'colors': ['Black', 'Dark Red', 'Dino Albino', 'Red']}]
       taming = {'nonViolent': False, 'violent': False, 'tamingIneffectiveness': 0.72072, 'affinityNeeded0': 3750, 'affinityIncreasePL': 135, 'foodConsumptionBase': 0.000185, 'foodConsumptionMult': 199.984}
       TamedBaseHealthMultiplier = 1
       displayedStats = 927
