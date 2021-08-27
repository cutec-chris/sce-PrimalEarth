import sys,sce
class Turtle_Character_BP_Aberrant(sce.Aberration):
   def __init__(self):
       super().__init__(self)
       name = 'Aberrant Carbonemys'
       blueprintPath = '/Game/PrimalEarth/Dinos/Turtle/Turtle_Character_BP_Aberrant.Turtle_Character_BP_Aberrant'
       variants = ['Aberrant']
       fullStatsRaw = [[700, 0.2, 0.27, 0.5, 0], [200, 0.1, 0.1, 0, 0], [275, 0.06, 0, 0.5, 0], [150, 0.1, 0.1, 0, 0], [3000, 0.1, 0.1, 0, 0], None, None, [270, 0.02, 0.04, 0, 0], [1, 0.05, 0.1, 0.5, 0.4], [1, 0, 0.01, 0.7, 0], None, None]
       immobilizedBy = ['Chain Bola', 'Large Bear Trap', 'Plant Species Y']
       breeding = {'gestationTime': 0, 'incubationTime': 4499.64003, 'eggTempMin': 30, 'eggTempMax': 34, 'maturationTime': 83333.3333, 'matingCooldownMin': 64800, 'matingCooldownMax': 172800}
       colors = [{'name': 'Unknown', 'colors': ['Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Dark Green', 'Dino Dark Orange', 'Dino Dark Red', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Medium Brown', 'Dino Medium Green']}, {'name': 'Unknown', 'colors': ['Black', 'Dino Light Blue', 'Dino Light Brown', 'Dino Light Orange', 'Dino Light Purple', 'Dino Light Red', 'Dino Light Yellow', 'Dino Medium Brown', 'Light Grey']}, None, None, {'name': 'Unknown', 'colors': ['Black', 'Dark Grey', 'Dino Dark Blue', 'Dino Dark Brown', 'Dino Dark Orange', 'Dino Dark Purple', 'Dino Dark Red', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Medium Brown']}, {'name': 'Unknown', 'colors': ['Black', 'Dino Light Brown', 'Dino Light Green', 'Dino Light Orange', 'Dino Light Yellow', 'Dino Medium Brown', 'Dino Medium Green', 'Light Grey']}]
       taming = {'nonViolent': False, 'violent': True, 'tamingIneffectiveness': 0.2, 'affinityNeeded0': 3000, 'affinityIncreasePL': 150, 'torporDepletionPS0': 0.3, 'foodConsumptionBase': 0.003156, 'foodConsumptionMult': 352.0631}
       boneDamageAdjusters = {'c_neck5': 1, 'c_body': 0.2, 'c_tail1': 0.5, 'c_tail2': 0.5, 'c_tail3': 0.5}
       TamedBaseHealthMultiplier = 0.864
       displayedStats = 919
