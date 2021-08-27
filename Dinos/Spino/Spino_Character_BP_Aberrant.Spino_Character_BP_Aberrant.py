import sys,sce
class Spino_Character_BP_Aberrant(sce.Aberration):
   def __init__(self):
       super().__init__(self)
       name = 'Aberrant Spino'
       blueprintPath = '/Game/PrimalEarth/Dinos/Spino/Spino_Character_BP_Aberrant.Spino_Character_BP_Aberrant'
       variants = ['Aberrant']
       fullStatsRaw = [[700, 0.2, 0.27, 0.5, 0], [350, 0.1, 0.1, 0, 0], [850, 0.06, 0, 0.5, 0], [650, 0.1, 0.1, 0, 0], [2600, 0.1, 0.1, 0, 0], None, None, [350, 0.02, 0.04, 0, 0], [1, 0.05, 0.1, 0.5, 0.4], [1, 0, 0.01, 0, 0], None, None]
       immobilizedBy = ['Chain Bola', 'Large Bear Trap']
       breeding = {'gestationTime': 0, 'incubationTime': 13845.0462, 'eggTempMin': 30, 'eggTempMax': 32, 'maturationTime': 256410.256, 'matingCooldownMin': 64800, 'matingCooldownMax': 172800}
       colors = [{'name': 'Unknown', 'colors': ['Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Dark Green', 'Dino Dark Orange', 'Dino Dark Red', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Medium Brown', 'Dino Medium Green']}, {'name': 'Unknown', 'colors': ['Black', 'Dino Albino', 'Dino Dark Blue', 'Dino Dark Green', 'Dino Dark Orange', 'Dino Dark Purple', 'Dino Dark Red', 'Dino Dark Yellow', 'Dino Light Blue', 'Dino Light Green', 'Dino Light Orange', 'Dino Light Purple', 'Dino Light Red', 'Dino Light Yellow', 'Dino Medium Green']}, {'name': 'Unknown', 'colors': ['Black', 'Dark Grey', 'Dino Albino', 'Dino Dark Blue', 'Dino Dark Brown', 'Dino Dark Green', 'Dino Dark Orange', 'Dino Dark Purple', 'Dino Dark Red', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Light Blue', 'Dino Light Brown', 'Dino Light Green', 'Dino Light Orange', 'Dino Light Purple', 'Dino Light Red', 'Dino Light Yellow', 'Dino Medium Brown', 'Dino Medium Green', 'Light Grey']}, None, {'name': 'Unknown', 'colors': ['Black', 'Dino Albino', 'Dino Dark Blue', 'Dino Dark Green', 'Dino Dark Orange', 'Dino Dark Purple', 'Dino Dark Red', 'Dino Dark Yellow', 'Dino Light Blue', 'Dino Light Green', 'Dino Light Orange', 'Dino Light Purple', 'Dino Light Red', 'Dino Light Yellow', 'Dino Medium Green']}, {'name': 'Unknown', 'colors': ['Black', 'Dino Light Blue', 'Dino Light Brown', 'Dino Light Green', 'Dino Light Orange', 'Dino Light Yellow', 'Dino Medium Brown', 'Dino Medium Green', 'Light Grey']}]
       taming = {'nonViolent': False, 'violent': True, 'tamingIneffectiveness': 1.5, 'affinityNeeded0': 3200, 'affinityIncreasePL': 150, 'torporDepletionPS0': 2.1333332, 'foodConsumptionBase': 0.002066, 'foodConsumptionMult': 150}
       TamedBaseHealthMultiplier = 0.96
       displayedStats = 927
