import sys,sce
class Monkey_Character_BP_Aggressive_Hard(sce.BaseCreature):
   def __init__(self):
       super().__init__(self)
       name = 'Mesopithecus'
       blueprintPath = '/Game/PrimalEarth/Dinos/Monkey/Monkey_Character_BP_Aggressive_Hard.Monkey_Character_BP_Aggressive_Hard'
       variants = ['Alpha', 'Boss']
       fullStatsRaw = [[345, 0.2, 0.27, 0.5, 0], [100, 0.1, 0.1, 0, 0], [60, 0.06, 0, 0.5, 0], [150, 0.1, 0.1, 0, 0], [450, 0.1, 0.1, 0, 0.15], None, None, [70, 0.02, 0.04, 0, 0], [1, 0.05, 0.1, 1, 0.4], [1, 0, 0.01, 1.3, 0], None, None]
       altBaseStats = {'0': 115}
       immobilizedBy = []
       breeding = {'gestationTime': 9523.80952, 'incubationTime': 0, 'maturationTime': 111111.111, 'matingCooldownMin': 64800, 'matingCooldownMax': 172800}
       colors = [{'name': 'Unknown', 'colors': ['BigFoot0', 'BigFoot4', 'BigFoot5', 'Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Dark Orange', 'Dino Darker Grey', 'Dino Light Brown', 'Dino Light Orange', 'Dino Medium Brown', 'Light Grey']}, None, {'name': 'Unknown', 'colors': ['BigFoot0', 'BigFoot4', 'BigFoot5', 'Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Dark Orange', 'Dino Darker Grey', 'Dino Light Blue', 'Dino Light Brown', 'Dino Light Orange', 'Dino Light Purple', 'Dino Medium Brown', 'Light Grey']}, None, {'name': 'Unknown', 'colors': ['BigFoot0', 'BigFoot4', 'BigFoot5', 'Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Dark Orange', 'Dino Darker Grey', 'Dino Light Brown', 'Dino Light Orange', 'Dino Medium Brown', 'Light Grey']}, {'name': 'Unknown', 'colors': ['BigFoot0', 'BigFoot4', 'BigFoot5', 'Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Dark Orange', 'Dino Darker Grey', 'Dino Light Brown', 'Dino Light Orange', 'Dino Medium Brown', 'Light Grey']}]
       taming = {'nonViolent': True, 'violent': False, 'tamingIneffectiveness': 2.5, 'affinityNeeded0': 2200, 'affinityIncreasePL': 65, 'wakeAffinityMult': 1.65, 'wakeFoodDeplMult': 2, 'foodConsumptionBase': 0.000868, 'foodConsumptionMult': 2880.184}
       boneDamageAdjusters = {'c_head': 3, 'c_neck': 3}
       TamedBaseHealthMultiplier = 1
       displayedStats = 927
