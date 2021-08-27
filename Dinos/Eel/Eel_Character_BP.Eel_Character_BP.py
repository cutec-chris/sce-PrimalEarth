import sys,sce
class Eel_Character_BP(sce.Dinos):
   def __init__(self):
       super().__init__(self)
       name = 'Electrophorus'
       blueprintPath = '/Game/PrimalEarth/Dinos/Eel/Eel_Character_BP.Eel_Character_BP'
       fullStatsRaw = [[180, 0.2, 0.27, -0.2, 0], [165, 0.1, 0.1, 0, 0], [175, 0.06, 0, 0.5, 0], [1050, 0.1, 0.1, 0, 0], [1500, 0.1, 0.1, 0, 0], None, None, [150, 0.02, 0.04, 0, 0], [1, 0.05, 0.1, -0.25, 0.25], [1, 0, 0.01, 0, 0], None, None]
       altBaseStats = {'0': 260}
       immobilizedBy = []
       breeding = {'gestationTime': 0, 'incubationTime': 17998.5601, 'eggTempMin': -75, 'eggTempMax': 75, 'maturationTime': 166666.667, 'matingCooldownMin': 64800, 'matingCooldownMax': 172800}
       colors = [{'name': 'Body Main', 'colors': ['Black', 'Dino Albino', 'Dino Dark Blue', 'Dino Dark Orange', 'Dino Dark Purple', 'Dino Dark Red', 'Dino Dark Yellow', 'Dino Light Blue', 'Dino Light Green', 'Dino Light Orange', 'Dino Light Purple', 'Dino Light Red', 'Dino Light Yellow']}, {'name': 'Fins', 'colors': ['Dino Dark Orange', 'Dino Dark Red', 'Dino Light Blue', 'Dino Light Orange', 'Dino Light Purple', 'Dino Light Red', 'DragonBase1', 'DragonGreen3', 'None']}, {'name': 'Eel Highlight'}, {'name': 'Fin Highlight'}, {'name': 'Unknown', 'colors': ['Black', 'Dino Albino', 'Dino Dark Blue', 'Dino Dark Green', 'Dino Dark Orange', 'Dino Dark Purple', 'Dino Dark Red', 'Dino Dark Yellow', 'Dino Light Blue', 'Dino Light Green', 'Dino Light Orange', 'Dino Light Purple', 'Dino Light Red', 'Dino Light Yellow', 'Dino Medium Green']}, {'name': 'Belly', 'colors': ['Black', 'Dino Albino', 'Dino Dark Yellow', 'Dino Light Blue', 'Dino Light Green', 'Dino Light Orange', 'Dino Light Purple', 'Dino Light Red', 'Dino Light Yellow', 'DragonBase0', 'DragonBase1', 'DragonGreen3', 'WyvernPurple0']}]
       taming = {'nonViolent': True, 'violent': False, 'tamingIneffectiveness': 2.5, 'affinityNeeded0': 2250, 'affinityIncreasePL': 90, 'wakeAffinityMult': 1.6, 'wakeFoodDeplMult': 4, 'foodConsumptionBase': 0.002929, 'foodConsumptionMult': 420}
       TamedBaseHealthMultiplier = 1
       displayedStats = 927
