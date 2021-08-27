import sys,sce
class Achatina_Character_BP_Aberrant(sce.Aberration):
   def __init__(self):
       super().__init__(self)
       name = 'Aberrant Achatina'
       blueprintPath = '/Game/PrimalEarth/Dinos/Achatina/Achatina_Character_BP_Aberrant.Achatina_Character_BP_Aberrant'
       variants = ['Aberrant']
       fullStatsRaw = [[75, 0.2, 0.27, 0.5, 0], [100, 0.1, 0.1, 0, 0], [50, 0.06, 0, 0.5, 0], [150, 0.1, 0.1, 0, 0], [450, 0.1, 0.1, 0, 0], None, None, [150, 0.02, 0.04, 0, 0], [1, 0.05, 0.1, 0.5, 0.4], [1, 0, 0.01, 0, 0], None, None]
       immobilizedBy = ['Bola', 'Bear Trap', 'Plant Species Y']
       noGender = True
       colors = [{'name': 'Unknown', 'colors': ['DarkWolfFur', 'Dino Dark Brown', 'Dino Dark Orange', 'Dino Medium Brown', 'DragonBase0', 'DragonBase1', 'WyvernPurple0']}, {'name': 'Unknown', 'colors': ['Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Dark Orange', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Light Blue', 'Dino Light Brown', 'Dino Light Orange', 'Dino Light Purple', 'Dino Light Red', 'Dino Light Yellow', 'Dino Medium Brown', 'Light Grey']}, None, {'name': 'Unknown', 'colors': ['Dino Light Blue', 'Dino Light Brown', 'Dino Light Green', 'Dino Light Orange', 'Dino Light Purple', 'Dino Light Red', 'Dino Light Yellow', 'Dino Medium Brown', 'DragonBase1']}, {'name': 'Unknown', 'colors': ['DarkWolfFur', 'Dino Light Brown', 'Dino Light Green', 'Dino Light Orange', 'Dino Light Purple', 'Dino Light Red', 'Dino Light Yellow', 'WyvernPurple1']}, {'name': 'Unknown', 'colors': ['Dino Light Green', 'Dino Light Orange', 'Dino Light Purple', 'Dino Light Red', 'Dino Light Yellow', 'Dino Medium Brown', 'WyvernPurple1']}]
       taming = {'nonViolent': False, 'violent': True, 'tamingIneffectiveness': 0.2, 'affinityNeeded0': 4000, 'affinityIncreasePL': 150, 'torporDepletionPS0': 0.3, 'foodConsumptionBase': 0.001736, 'foodConsumptionMult': 864.0553}
       boneDamageAdjusters = {'c_neck3': 1, 'c_tail1': 0.5, 'joint17': 0.1}
       TamedBaseHealthMultiplier = 0.96
       displayedStats = 919
