import sys,sce
class Chalico_Character_BP(sce.Dinos):
   def __init__(self):
       super().__init__(self)
       name = 'Chalicotherium'
       blueprintPath = '/Game/PrimalEarth/Dinos/Chalicotherium/Chalico_Character_BP.Chalico_Character_BP'
       fullStatsRaw = [[600, 0.2, 0.27, 0.5, 0], [300, 0.1, 0.1, 0, 0], [500, 0.06, 0, 0.5, 0], [150, 0.1, 0.1, 0, 0], [4000, 0.1, 0.1, 0, 0], None, None, [400, 0.02, 0.04, 0, 0], [1, 0.05, 0.1, 0.5, 0.4], [1, 0, 0.01, 0, 0], None, None]
       immobilizedBy = ['Chain Bola', 'Large Bear Trap', 'Plant Species Y']
       breeding = {'gestationTime': 28571.4286, 'incubationTime': 0, 'maturationTime': 296296.296, 'matingCooldownMin': 64800, 'matingCooldownMax': 172800}
       colors = [{'name': 'Main Body', 'colors': ['BigFoot0', 'BigFoot5', 'Black', 'Dark Grey', 'DarkWolfFur', 'Dino Dark Brown', 'Dino Dark Orange', 'Dino Dark Red', 'Dino Darker Grey', 'Dino Medium Brown']}, None, None, None, {'name': 'Fur Highlights', 'colors': ['Dark Grey', 'DarkWolfFur', 'Dino Dark Brown', 'Dino Dark Red', 'Dino Darker Grey', 'Dino Medium Brown', 'None']}, {'name': 'Stripes and Belly', 'colors': ['BigFoot4', 'Black', 'Dino Light Brown', 'Dino Light Orange', 'Dino Medium Brown', 'Light Grey', 'WolfFur']}]
       taming = {'nonViolent': True, 'violent': False, 'tamingIneffectiveness': 0.16, 'affinityNeeded0': 5000, 'affinityIncreasePL': 275, 'wakeAffinityMult': 1.6, 'wakeFoodDeplMult': 2, 'foodConsumptionBase': 0.003156, 'foodConsumptionMult': 352.0631}
       TamedBaseHealthMultiplier = 1
       displayedStats = 927
