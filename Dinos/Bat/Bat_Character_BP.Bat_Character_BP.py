import sys,sce
class Bat_Character_BP(sce.Dinos):
   def __init__(self):
       super().__init__(self)
       name = 'Onyc'
       blueprintPath = '/Game/PrimalEarth/Dinos/Bat/Bat_Character_BP.Bat_Character_BP'
       isFlyer = True
       fullStatsRaw = [[250, 0.2, 0.27, 0.5, 0], [100, 0.1, 0.1, 0, 0], [200, 0.06, 0, 0.5, 0], [150, 0.1, 0.1, 0, 0], [1500, 0.1, 0.1, 0, 0], None, None, [50, 0.02, 0.04, 0, 0], [1, 0.05, 0.1, 0.5, 0.4], [1, 0, 0.01, 0, 0], None, None]
       immobilizedBy = []
       breeding = {'gestationTime': 14285.7143, 'incubationTime': 0, 'maturationTime': 101010.101, 'matingCooldownMin': 64800, 'matingCooldownMax': 172800}
       colors = [{'name': 'Main Body', 'colors': ['Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Dark Orange', 'Dino Dark Red', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Medium Brown']}, {'name': 'Claws', 'colors': ['Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Dark Orange', 'Dino Dark Red', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Medium Brown']}, {'name': 'Membrane Shading', 'colors': ['Black', 'Dino Light Blue', 'Dino Light Brown', 'Dino Light Orange', 'Dino Light Yellow', 'Dino Medium Brown', 'Light Grey']}, None, {'name': 'Abdomen and Legs', 'colors': ['Black', 'Dino Light Blue', 'Dino Light Brown', 'Dino Light Orange', 'Dino Light Yellow', 'Dino Medium Brown', 'Light Grey']}, {'name': 'Wing Membrane', 'colors': ['Black', 'Dino Light Blue', 'Dino Light Brown', 'Dino Light Orange', 'Dino Light Yellow', 'Dino Medium Brown', 'Light Grey']}]
       taming = {'nonViolent': True, 'violent': False, 'tamingIneffectiveness': 2.5, 'affinityNeeded0': 3000, 'affinityIncreasePL': 90, 'wakeAffinityMult': 1, 'wakeFoodDeplMult': 2, 'foodConsumptionBase': 0.002893, 'foodConsumptionMult': 192.0344}
       TamedBaseHealthMultiplier = 1
       displayedStats = 927
