import sys,sce
class MegaRex_Character_BP(sce.Alphas):
   def __init__(self):
       super().__init__(self)
       name = 'Alpha T-Rex'
       blueprintPath = '/Game/PrimalEarth/Dinos/Rex/MegaRex_Character_BP.MegaRex_Character_BP'
       variants = ['Mega']
       fullStatsRaw = [[17500, 0.2, 0.27, 0.5, 0], [420, 0.1, 0.1, 0, 0], [1550, 0.06, 0, 0.5, 0], [150, 0.1, 0.1, 0, 0], [3000, 0.1, 0.1, 0, 0], None, None, [500, 0.02, 0.04, 0, 0], [1, 0.05, 0.1, 0.5, 0.4], [1, 0, 0.01, 0, 0], None, None]
       immobilizedBy = ['Chain Bola']
       breeding = {'gestationTime': 0, 'incubationTime': 17998.5601, 'eggTempMin': 32, 'eggTempMax': 34, 'maturationTime': 333333.333, 'matingCooldownMin': 64800, 'matingCooldownMax': 172800}
       colors = [{'name': 'Unknown', 'colors': ['Black', 'Dark Red', 'Dino Albino', 'Red']}, {'name': 'Unknown', 'colors': ['Black', 'Dark Red', 'Dino Albino', 'Red']}, {'name': 'Unknown', 'colors': ['Black', 'Dark Red', 'Dino Albino', 'Red']}, {'name': 'Unknown', 'colors': ['Black', 'Dark Red', 'Dino Albino', 'Red']}, {'name': 'Unknown', 'colors': ['Black', 'Dark Red', 'Dino Albino', 'Red']}, {'name': 'Unknown', 'colors': ['Black', 'Dark Red', 'Dino Albino', 'Red']}]
       taming = {'nonViolent': False, 'violent': False, 'tamingIneffectiveness': 1.25, 'affinityNeeded0': 3450, 'affinityIncreasePL': 150, 'foodConsumptionBase': 0.002314, 'foodConsumptionMult': 180.0634}
       TamedBaseHealthMultiplier = 1
       displayedStats = 919
