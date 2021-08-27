import sys,sce
class Troodon_Character_BP(sce.Dinos):
   def __init__(self):
       super().__init__(self)
       name = 'Troodon'
       blueprintPath = '/Game/PrimalEarth/Dinos/Troodon/Troodon_Character_BP.Troodon_Character_BP'
       fullStatsRaw = [[200, 0.2, 0.27, 0.5, 0], [150, 0.1, 0.1, 0, 0], [180, 0.06, 0, 0.5, 0], [150, 0.1, 0.1, 0, 0], [200, 0.1, 0.1, 0, 0], None, None, [140, 0.02, 0.04, 0, 0], [1, 0.05, 0.1, 0.5, 0.4], [1, 0, 0.01, 0.2, 0], None, None]
       altBaseStats = {'4': 100}
       immobilizedBy = ['Bola', 'Bear Trap', 'Plant Species Y']
       breeding = {'gestationTime': 0, 'incubationTime': 4090.58184, 'eggTempMin': 28, 'eggTempMax': 32, 'maturationTime': 75757.5758, 'matingCooldownMin': 64800, 'matingCooldownMax': 172800}
       colors = [{'name': 'Main Body', 'colors': ['Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Dark Orange', 'Dino Dark Red', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Medium Brown', 'DragonGreen3', 'WyvernBlue1']}, None, None, None, {'name': 'Body Highlights and Feathers', 'colors': ['Black', 'Dino Light Brown', 'Dino Light Orange', 'Dino Light Yellow', 'Dino Medium Brown', 'DragonBase0', 'DragonGreen3', 'Light Grey', 'WyvernBlue0']}, {'name': 'Belly', 'colors': ['Black', 'Dark Grey', 'Dino Light Blue', 'Dino Light Brown', 'Dino Light Orange', 'Dino Light Yellow', 'Dino Medium Brown', 'DragonGreen2', 'Light Grey']}]
       taming = {'nonViolent': True, 'violent': False, 'tamingIneffectiveness': 8.333333, 'affinityNeeded0': 480, 'affinityIncreasePL': 45, 'wakeAffinityMult': 1.6, 'wakeFoodDeplMult': 2, 'foodConsumptionBase': 0.001543, 'foodConsumptionMult': 648.0881}
       boneDamageAdjusters = {'c_head': 3, 'c_jaw': 3, 'c_neck3': 3}
       TamedBaseHealthMultiplier = 1
       displayedStats = 927
