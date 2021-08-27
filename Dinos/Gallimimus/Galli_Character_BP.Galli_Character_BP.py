import sys,sce
class Galli_Character_BP(sce.Dinos):
   def __init__(self):
       super().__init__(self)
       name = 'Gallimimus'
       blueprintPath = '/Game/PrimalEarth/Dinos/Gallimimus/Galli_Character_BP.Galli_Character_BP'
       fullStatsRaw = [[150, 0.2, 0.27, 0.5, 0], [300, 0.1, 0.1, 0, 0], [420, 0.06, 0, 0.5, 0], [150, 0.1, 0.1, 0, 0], [1000, 0.1, 0.1, 0, 0], None, None, [270, 0.02, 0.04, 0, 0], [1, 0.05, 0.2, 0.5, 0.4], [1, 0, 0.01, 0, 0], None, None]
       immobilizedBy = ['Chain Bola', 'Bear Trap', 'Large Bear Trap', 'Plant Species Y']
       breeding = {'gestationTime': 0, 'incubationTime': 5142.44575, 'eggTempMin': 24, 'eggTempMax': 28, 'maturationTime': 95238.0952, 'matingCooldownMin': 64800, 'matingCooldownMax': 172800}
       colors = [{'name': 'Body', 'colors': ['Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Dark Green', 'Dino Dark Orange', 'Dino Dark Red', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Light Brown', 'Dino Light Green', 'Dino Light Orange', 'Dino Light Red', 'Dino Light Yellow', 'Dino Medium Brown', 'Dino Medium Green', 'Light Grey']}, {'name': 'Feathers', 'colors': ['Black', 'Dark Grey', 'Dino Albino', 'Dino Dark Brown', 'Dino Dark Green', 'Dino Dark Orange', 'Dino Dark Red', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Medium Brown', 'Dino Medium Green']}, None, {'name': 'Back Accents', 'colors': ['Black', 'Dark Grey', 'Dino Albino', 'Dino Dark Brown', 'Dino Dark Green', 'Dino Dark Orange', 'Dino Dark Red', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Light Brown', 'Dino Light Green', 'Dino Light Orange', 'Dino Light Yellow', 'Dino Medium Brown', 'Dino Medium Green', 'Light Grey']}, {'name': 'Spine and Feather Tips', 'colors': ['Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Dark Green', 'Dino Dark Orange', 'Dino Dark Red', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Medium Brown', 'Dino Medium Green']}, {'name': 'Lower Body', 'colors': ['Black', 'Dino Light Brown', 'Dino Light Green', 'Dino Light Orange', 'Dino Light Red', 'Dino Light Yellow', 'Dino Medium Brown', 'Dino Medium Green', 'Light Grey']}]
       taming = {'nonViolent': False, 'violent': True, 'tamingIneffectiveness': 0.4, 'affinityNeeded0': 2200, 'affinityIncreasePL': 95, 'torporDepletionPS0': 4.175, 'foodConsumptionBase': 0.001929, 'foodConsumptionMult': 432.0028}
       boneDamageAdjusters = {'c_jaw': 2, 'c_head': 2}
       TamedBaseHealthMultiplier = 1
       displayedStats = 927
