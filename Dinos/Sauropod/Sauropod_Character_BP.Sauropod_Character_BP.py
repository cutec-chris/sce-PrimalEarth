import sys,sce
class Sauropod_Character_BP(sce.Dinos):
   def __init__(self):
       super().__init__(self)
       name = 'Brontosaurus'
       blueprintPath = '/Game/PrimalEarth/Dinos/Sauropod/Sauropod_Character_BP.Sauropod_Character_BP'
       fullStatsRaw = [[2070, 0.2, 0.1254, 0.5, 0], [240, 0.1, 0.1, 0, 0], [2000, 0.06, 0, 0.5, 0], [150, 0.1, 0.1, 0, 0], [10000, 0.1, 0.1, 0, 0], None, None, [1600, 0.02, 0.04, 0, 0], [1, 0.05, 0.1, 0.5, 0.4], [1, 0, 0.02, 0, 0], None, None]
       immobilizedBy = ['Large Bear Trap']
       breeding = {'gestationTime': 0, 'incubationTime': 17998.5601, 'eggTempMin': 28, 'eggTempMax': 31, 'maturationTime': 333333.333, 'matingCooldownMin': 64800, 'matingCooldownMax': 172800}
       colors = [{'name': 'Body', 'colors': ['Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Dark Green', 'Dino Dark Orange', 'Dino Dark Red', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Medium Brown', 'Dino Medium Green']}, {'name': 'Spine', 'colors': ['Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Dark Green', 'Dino Dark Orange', 'Dino Dark Red', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Medium Brown', 'Dino Medium Green']}, None, None, {'name': 'Back', 'colors': ['Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Dark Green', 'Dino Dark Orange', 'Dino Dark Red', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Medium Brown', 'Dino Medium Green']}, {'name': 'Legs', 'colors': ['Black', 'Dino Light Brown', 'Dino Light Green', 'Dino Light Orange', 'Dino Light Yellow', 'Dino Medium Brown', 'Dino Medium Green', 'Light Grey']}]
       taming = {'nonViolent': False, 'violent': True, 'tamingIneffectiveness': 0.06, 'affinityNeeded0': 10000, 'affinityIncreasePL': 500, 'torporDepletionPS0': 0.3, 'foodConsumptionBase': 0.007716, 'foodConsumptionMult': 180.0011}
       TamedBaseHealthMultiplier = 0.9
       displayedStats = 927
