import sys,sce
class Beaver_Character_BP(sce.Dinos):
   def __init__(self):
       super().__init__(self)
       name = 'Castoroides'
       blueprintPath = '/Game/PrimalEarth/Dinos/Beaver/Beaver_Character_BP.Beaver_Character_BP'
       fullStatsRaw = [[450, 0.2, 0.27, 0.5, 0], [180, 0.1, 0.1, 0, 0], [350, 0.06, 0, 0.5, 0], [750, 0.1, 0.1, 0, 0], [2000, 0.1, 0.1, 0, 0], None, None, [300, 0.02, 0.04, 0, 0], [1, 0.04, 0.1, 0.5, 0.4], [1, 0, 0.01, 0.7, 0], None, None]
       immobilizedBy = ['Bola', 'Large Bear Trap']
       breeding = {'gestationTime': 28571.4286, 'incubationTime': 0, 'maturationTime': 222222.222, 'matingCooldownMin': 64800, 'matingCooldownMax': 142800}
       colors = [{'name': 'Body', 'colors': ['BigFoot0', 'BigFoot4', 'BigFoot5', 'Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Dark Orange', 'Dino Darker Grey', 'Dino Light Brown', 'Dino Light Orange', 'Dino Medium Brown', 'Light Grey']}, {'name': 'Feet', 'colors': ['BigFoot0', 'BigFoot4', 'BigFoot5', 'Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Dark Orange', 'Dino Darker Grey', 'Dino Light Brown', 'Dino Light Orange', 'Dino Medium Brown', 'Light Grey']}, None, None, {'name': 'Stripe', 'colors': ['BigFoot0', 'BigFoot4', 'BigFoot5', 'Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Dark Orange', 'Dino Darker Grey', 'Dino Light Brown', 'Dino Light Orange', 'Dino Medium Brown', 'Light Grey']}, {'name': 'Tail', 'colors': ['BigFoot0', 'BigFoot4', 'BigFoot5', 'Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Dark Orange', 'Dino Darker Grey', 'Dino Light Brown', 'Dino Light Orange', 'Dino Medium Brown', 'Light Grey']}]
       taming = {'nonViolent': False, 'violent': True, 'tamingIneffectiveness': 0.3, 'affinityNeeded0': 2000, 'affinityIncreasePL': 100, 'torporDepletionPS0': 1.5, 'foodConsumptionBase': 0.002314, 'foodConsumptionMult': 160.0563}
       TamedBaseHealthMultiplier = 1
       displayedStats = 927
