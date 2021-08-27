import sys,sce
class Manta_Character_BP(sce.Dinos):
   def __init__(self):
       super().__init__(self)
       name = 'Manta'
       blueprintPath = '/Game/PrimalEarth/Dinos/Manta/Manta_Character_BP.Manta_Character_BP'
       fullStatsRaw = [[320, 0.05, 0.0675, 0.5, 0], [270, 0.2, 0.2, 0, 0], [700, 0.06, 0, 0.5, 0], [150, 0.1, 0.1, 0, 0], [1000, 0.1, 0.1, 0, 0.15], None, None, [200, 0.02, 0.04, 0, 0], [1, 0.05, 0.05, 1, 0.4], [1, 0, 0.0125, 0, 0], None, None]
       immobilizedBy = []
       breeding = {'gestationTime': 28571.4286, 'incubationTime': 0, 'maturationTime': 133333.333, 'matingCooldownMin': 64800, 'matingCooldownMax': 172800}
       colors = [{'name': 'Body', 'colors': ['Black', 'Dino Dark Blue', 'Dino Dark Orange', 'Dino Dark Red', 'Dino Dark Yellow', 'Dino Light Blue', 'Dino Light Orange', 'Dino Light Red', 'Dino Light Yellow']}, {'name': 'Spots', 'colors': ['Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Dark Green', 'Dino Dark Orange', 'Dino Dark Red', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Medium Brown', 'Dino Medium Green']}, None, None, {'name': 'Patterning', 'colors': ['Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Dark Green', 'Dino Dark Orange', 'Dino Dark Red', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Medium Brown', 'Dino Medium Green']}, None]
       taming = {'nonViolent': True, 'violent': False, 'tamingIneffectiveness': 2.5, 'affinityNeeded0': 1500, 'affinityIncreasePL': 75, 'wakeAffinityMult': 1.6, 'wakeFoodDeplMult': 1, 'foodConsumptionBase': 0.001929, 'foodConsumptionMult': 420}
       TamedBaseHealthMultiplier = 1
       displayedStats = 919
