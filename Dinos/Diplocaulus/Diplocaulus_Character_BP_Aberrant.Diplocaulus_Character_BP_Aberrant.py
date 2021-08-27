import sys,sce
class Diplocaulus_Character_BP_Aberrant(sce.Aberration):
   def __init__(self):
       super().__init__(self)
       name = 'Aberrant Diplocaulus'
       blueprintPath = '/Game/PrimalEarth/Dinos/Diplocaulus/Diplocaulus_Character_BP_Aberrant.Diplocaulus_Character_BP_Aberrant'
       variants = ['Aberrant']
       fullStatsRaw = [[250, 0.2, 0.27, 0.5, 0], [165, 0.1, 0.1, 0, 0], [220, 0.06, 0, 0.5, 0], [1050, 0.1, 0.1, 0, 0], [1500, 0.1, 0.1, 0, 0], None, None, [150, 0.02, 0.04, 0, 0], [1, 0.05, 0.1, 0.5, 0.25], [1, 0, 0.01, 0, 0], None, None]
       immobilizedBy = ['Bola', 'Bear Trap', 'Plant Species Y']
       breeding = {'gestationTime': 0, 'incubationTime': 17998.5601, 'eggTempMin': -75, 'eggTempMax': 75, 'maturationTime': 133333.333, 'matingCooldownMin': 64800, 'matingCooldownMax': 172800}
       colors = [{'name': 'Body', 'colors': ['Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Dark Green', 'Dino Dark Orange', 'Dino Dark Red', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Medium Brown', 'Dino Medium Green']}, {'name': 'Fins', 'colors': ['Black', 'Dino Dark Blue', 'Dino Dark Green', 'Dino Dark Orange', 'Dino Dark Purple', 'Dino Dark Red', 'Dino Dark Yellow', 'Dino Light Blue', 'Dino Light Green', 'Dino Light Orange', 'Dino Light Purple', 'Dino Light Red', 'Dino Light Yellow', 'Dino Medium Green']}, None, None, {'name': 'Body Highlights', 'colors': ['Black', 'Dino Dark Blue', 'Dino Dark Green', 'Dino Dark Orange', 'Dino Dark Purple', 'Dino Dark Red', 'Dino Dark Yellow', 'Dino Light Blue', 'Dino Light Green', 'Dino Light Orange', 'Dino Light Purple', 'Dino Light Red', 'Dino Light Yellow', 'Dino Medium Green']}, {'name': 'Underbelly', 'colors': ['Black', 'Dino Light Blue', 'Dino Light Brown', 'Dino Light Green', 'Dino Light Orange', 'Dino Light Yellow', 'Dino Medium Brown', 'Dino Medium Green', 'Light Grey']}]
       taming = {'nonViolent': False, 'violent': True, 'tamingIneffectiveness': 2.5, 'affinityNeeded0': 2000, 'affinityIncreasePL': 75, 'torporDepletionPS0': 0.3, 'foodConsumptionBase': 0.001543, 'foodConsumptionMult': 225}
       TamedBaseHealthMultiplier = 0.96
       displayedStats = 927
