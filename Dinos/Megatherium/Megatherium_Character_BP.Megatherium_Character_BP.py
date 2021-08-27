import sys,sce
class Megatherium_Character_BP(sce.Dinos):
   def __init__(self):
       super().__init__(self)
       name = 'Megatherium'
       blueprintPath = '/Game/PrimalEarth/Dinos/Megatherium/Megatherium_Character_BP.Megatherium_Character_BP'
       fullStatsRaw = [[740, 0.2, 0.27, 0.5, 0], [400, 0.1, 0.1, 0, 0], [1000, 0.06, 0, 0.5, 0], [270, 0.1, 0.1, 0, 0], [3000, 0.1, 0.1, 0, 0], None, None, [725, 0.02, 0.045, 0, 0], [1, 0.05, 0.1, 0.5, 0.4], [1, 0, 0.01, 0, 0], None, None]
       immobilizedBy = ['Chain Bola', 'Large Bear Trap']
       breeding = {'gestationTime': 28571.4286, 'incubationTime': 0, 'maturationTime': 333333.333, 'matingCooldownMin': 64800, 'matingCooldownMax': 172800}
       colors = [{'name': 'BodyMain', 'colors': ['BigFoot0', 'BigFoot4', 'BigFoot5', 'Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Dark Orange', 'Dino Darker Grey', 'Dino Light Brown', 'Dino Light Orange', 'Dino Medium Brown', 'Light Grey']}, None, None, None, None, {'name': 'Feet and Hands', 'colors': ['BigFoot0', 'BigFoot4', 'BigFoot5', 'Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Darker Grey', 'Dino Light Brown', 'Dino Light Orange', 'Dino Medium Brown', 'Light Grey']}]
       taming = {'nonViolent': False, 'violent': True, 'tamingIneffectiveness': 1.25, 'affinityNeeded0': 5000, 'affinityIncreasePL': 130, 'torporDepletionPS0': 0.9, 'foodConsumptionBase': 0.003156, 'foodConsumptionMult': 150}
       TamedBaseHealthMultiplier = 1
       displayedStats = 927
