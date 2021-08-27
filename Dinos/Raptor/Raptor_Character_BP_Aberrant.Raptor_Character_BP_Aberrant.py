import sys,sce
class Raptor_Character_BP_Aberrant(sce.Aberration):
   def __init__(self):
       super().__init__(self)
       name = 'Aberrant Raptor'
       blueprintPath = '/Game/PrimalEarth/Dinos/Raptor/Raptor_Character_BP_Aberrant.Raptor_Character_BP_Aberrant'
       variants = ['Aberrant']
       fullStatsRaw = [[200, 0.2, 0.27, 0.5, 0], [150, 0.1, 0.1, 0, 0], [180, 0.06, 0, 0.5, 0], [150, 0.1, 0.1, 0, 0], [1200, 0.1, 0.1, 0, 0], None, None, [140, 0.02, 0.04, 0, 0], [1, 0.05, 0.1, 0.5, 0.4], [1, 0, 0.015, 0.2, 0], None, None]
       immobilizedBy = ['Bola', 'Bear Trap', 'Large Bear Trap', 'Plant Species Y']
       breeding = {'gestationTime': 0, 'incubationTime': 7199.42405, 'eggTempMin': 20, 'eggTempMax': 28, 'maturationTime': 133333.333, 'matingCooldownMin': 64800, 'matingCooldownMax': 172800}
       colors = [{'name': 'Unknown', 'colors': ['Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Dark Green', 'Dino Dark Orange', 'Dino Dark Red', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Medium Brown', 'Dino Medium Green']}, {'name': 'Unknown', 'colors': ['Dino Light Blue', 'Dino Light Green', 'Dino Light Orange', 'Dino Light Purple', 'Dino Light Red', 'Dino Light Yellow', 'Dino Medium Green']}, None, {'name': 'Unknown', 'colors': ['Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Dark Green', 'Dino Dark Orange', 'Dino Dark Red', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Light Brown', 'Dino Light Green', 'Dino Light Orange', 'Dino Light Yellow', 'Dino Medium Brown', 'Dino Medium Green', 'Light Grey']}, {'name': 'Unknown', 'colors': ['Dino Light Blue', 'Dino Light Green', 'Dino Light Orange', 'Dino Light Purple', 'Dino Light Red', 'Dino Light Yellow', 'Dino Medium Green']}, {'name': 'Unknown', 'colors': ['Black', 'Dino Light Blue', 'Dino Light Brown', 'Dino Light Green', 'Dino Light Orange', 'Dino Light Yellow', 'Dino Medium Brown', 'Dino Medium Green', 'Light Grey']}]
       taming = {'nonViolent': False, 'violent': True, 'tamingIneffectiveness': 3.125, 'affinityNeeded0': 1200, 'affinityIncreasePL': 60, 'torporDepletionPS0': 0.3, 'foodConsumptionBase': 0.001543, 'foodConsumptionMult': 648.0881}
       boneDamageAdjusters = {'Cnt_Head_JNT_SKL': 3, 'Cnt_Neck_002_JNT_SKL': 3, 'Cnt_Neck_000_JNT_SKL': 3}
       TamedBaseHealthMultiplier = 0.96
       displayedStats = 927
