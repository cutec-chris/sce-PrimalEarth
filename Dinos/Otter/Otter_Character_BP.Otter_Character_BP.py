import sys,sce
class Otter_Character_BP(sce.Dinos):
   def __init__(self):
       super().__init__(self)
       name = 'Otter'
       blueprintPath = '/Game/PrimalEarth/Dinos/Otter/Otter_Character_BP.Otter_Character_BP'
       fullStatsRaw = [[40, 0.2, 0.27, 0.5, 0], [180, 0.1, 0.1, 0, 0], [350, 0.06, 0, 0.5, 0], [600, 0.1, 0.1, 0, 0], [400, 0.1, 0.1, 0, 0], None, None, [30, 0.02, 0.04, 0, 0], [1, 0.04, 0.1, 0.5, 0.4], [1, 0, 0.01, 0.7, 0], None, None]
       immobilizedBy = ['Bola', 'Bear Trap', 'Plant Species Y']
       breeding = {'gestationTime': 28571.4286, 'incubationTime': 0, 'maturationTime': 75757.5758, 'matingCooldownMin': 64800, 'matingCooldownMax': 142800}
       colors = [{'name': 'Body Main', 'colors': ['BigFoot0', 'BigFoot4', 'BigFoot5', 'Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Dark Orange', 'Dino Darker Grey', 'Dino Light Brown', 'Dino Light Orange', 'Dino Medium Brown', 'Light Grey']}, None, None, None, {'name': 'Body Stripes and Highlights', 'colors': ['BigFoot0', 'BigFoot4', 'BigFoot5', 'Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Dark Orange', 'Dino Darker Grey', 'Dino Medium Brown', 'Light Grey']}, {'name': 'Underbelly', 'colors': ['BigFoot0', 'BigFoot4', 'BigFoot5', 'Dino Light Brown', 'Dino Light Orange', 'Dino Medium Brown', 'Light Grey']}]
       taming = {'nonViolent': True, 'violent': False, 'tamingIneffectiveness': 8.333333, 'affinityNeeded0': 1200, 'affinityIncreasePL': 25, 'wakeAffinityMult': 1.6, 'wakeFoodDeplMult': 2, 'foodConsumptionBase': 0.002314, 'foodConsumptionMult': 160.0563}
       TamedBaseHealthMultiplier = 1
       displayedStats = 927
