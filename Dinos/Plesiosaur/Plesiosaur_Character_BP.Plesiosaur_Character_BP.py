import sys,sce
class Plesiosaur_Character_BP(sce.Dinos):
   def __init__(self):
       super().__init__(self)
       name = 'Plesiosaur'
       blueprintPath = '/Game/PrimalEarth/Dinos/Plesiosaur/Plesiosaur_Character_BP.Plesiosaur_Character_BP'
       fullStatsRaw = [[2400, 0.12, 0.162, 0.16, 0], [800, 0.1, 0.1, 0, 0], [1600, 0.06, 0, 0.5, 0], [150, 0.1, 0.1, 0, 0], [5000, 0.1, 0.1, 0, 0.15], None, None, [800, 0.02, 0.04, 0, 0], [1, 0.05, 0.1, 1, 0.4], [1, 0, 0.005, 0, 0], None, None]
       immobilizedBy = []
       breeding = {'gestationTime': 28571.4286, 'incubationTime': 0, 'maturationTime': 416666.667, 'matingCooldownMin': 64800, 'matingCooldownMax': 172800}
       colors = [{'name': 'Body', 'colors': ['Black', 'Dino Dark Blue', 'Dino Dark Orange', 'Dino Dark Red', 'Dino Dark Yellow', 'Dino Light Blue', 'Dino Light Orange', 'Dino Light Red', 'Dino Light Yellow']}, {'name': 'Facial Fins', 'colors': ['Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Dark Green', 'Dino Dark Orange', 'Dino Dark Red', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Medium Brown', 'Dino Medium Green']}, {'name': 'Unknown', 'colors': ['Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Dark Green', 'Dino Dark Orange', 'Dino Dark Red', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Medium Brown', 'Dino Medium Green']}, None, {'name': 'Back', 'colors': ['Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Dark Green', 'Dino Dark Orange', 'Dino Dark Red', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Medium Brown', 'Dino Medium Green']}, {'name': 'Belly', 'colors': ['Black', 'Dino Albino', 'Dino Light Blue', 'Dino Light Brown', 'Dino Light Orange', 'Dino Light Yellow', 'Dino Medium Brown', 'Light Grey']}]
       taming = {'nonViolent': False, 'violent': True, 'tamingIneffectiveness': 0.75, 'affinityNeeded0': 5000, 'affinityIncreasePL': 250, 'torporDepletionPS0': 2.1333332, 'foodConsumptionBase': 0.003858, 'foodConsumptionMult': 180.0011}
       TamedBaseHealthMultiplier = 1
       displayedStats = 919
