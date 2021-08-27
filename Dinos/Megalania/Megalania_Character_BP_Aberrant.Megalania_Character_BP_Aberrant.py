import sys,sce
class Megalania_Character_BP_Aberrant(sce.Aberration):
   def __init__(self):
       super().__init__(self)
       name = 'Aberrant Megalania'
       blueprintPath = '/Game/PrimalEarth/Dinos/Megalania/Megalania_Character_BP_Aberrant.Megalania_Character_BP_Aberrant'
       variants = ['Aberrant']
       fullStatsRaw = [[480, 0.2, 0.27, 0.5, 0], [400, 0.1, 0.1, 0, 0], [700, 0.06, 0, 0.5, 0], [200, 0.1, 0.1, 0, 0], [1500, 0.1, 0.1, 0, 0.15], None, None, [400, 0.02, 0.04, 0, 0], [1, 0.05, 0.1, 0.4, 0.35], [1, 0, 0.01, 0.3, 0], None, None]
       immobilizedBy = ['Bola', 'Bear Trap', 'Plant Species Y']
       breeding = {'gestationTime': 0, 'incubationTime': 7199.42405, 'eggTempMin': 29, 'eggTempMax': 35, 'maturationTime': 133333.333, 'matingCooldownMin': 64800, 'matingCooldownMax': 172800}
       colors = [{'name': 'Body Main', 'colors': ['Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Dark Orange', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Light Brown', 'Dino Light Green', 'Dino Light Orange', 'Dino Light Yellow', 'Dino Medium Brown', 'Dino Medium Green', 'DragonGreen0', 'Light Grey']}, None, None, None, {'name': 'Stripes', 'colors': ['Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Dark Orange', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Light Brown', 'Dino Light Green', 'Dino Light Orange', 'Dino Light Yellow', 'Dino Medium Brown', 'Dino Medium Green', 'DragonBase0', 'DragonGreen1', 'DragonGreen3', 'Light Grey', 'WyvernBlue0', 'WyvernPurple1']}, {'name': 'Belly', 'colors': ['Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Dark Orange', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Light Brown', 'Dino Light Green', 'Dino Light Orange', 'Dino Light Yellow', 'Dino Medium Brown', 'Dino Medium Green', 'DragonBase1', 'DragonGreen1', 'DragonGreen3', 'Light Grey', 'WyvernBlue1', 'WyvernPurple1']}]
       taming = {'nonViolent': False, 'violent': True, 'tamingIneffectiveness': 3.5, 'affinityNeeded0': 4000, 'affinityIncreasePL': 85, 'torporDepletionPS0': 3.6, 'foodConsumptionBase': 0.001736, 'foodConsumptionMult': 199.984}
       TamedBaseHealthMultiplier = 0.96
       displayedStats = 927
