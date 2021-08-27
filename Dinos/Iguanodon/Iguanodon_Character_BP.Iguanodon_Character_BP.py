import sys,sce
class Iguanodon_Character_BP(sce.Dinos):
   def __init__(self):
       super().__init__(self)
       name = 'Iguanodon'
       blueprintPath = '/Game/PrimalEarth/Dinos/Iguanodon/Iguanodon_Character_BP.Iguanodon_Character_BP'
       fullStatsRaw = [[250, 0.2, 0.27, 0.5, 0], [200, 0.1, 0.1, 0, 0], [210, 0.06, 0, 0.5, 0], [150, 0.1, 0.1, 0, 0], [1800, 0.1, 0.1, 0, 0], None, None, [375, 0.02, 0.04, 0, 0], [1, 0.05, 0.1, 0.5, 0.4], [1, 0, 0.02, 0, 0], None, None]
       immobilizedBy = ['Bola', 'Bear Trap', 'Large Bear Trap', 'Plant Species Y']
       breeding = {'gestationTime': 0, 'incubationTime': 5142.44575, 'eggTempMin': 24, 'eggTempMax': 28, 'maturationTime': 166666.667, 'matingCooldownMin': 64800, 'matingCooldownMax': 172800}
       colors = [{'name': 'MainBody', 'colors': ['Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Dark Orange', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Light Brown', 'Dino Light Green', 'Dino Light Orange', 'Dino Light Yellow', 'Dino Medium Brown', 'DragonBase0', 'DragonGreen0', 'DragonGreen1', 'Light Grey', 'WyvernBlue1']}, None, None, None, {'name': 'Stripes', 'colors': ['Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Dark Green', 'Dino Dark Orange', 'Dino Dark Red', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Medium Brown', 'Dino Medium Green']}, {'name': 'Highlights and Belly', 'colors': ['BigFoot0', 'Black', 'Dino Light Brown', 'Dino Light Green', 'Dino Light Orange', 'Dino Light Yellow', 'DragonBase1', 'DragonGreen2', 'Light Grey']}]
       taming = {'nonViolent': False, 'violent': True, 'tamingIneffectiveness': 0.4, 'affinityNeeded0': 2800, 'affinityIncreasePL': 140, 'torporDepletionPS0': 0.3, 'foodConsumptionBase': 0.001929, 'foodConsumptionMult': 864.0056}
       boneDamageAdjusters = {'c_jaw': 2, 'c_head': 2}
       TamedBaseHealthMultiplier = 1
       displayedStats = 927
