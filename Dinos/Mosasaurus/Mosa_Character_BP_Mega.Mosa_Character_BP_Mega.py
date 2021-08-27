import sys,sce
class Mosa_Character_BP_Mega(sce.Alphas):
   def __init__(self):
       super().__init__(self)
       name = 'Alpha Mosasaur'
       blueprintPath = '/Game/PrimalEarth/Dinos/Mosasaurus/Mosa_Character_BP_Mega.Mosa_Character_BP_Mega'
       variants = ['Mega']
       fullStatsRaw = [[54000, 0.12, 0.21, 0.3, 0], [400, 0.1, 0.1, 0, 0], [3000, 0.06, 0, 0.5, 0], [150, 0.1, 0.1, 0, 0], [8000, 0.1, 0.1, 0, 0.15], None, None, [1300, 0.02, 0.04, 0, 0], [1, 0.05, 0.1, 0.65, 0.4], [1, 0, 0.005, 0, 0], None, None]
       immobilizedBy = []
       breeding = {'gestationTime': 28571.4286, 'incubationTime': 0, 'maturationTime': 666666.667, 'matingCooldownMin': 64800, 'matingCooldownMax': 172800}
       colors = [{'name': 'Unknown', 'colors': ['Black', 'Dark Red', 'Dino Albino', 'Red']}, {'name': 'Unknown', 'colors': ['Black', 'Dark Red', 'Dino Albino', 'Red']}, {'name': 'Unknown', 'colors': ['Black', 'Dark Red', 'Dino Albino', 'Red']}, {'name': 'Unknown', 'colors': ['Black', 'Dark Red', 'Dino Albino', 'Red']}, {'name': 'Unknown', 'colors': ['Black', 'Dark Red', 'Dino Albino', 'Red']}, {'name': 'Unknown', 'colors': ['Black', 'Dark Red', 'Dino Albino', 'Red']}]
       taming = {'nonViolent': False, 'violent': False, 'tamingIneffectiveness': 0.06, 'affinityNeeded0': 11000, 'affinityIncreasePL': 600, 'foodConsumptionBase': 0.005, 'foodConsumptionMult': 180.0011}
       TamedBaseHealthMultiplier = 1
       displayedStats = 919
