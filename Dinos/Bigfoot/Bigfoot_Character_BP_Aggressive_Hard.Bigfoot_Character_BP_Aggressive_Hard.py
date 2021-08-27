import sys,sce
class Bigfoot_Character_BP_Aggressive_Hard(sce.BaseCreature):
   def __init__(self):
       super().__init__(self)
       name = 'Gigantopithecus'
       blueprintPath = '/Game/PrimalEarth/Dinos/Bigfoot/Bigfoot_Character_BP_Aggressive_Hard.Bigfoot_Character_BP_Aggressive_Hard'
       variants = ['Alpha', 'Boss']
       fullStatsRaw = [[1920, 0.1, 0.27, 0.5, 0], [300, 0.1, 0.1, 0, 0], [1100, 0.06, 0, 0.5, 0], [150, 0.1, 0.1, 0, 0], [1500, 0.1, 0.1, 0, 0], None, None, [220, 0.02, 0.04, 0, 0], [1, 0.04, 0.1, 0.5, 0.4], [1, 0, 0.01, 0.06, 0], None, None]
       altBaseStats = {'0': 640}
       immobilizedBy = []
       breeding = {'gestationTime': 23809.5238, 'incubationTime': 0, 'maturationTime': 277777.778, 'matingCooldownMin': 64800, 'matingCooldownMax': 172800}
       colors = [{'name': 'Unknown', 'colors': ['BigFoot0', 'BigFoot4', 'BigFoot5', 'Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Dark Orange', 'Dino Darker Grey', 'Dino Light Brown', 'Dino Light Orange', 'Dino Medium Brown', 'Light Grey']}, None, None, None, {'name': 'Unknown', 'colors': ['BigFoot0', 'BigFoot4', 'BigFoot5', 'Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Dark Orange', 'Dino Darker Grey', 'Dino Light Brown', 'Dino Light Orange', 'Dino Medium Brown', 'Light Grey']}, {'name': 'Unknown', 'colors': ['BigFoot0', 'BigFoot4', 'BigFoot5', 'Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Dark Orange', 'Dino Darker Grey', 'Dino Light Brown', 'Dino Light Orange', 'Dino Medium Brown', 'Light Grey']}]
       taming = {'nonViolent': True, 'violent': False, 'tamingIneffectiveness': 2.5, 'affinityNeeded0': 4600, 'affinityIncreasePL': 75, 'wakeAffinityMult': 1.65, 'wakeFoodDeplMult': 2, 'foodConsumptionBase': 0.004156, 'foodConsumptionMult': 176.0315}
       boneDamageAdjusters = {'c_jaw': 3.5, 'c_head': 3.5}
       TamedBaseHealthMultiplier = 1
       displayedStats = 927
