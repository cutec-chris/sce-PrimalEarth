import sys,sce
class Mega_Tusoteuthis_Character_BP(sce.Alphas):
   def __init__(self):
       super().__init__(self)
       name = 'Alpha Tusoteuthis'
       blueprintPath = '/Game/PrimalEarth/Dinos/Tusoteuthis/Mega_Tusoteuthis_Character_BP.Mega_Tusoteuthis_Character_BP'
       variants = ['Mega']
       fullStatsRaw = [[30000, 0.2, 0.2025, 0.5, 0], [300, 0.1, 0.1, 0, 0], [1800, 0.06, 0, 0.5, 0], [215, 0.1, 0.1, 0, 0], [3200, 0.1, 0.1, 0, 0.15], None, None, [800, 0.02, 0.04, 0, 0], [1, 0.05, 0.1, 0.5, 0.4], [1, 0, 0.01, 1, 0], None, None]
       immobilizedBy = []
       breeding = {'gestationTime': 0, 'incubationTime': 17998.5601, 'eggTempMin': -75, 'eggTempMax': 75, 'maturationTime': 666666.667, 'matingCooldownMin': 64800, 'matingCooldownMax': 172800}
       colors = [{'name': 'Body Highlights', 'colors': ['Black', 'Dino Dark Blue', 'Dino Dark Orange', 'Dino Dark Red', 'Dino Dark Yellow', 'Dino Light Blue', 'Dino Light Orange', 'Dino Light Red', 'Dino Light Yellow']}, {'name': 'Tentacle Highlights', 'colors': ['Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Dark Green', 'Dino Dark Orange', 'Dino Dark Red', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Medium Brown', 'Dino Medium Green']}, None, None, {'name': 'Tentacle Main', 'colors': ['Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Dark Green', 'Dino Dark Orange', 'Dino Dark Red', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Medium Brown', 'Dino Medium Green']}, {'name': 'Body Main', 'colors': ['Black', 'Dino Albino', 'Dino Light Blue', 'Dino Light Brown', 'Dino Light Orange', 'Dino Light Yellow', 'Dino Medium Brown', 'Light Grey']}]
       taming = {'nonViolent': False, 'violent': False, 'tamingIneffectiveness': 0.75, 'affinityNeeded0': 12500, 'affinityIncreasePL': 125, 'foodConsumptionBase': 0.005, 'foodConsumptionMult': 180.0011}
       boneDamageAdjusters = {'upper_beak': 3, 'lower_beak': 3}
       TamedBaseHealthMultiplier = 1
       displayedStats = 919
