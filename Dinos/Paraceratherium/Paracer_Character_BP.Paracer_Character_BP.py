import sys,sce
class Paracer_Character_BP(sce.Dinos):
   def __init__(self):
       super().__init__(self)
       name = 'Paraceratherium'
       blueprintPath = '/Game/PrimalEarth/Dinos/Paraceratherium/Paracer_Character_BP.Paracer_Character_BP'
       fullStatsRaw = [[1026, 0.2, 0.172125, 0.5, 0], [300, 0.1, 0.1, 0, 0], [1300, 0.06, 0, 0.5, 0], [150, 0.1, 0.1, 0, 0], [6500, 0.1, 0.1, 0, 0], None, None, [850, 0.02, 0.04, 0, 0], [1, 0.05, 0.1, 0.5, 0.4], [1, 0, 0.01, 0, 0], None, None]
       immobilizedBy = ['Chain Bola', 'Large Bear Trap']
       breeding = {'gestationTime': 28571.4286, 'incubationTime': 0, 'maturationTime': 333333.333, 'matingCooldownMin': 64800, 'matingCooldownMax': 172800}
       colors = [{'name': 'Body', 'colors': ['BigFoot0', 'BigFoot4', 'BigFoot5', 'Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Dark Orange', 'Dino Darker Grey', 'Dino Light Brown', 'Dino Light Orange', 'Dino Medium Brown', 'Light Grey']}, None, None, None, {'name': 'Back', 'colors': ['BigFoot0', 'BigFoot4', 'BigFoot5', 'Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Dark Orange', 'Dino Darker Grey', 'Dino Light Brown', 'Dino Light Orange', 'Dino Medium Brown', 'Light Grey']}, {'name': 'Underside', 'colors': ['BigFoot0', 'BigFoot4', 'BigFoot5', 'Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Dark Orange', 'Dino Darker Grey', 'Dino Light Brown', 'Dino Light Orange', 'Dino Medium Brown', 'Light Grey']}]
       taming = {'nonViolent': False, 'violent': True, 'tamingIneffectiveness': 0.0923, 'affinityNeeded0': 6500, 'affinityIncreasePL': 325, 'torporDepletionPS0': 0.9025, 'foodConsumptionBase': 0.0035, 'foodConsumptionMult': 327.6474}
       TamedBaseHealthMultiplier = 1
       displayedStats = 927
