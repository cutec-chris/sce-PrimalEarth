import sys,sce
class Pachyrhino_Character_BP(sce.Dinos):
   def __init__(self):
       super().__init__(self)
       name = 'Pachyrhinosaurus'
       blueprintPath = '/Game/PrimalEarth/Dinos/Pachyrhinosaurus/Pachyrhino_Character_BP.Pachyrhino_Character_BP'
       fullStatsRaw = [[375, 0.2, 0.27, 0.5, 0], [150, 0.1, 0.1, 0, 0], [250, 0.06, 0, 0.5, 0], [150, 0.1, 0.1, 0, 0], [3000, 0.1, 0.1, 0, 0], None, None, [365, 0.02, 0.04, 0, 0], [1, 0.05, 0.1, 0.5, 0.4], [1, 0, 0.01, 0, 0], None, None]
       immobilizedBy = ['Chain Bola', 'Large Bear Trap', 'Plant Species Y']
       breeding = {'gestationTime': 0, 'incubationTime': 8999.28006, 'eggTempMin': 22, 'eggTempMax': 28, 'maturationTime': 166666.667, 'matingCooldownMin': 64800, 'matingCooldownMax': 172800}
       colors = [{'name': 'Body', 'colors': ['Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Dark Orange', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Medium Brown', 'DragonBase0', 'DragonGreen0', 'DragonGreen1']}, None, {'name': 'Spikes and Horns', 'colors': ['Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Dark Orange', 'Dino Dark Red', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Medium Brown', 'DragonGreen0', 'DragonGreen1']}, None, {'name': 'Back', 'colors': ['Black', 'Dark Grey', 'Dino Dark Blue', 'Dino Dark Brown', 'Dino Dark Orange', 'Dino Dark Purple', 'Dino Dark Red', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Medium Brown', 'DragonGreen0', 'DragonGreen1']}, {'name': 'Face, Legs, and Underside', 'colors': ['Black', 'Dino Light Brown', 'Dino Light Green', 'Dino Light Orange', 'Dino Light Yellow', 'Dino Medium Brown', 'DragonGreen2', 'Light Grey']}]
       taming = {'nonViolent': False, 'violent': True, 'tamingIneffectiveness': 0.2, 'affinityNeeded0': 4500, 'affinityIncreasePL': 175, 'torporDepletionPS0': 3.5, 'foodConsumptionBase': 0.003156, 'foodConsumptionMult': 352.0631}
       boneDamageAdjusters = {'c_head': 0.25, 'c_jaw': 0.25}
       TamedBaseHealthMultiplier = 1
       displayedStats = 927
