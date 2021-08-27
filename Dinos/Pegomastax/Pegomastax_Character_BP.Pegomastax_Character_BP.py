import sys,sce
class Pegomastax_Character_BP(sce.Dinos):
   def __init__(self):
       super().__init__(self)
       name = 'Pegomastax'
       blueprintPath = '/Game/PrimalEarth/Dinos/Pegomastax/Pegomastax_Character_BP.Pegomastax_Character_BP'
       fullStatsRaw = [[120, 0.2, 0.27, 0.5, 0], [100, 0.1, 0.1, 0, 0], [30, 0.06, 0, 0.5, 0], [150, 0.1, 0.1, 0, 0], [450, 0.1, 0.1, 0, 0.15], None, None, [55, 0.02, 0.04, 0, 0], [1, 0.05, 0.1, 1, 0.4], [1, 0, 0.01, 0.5, 0], None, None]
       altBaseStats = {'0': 200}
       immobilizedBy = ['Bola', 'Bear Trap', 'Plant Species Y']
       breeding = {'gestationTime': 0, 'incubationTime': 4090.58184, 'eggTempMin': 28, 'eggTempMax': 32, 'maturationTime': 111111.111, 'matingCooldownMin': 64800, 'matingCooldownMax': 172800}
       colors = [{'name': 'Body Main', 'colors': ['Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Dark Orange', 'Dino Dark Red', 'Dino Dark Yellow', 'Dino Light Blue', 'Dino Light Orange', 'Dino Light Yellow', 'Dino Medium Brown']}, {'name': 'Quills', 'colors': ['Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Dark Green', 'Dino Dark Orange', 'Dino Dark Red', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Medium Brown', 'Dino Medium Green']}, {'name': 'Beak', 'colors': ['Dino Light Blue', 'Dino Light Orange', 'Dino Light Yellow', 'Dino Medium Brown', 'DragonBase1', 'DragonGreen2', 'WyvernPurple1']}, None, {'name': 'Back Fur', 'colors': ['BigFoot0', 'BigFoot5', 'Black', 'Dark Grey', 'DarkWolfFur', 'Dino Dark Brown', 'Dino Darker Grey', 'Dino Medium Brown', 'WolfFur']}, {'name': 'Limb Highlights', 'colors': ['Black', 'Dino Albino', 'Dino Light Blue', 'Dino Light Brown', 'Dino Light Orange', 'Dino Light Yellow', 'Dino Medium Brown', 'Light Grey']}]
       taming = {'nonViolent': True, 'violent': False, 'tamingIneffectiveness': 1.333333, 'affinityNeeded0': 1900, 'affinityIncreasePL': 35, 'wakeAffinityMult': 1.6, 'wakeFoodDeplMult': 2, 'foodConsumptionBase': 0.000868, 'foodConsumptionMult': 2880.184}
       boneDamageAdjusters = {'c_head': 3, 'c_neck3': 3}
       TamedBaseHealthMultiplier = 1
       displayedStats = 927
