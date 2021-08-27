import sys,sce
class CrystalWyvern_Character_BP_Blood(sce.Dinos):
   def __init__(self):
       super().__init__(self)
       name = 'Blood Crystal Wyvern'
       blueprintPath = '/Game/PrimalEarth/Dinos/CrystalWyvern/CrystalWyvern_Character_BP_Blood.CrystalWyvern_Character_BP_Blood'
       variants = ['CrystalIsles']
       isFlyer = True
       fullStatsRaw = [[1295, 0.15, 0.2025, -785, 0], [325, 0.05, 0.05, 0, 0], [545, 0.06, 0, 0.5, 0], [150, 0.1, 0.1, 0, 0], [1500, 0.1, 0.1, 0, 0], None, None, [300, 0.02, 0.04, 0, 0], [1, 0.05, 0.1, -0.25, 0.4], [1, 0, 0.01, 0, 0], None, None]
       statImprintMult = [0.2, 0, 0.2, 0, 0.2, 0.2, 0, 0.2, 0.2, 0, 0, 0]
       immobilizedBy = ['Chain Bola', 'Large Bear Trap']
       breeding = {'gestationTime': 0, 'incubationTime': 17998.5601, 'eggTempMin': 75, 'eggTempMax': 85, 'maturationTime': 333333.333, 'matingCooldownMin': 64800, 'matingCooldownMax': 172800}
       colors = [{'name': 'Body Main', 'colors': ['Black', 'Black Sands', 'Dark Red', 'Dark Violet', 'Dark Warm Gray', 'Dino Dark Red', 'Dino Darker Grey', 'NearBlack']}, None, {'name': 'Scales Main', 'colors': ['Coral', 'Dino Albino', 'Dino Light Red', 'Light Red', 'Light Warm Gray']}, None, {'name': 'Fins Highlight', 'colors': ['Coral', 'Dino Albino', 'Dino Light Red', 'Light Red', 'Light Warm Gray']}, {'name': 'Body Highlights', 'colors': ['Coral', 'Dino Albino', 'Dino Light Red', 'Light Red', 'Light Warm Gray']}]
       taming = {'nonViolent': True, 'violent': False, 'tamingIneffectiveness': 0.72072, 'affinityNeeded0': 3750, 'affinityIncreasePL': 135, 'wakeAffinityMult': 1, 'wakeFoodDeplMult': 62.5, 'foodConsumptionBase': 0.000185, 'foodConsumptionMult': 199.984}
       TamedBaseHealthMultiplier = 1
       displayedStats = 927
