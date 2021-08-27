import sys,sce
class Doed_Character_BP(sce.Dinos):
   def __init__(self):
       super().__init__(self)
       name = 'Doedicurus'
       blueprintPath = '/Game/PrimalEarth/Dinos/Doedicurus/Doed_Character_BP.Doed_Character_BP'
       fullStatsRaw = [[850, 0.2, 0.27, 0.5, 0], [300, 0.1, 0.1, 0, 0], [800, 0.06, 0, 0.5, 0], [150, 0.1, 0.1, 0, 0], [3000, 0.1, 0.1, 0, 0.15], None, None, [250, 0.02, 0.04, 0, 0], [1, 0.05, 0.1, 1, 0.4], [1, 0, 0.02, 0.6, 0], None, None]
       immobilizedBy = ['Chain Bola', 'Large Bear Trap']
       breeding = {'gestationTime': 17857.1429, 'incubationTime': 0, 'maturationTime': 208333.333, 'matingCooldownMin': 64800, 'matingCooldownMax': 172800}
       colors = [{'name': 'Shell and Plates', 'colors': ['BigFoot0', 'BigFoot4', 'BigFoot5', 'Black', 'Dark Grey', 'Dino Dark Blue', 'Dino Dark Brown', 'Dino Dark Orange', 'Dino Darker Grey', 'Dino Light Brown', 'Dino Light Orange', 'Dino Medium Brown', 'Light Grey']}, {'name': 'Spikes and Claws', 'colors': ['BigFoot0', 'BigFoot4', 'BigFoot5', 'Black', 'Dark Grey', 'Dino Dark Blue', 'Dino Dark Brown', 'Dino Dark Orange', 'Dino Darker Grey', 'Dino Light Brown', 'Dino Light Orange', 'Dino Medium Brown', 'Light Grey']}, None, None, {'name': 'Shell Patterning', 'colors': ['BigFoot0', 'BigFoot4', 'BigFoot5', 'Black', 'Dark Grey', 'Dino Dark Blue', 'Dino Dark Brown', 'Dino Dark Orange', 'Dino Darker Grey', 'Dino Light Brown', 'Dino Light Orange', 'Dino Medium Brown', 'Light Grey']}, {'name': 'Underside', 'colors': ['BigFoot0', 'BigFoot4', 'BigFoot5', 'Black', 'Dark Grey', 'Dino Dark Blue', 'Dino Dark Brown', 'Dino Dark Orange', 'Dino Darker Grey', 'Dino Light Brown', 'Dino Light Orange', 'Dino Medium Brown', 'Light Grey']}]
       taming = {'nonViolent': False, 'violent': True, 'tamingIneffectiveness': 0.2, 'affinityNeeded0': 4000, 'affinityIncreasePL': 150, 'torporDepletionPS0': 0.75, 'foodConsumptionBase': 0.003156, 'foodConsumptionMult': 176.0315}
       TamedBaseHealthMultiplier = 0.9
       displayedStats = 927
