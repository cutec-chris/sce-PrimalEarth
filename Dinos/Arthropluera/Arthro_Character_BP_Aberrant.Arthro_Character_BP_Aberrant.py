import sys,sce
class Arthro_Character_BP_Aberrant(sce.Aberration):
   def __init__(self):
       super().__init__(self)
       name = 'Aberrant Arthropluera'
       blueprintPath = '/Game/PrimalEarth/Dinos/Arthropluera/Arthro_Character_BP_Aberrant.Arthro_Character_BP_Aberrant'
       variants = ['Aberrant']
       fullStatsRaw = [[500, 0.2, 0.27, 0.5, 0], [200, 0.1, 0.1, 0, 0], [175, 0.06, 0, 0.5, 0], [150, 0.1, 0.1, 0, 0], [1200, 0.1, 0.1, 0, 0], None, None, [100, 0.02, 0.04, 0, 0], [1, 0.05, 0.1, 0.5, 0.4], [1, 0, 0.01, 0.2, 0], None, None]
       immobilizedBy = []
       breeding = {'gestationTime': 0, 'incubationTime': 8999.28006, 'eggTempMin': 18, 'eggTempMax': 22, 'maturationTime': 185185.185, 'matingCooldownMin': 64800, 'matingCooldownMax': 172800}
       colors = [{'name': 'Unknown', 'colors': ['Black', 'Dark Grey', 'Dino Dark Blue', 'Dino Dark Brown', 'Dino Dark Green', 'Dino Dark Orange', 'Dino Dark Purple', 'Dino Dark Red', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Medium Brown', 'Dino Medium Green']}, {'name': 'Unknown', 'colors': ['Black', 'Dino Light Blue', 'Dino Light Brown', 'Dino Light Green', 'Dino Light Orange', 'Dino Light Purple', 'Dino Light Red', 'Dino Light Yellow', 'Dino Medium Brown', 'Dino Medium Green', 'Light Grey']}, {'name': 'Unknown', 'colors': ['Black', 'Dino Light Blue', 'Dino Light Brown', 'Dino Light Green', 'Dino Light Orange', 'Dino Light Purple', 'Dino Light Red', 'Dino Light Yellow', 'Dino Medium Brown', 'Dino Medium Green', 'Light Grey']}, {'name': 'Unknown', 'colors': ['Black', 'Dino Light Blue', 'Dino Light Brown', 'Dino Light Green', 'Dino Light Orange', 'Dino Light Purple', 'Dino Light Red', 'Dino Light Yellow', 'Dino Medium Brown', 'Dino Medium Green', 'Light Grey']}, {'name': 'Unknown', 'colors': ['Black', 'Dino Light Blue', 'Dino Light Brown', 'Dino Light Green', 'Dino Light Orange', 'Dino Light Purple', 'Dino Light Red', 'Dino Light Yellow', 'Dino Medium Brown', 'Dino Medium Green', 'Light Grey']}, {'name': 'Unknown', 'colors': ['Black', 'Dino Light Blue', 'Dino Light Brown', 'Dino Light Green', 'Dino Light Orange', 'Dino Light Purple', 'Dino Light Red', 'Dino Light Yellow', 'Dino Medium Brown', 'Dino Medium Green', 'Light Grey']}]
       taming = {'nonViolent': True, 'violent': False, 'tamingIneffectiveness': 2.5, 'affinityNeeded0': 3000, 'affinityIncreasePL': 75, 'wakeAffinityMult': 1.6, 'wakeFoodDeplMult': 2, 'foodConsumptionBase': 0.001543, 'foodConsumptionMult': 648.0881}
       boneDamageAdjusters = {'c_head': 2.5, 'c_jaw': 2.5, 'l_jaw': 2.5, 'r_jaw': 2.5}
       TamedBaseHealthMultiplier = 0.96
       displayedStats = 919
