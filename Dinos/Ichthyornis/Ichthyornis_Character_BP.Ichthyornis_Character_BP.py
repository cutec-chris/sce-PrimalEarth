import sys,sce
class Ichthyornis_Character_BP(sce.Dinos):
   def __init__(self):
       super().__init__(self)
       name = 'Ichthyornis'
       blueprintPath = '/Game/PrimalEarth/Dinos/Ichthyornis/Ichthyornis_Character_BP.Ichthyornis_Character_BP'
       isFlyer = True
       fullStatsRaw = [[50, 0.2, 0.27, 0.5, 0], [150, 0.1, 0.1, 0, 0], [120, 0.06, 0, 0.5, 0], [150, 0.1, 0.1, 0, 0], [1000, 0.1, 0.1, 0, 0.15], None, None, [55, 0.02, 0.04, 0, 0], [1, 0.05, 0.1, 0.65, 0.4], [1, 0, 0.01, 0.365, 0], None, None]
       immobilizedBy = ['Bola', 'Bear Trap', 'Plant Species Y']
       breeding = {'gestationTime': 0, 'incubationTime': 5999.52004, 'eggTempMin': 29, 'eggTempMax': 32, 'maturationTime': 133333.333, 'matingCooldownMin': 64800, 'matingCooldownMax': 172800}
       colors = [{'name': 'Main Body', 'colors': ['Black', 'Dark Grey', 'Dino Albino', 'Dino Dark Brown', 'Dino Dark Orange', 'Dino Darker Grey', 'Dino Light Blue', 'Dino Light Brown', 'Dino Light Orange', 'Dino Medium Brown', 'Light Grey']}, {'name': 'Feet', 'colors': ['Black', 'Dino Light Blue', 'Dino Light Brown', 'Dino Light Orange', 'Dino Light Purple', 'Dino Light Red', 'Dino Light Yellow', 'Dino Medium Brown', 'DragonGreen1', 'Light Grey']}, None, None, None, {'name': 'Facial Highlights', 'colors': ['Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Dark Orange', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Medium Brown']}]
       taming = {'nonViolent': False, 'violent': True, 'tamingIneffectiveness': 3.125, 'affinityNeeded0': 1750, 'affinityIncreasePL': 85, 'torporDepletionPS0': 0.3, 'foodConsumptionBase': 0.001543, 'foodConsumptionMult': 216.0294}
       boneDamageAdjusters = {'c_neck4': 3, 'c_jaw': 3}
       TamedBaseHealthMultiplier = 2
       displayedStats = 927
