import sys,sce
class Diplodocus_Character_BP_Aberrant(sce.Aberration):
   def __init__(self):
       super().__init__(self)
       name = 'Aberrant Diplodocus'
       blueprintPath = '/Game/PrimalEarth/Dinos/Diplodocus/Diplodocus_Character_BP_Aberrant.Diplodocus_Character_BP_Aberrant'
       variants = ['Aberrant']
       fullStatsRaw = [[1700, 0.2, 0.27, 0.5, 0], [550, 0.1, 0.1, 0, 0], [3000, 0.06, 0, 0.5, 0], [300, 0.1, 0.1, 0, 0], [10000, 0.1, 0.1, 0, 0], None, None, [800, 0.02, 0.04, 0, 0], [1, 0, 0, 0.5, 0.4], [1, 0, 0.01, 0, 0], None, None]
       immobilizedBy = ['Chain Bola', 'Large Bear Trap']
       breeding = {'gestationTime': 0, 'incubationTime': 17998.5601, 'eggTempMin': 26, 'eggTempMax': 29, 'maturationTime': 333333.333, 'matingCooldownMin': 64800, 'matingCooldownMax': 172800}
       colors = [{'name': 'Unknown', 'colors': ['Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Dark Green', 'Dino Dark Orange', 'Dino Dark Red', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Medium Brown', 'Dino Medium Green']}, {'name': 'Unknown', 'colors': ['Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Dark Green', 'Dino Dark Orange', 'Dino Dark Red', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Medium Brown', 'Dino Medium Green']}, {'name': 'Unknown', 'colors': ['Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Dark Green', 'Dino Dark Orange', 'Dino Dark Red', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Medium Brown', 'Dino Medium Green']}, {'name': 'Unknown', 'colors': ['Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Dark Green', 'Dino Dark Orange', 'Dino Dark Red', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Medium Brown', 'Dino Medium Green']}, {'name': 'Unknown', 'colors': ['Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Dark Green', 'Dino Dark Orange', 'Dino Dark Red', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Medium Brown', 'Dino Medium Green']}, {'name': 'Unknown', 'colors': ['Black', 'Dino Light Brown', 'Dino Light Green', 'Dino Light Orange', 'Dino Light Yellow', 'Dino Medium Brown', 'Dino Medium Green', 'Light Grey']}]
       taming = {'nonViolent': True, 'violent': True, 'tamingIneffectiveness': 0.08, 'affinityNeeded0': 7500, 'affinityIncreasePL': 375, 'torporDepletionPS0': 0.75, 'wakeAffinityMult': 3, 'wakeFoodDeplMult': 2, 'foodConsumptionBase': 0.007716, 'foodConsumptionMult': 180.0011}
       TamedBaseHealthMultiplier = 0.96
       displayedStats = 927
