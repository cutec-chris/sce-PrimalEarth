import sys,sce
class Dunkle_Character_BP(sce.Dinos):
   def __init__(self):
       super().__init__(self)
       name = 'Dunkleosteus'
       blueprintPath = '/Game/PrimalEarth/Dinos/Dunkleosteus/Dunkle_Character_BP.Dunkle_Character_BP'
       fullStatsRaw = [[710, 0.2, 0.27, 0.3, 0], [200, 0.1, 0.1, 0, 0], [1150, 0.06, 0, 0.5, 0], [150, 0.1, 0.1, 0, 0], [2000, 0.1, 0.1, 0, 0.15], None, None, [910, 0.02, 0.04, 0, 0], [1, 0.05, 0.1, 1, 0.4], [1, 0, 0.01, 0, 0], None, None]
       immobilizedBy = []
       breeding = {'gestationTime': 28571.4286, 'incubationTime': 0, 'maturationTime': 296296.296, 'matingCooldownMin': 64800, 'matingCooldownMax': 172800}
       colors = [{'name': 'Body', 'colors': ['Black', 'Dino Dark Blue', 'Dino Dark Orange', 'Dino Dark Red', 'Dino Dark Yellow', 'Dino Light Blue', 'Dino Light Orange', 'Dino Light Red', 'Dino Light Yellow']}, None, None, None, {'name': 'Spots', 'colors': ['Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Dark Green', 'Dino Dark Orange', 'Dino Dark Red', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Medium Brown', 'Dino Medium Green']}, {'name': 'Head', 'colors': ['Black', 'Dino Albino', 'Dino Light Blue', 'Dino Light Brown', 'Dino Light Orange', 'Dino Light Yellow', 'Dino Medium Brown', 'Light Grey']}]
       taming = {'nonViolent': False, 'violent': True, 'tamingIneffectiveness': 3.275, 'affinityNeeded0': 1300, 'affinityIncreasePL': 60, 'torporDepletionPS0': 1, 'foodConsumptionBase': 0.001852, 'foodConsumptionMult': 199.984}
       TamedBaseHealthMultiplier = 1
       displayedStats = 919
