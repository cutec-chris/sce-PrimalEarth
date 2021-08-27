import sys,sce
class Sarco_Character_BP_Aberrant(sce.Aberration):
   def __init__(self):
       super().__init__(self)
       name = 'Aberrant Sarco'
       blueprintPath = '/Game/PrimalEarth/Dinos/Sarco/Sarco_Character_BP_Aberrant.Sarco_Character_BP_Aberrant'
       variants = ['Aberrant']
       fullStatsRaw = [[400, 0.2, 0.27, 0.65, 0], [450, 0.1, 0.1, 0, 0], [400, 0.06, 0, 0.5, 0], [150, 0.1, 0.1, 0, 0], [1500, 0.1, 0.1, 0, 0], None, None, [300, 0.02, 0.04, 0, 0], [1, 0.05, 0.1, 0.8, 0.5], [1, 0, 0.01, 0.6, 0], None, None]
       immobilizedBy = ['Chain Bola', 'Large Bear Trap', 'Plant Species Y']
       breeding = {'gestationTime': 0, 'incubationTime': 8999.28006, 'eggTempMin': 30, 'eggTempMax': 34, 'maturationTime': 166666.667, 'matingCooldownMin': 64800, 'matingCooldownMax': 172800}
       colors = [{'name': 'Unknown', 'colors': ['Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Dark Green', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Light Yellow', 'Dino Medium Brown', 'Dino Medium Green']}, None, {'name': 'Unknown', 'colors': ['Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Dark Green', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Light Yellow', 'Dino Medium Brown', 'Dino Medium Green']}, {'name': 'Unknown', 'colors': ['Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Dark Green', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Light Yellow', 'Dino Medium Brown', 'Dino Medium Green']}, {'name': 'Unknown', 'colors': ['Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Dark Green', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Light Yellow', 'Dino Medium Brown', 'Dino Medium Green']}, {'name': 'Unknown', 'colors': ['Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Dark Green', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Light Yellow', 'Dino Medium Brown', 'Dino Medium Green']}]
       taming = {'nonViolent': False, 'violent': True, 'tamingIneffectiveness': 2.5, 'affinityNeeded0': 2000, 'affinityIncreasePL': 75, 'torporDepletionPS0': 0.3, 'foodConsumptionBase': 0.001578, 'foodConsumptionMult': 211.2379}
       TamedBaseHealthMultiplier = 0.96
       displayedStats = 919
