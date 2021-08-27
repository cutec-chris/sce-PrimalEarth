import sys,sce
class Lystro_Character_BP(sce.Dinos):
   def __init__(self):
       super().__init__(self)
       name = 'Lystrosaurus'
       blueprintPath = '/Game/PrimalEarth/Dinos/Lystrosaurus/Lystro_Character_BP.Lystro_Character_BP'
       fullStatsRaw = [[90, 0.2, 0.27, 0.5, 0], [100, 0.1, 0.1, 0, 0], [100, 0.06, 0, 0.5, 0], [215, 0.1, 0.1, 0, 0], [500, 0.1, 0.1, 0, 0.15], None, None, [90, 0.02, 0.04, 0, 0], [1, 0.05, 0.1, 0.5, 0.4], [1, 0, 0.01, 2, 0], None, None]
       immobilizedBy = ['Bola', 'Bear Trap', 'Plant Species Y']
       breeding = {'gestationTime': 0, 'incubationTime': 2999.76002, 'eggTempMin': 24, 'eggTempMax': 28, 'maturationTime': 55555.5556, 'matingCooldownMin': 64800, 'matingCooldownMax': 172800}
       colors = [{'name': 'Body', 'colors': ['Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Dark Green', 'Dino Dark Orange', 'Dino Dark Red', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Medium Brown', 'Dino Medium Green']}, None, None, None, {'name': 'Underside', 'colors': ['Black', 'Dark Grey', 'Dino Dark Blue', 'Dino Dark Brown', 'Dino Dark Green', 'Dino Dark Orange', 'Dino Dark Purple', 'Dino Dark Red', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Medium Brown', 'Dino Medium Green']}, {'name': 'Spine and Feet', 'colors': ['Black', 'Dino Light Brown', 'Dino Light Green', 'Dino Light Orange', 'Dino Light Yellow', 'Dino Medium Brown', 'Dino Medium Green', 'Light Grey']}]
       taming = {'nonViolent': True, 'violent': False, 'tamingIneffectiveness': 1.333333, 'affinityNeeded0': 2000, 'affinityIncreasePL': 22.5, 'wakeAffinityMult': 1.6, 'wakeFoodDeplMult': 1.1, 'foodConsumptionBase': 0.000868, 'foodConsumptionMult': 2880.184}
       boneDamageAdjusters = {'c_head': 3, 'c_neck3': 3}
       TamedBaseHealthMultiplier = 1
       displayedStats = 927
