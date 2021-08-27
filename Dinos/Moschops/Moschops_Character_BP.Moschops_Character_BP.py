import sys,sce
class Moschops_Character_BP(sce.Dinos):
   def __init__(self):
       super().__init__(self)
       name = 'Moschops'
       blueprintPath = '/Game/PrimalEarth/Dinos/Moschops/Moschops_Character_BP.Moschops_Character_BP'
       fullStatsRaw = [[375, 0.2, 0.27, 0.5, 0], [300, 0.1, 0.1, 0, 0], [300, 0.06, 0, 0.5, 0], [150, 0.1, 0.1, 0, 0], [300, 0.1, 0.1, 0, 0.15], None, None, [200, 0.02, 0.04, 0, 0], [1, 0.05, 0.1, 1, 0.4], [1, 0, 0.01, 0.2, 0], None, None]
       immobilizedBy = ['Bola', 'Large Bear Trap']
       breeding = {'gestationTime': 0, 'incubationTime': 9472.92638, 'eggTempMin': 16, 'eggTempMax': 20, 'maturationTime': 175438.596, 'matingCooldownMin': 64800, 'matingCooldownMax': 172800}
       colors = [{'name': 'Unknown', 'colors': ['Black', 'Dino Dark Orange', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Medium Brown', 'DragonBase0']}, {'name': 'Unknown', 'colors': ['Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Dark Orange', 'Dino Dark Yellow', 'Dino Medium Brown']}, {'name': 'Unknown', 'colors': ['Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Dark Orange', 'Dino Dark Red', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Medium Brown']}, {'name': 'Unknown', 'colors': ['Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Dark Orange', 'Dino Dark Red', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Medium Brown']}, {'name': 'Unknown', 'colors': ['Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Dark Orange', 'Dino Dark Red', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Medium Brown']}, {'name': 'Unknown', 'colors': ['Black', 'Dino Dark Yellow', 'Dino Light Orange', 'Dino Medium Brown', 'DragonBase0', 'Light Grey']}]
       taming = {'nonViolent': True, 'violent': False, 'tamingIneffectiveness': 0.2, 'affinityNeeded0': 6000, 'affinityIncreasePL': 150, 'wakeAffinityMult': 2.5, 'wakeFoodDeplMult': 1.2, 'foodConsumptionBase': 0.001736, 'foodConsumptionMult': 176.0315}
       TamedBaseHealthMultiplier = 1
       displayedStats = 927
