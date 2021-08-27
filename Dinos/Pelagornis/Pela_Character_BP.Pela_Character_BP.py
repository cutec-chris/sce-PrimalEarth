import sys,sce
class Pela_Character_BP(sce.Dinos):
   def __init__(self):
       super().__init__(self)
       name = 'Pelagornis'
       blueprintPath = '/Game/PrimalEarth/Dinos/Pelagornis/Pela_Character_BP.Pela_Character_BP'
       isFlyer = True
       fullStatsRaw = [[240, 0.2, 0.27, 0.5, 0], [180, 0.05, 0.04, 0, 0], [120, 0.06, 0, 0.5, 0], [150, 0.1, 0.1, 0, 0], [1200, 0.1, 0.1, 0, 0.15], None, None, [150, 0.02, 0.03, 0, 0], [1, 0.05, 0.075, 0.65, 0.4], [1, 0, 0.01, 0.365, 0], None, None]
       statImprintMult = [0.2, 0, 0.2, 0, 0.2, 0.2, 0, 0.2, 0.2, 0, 0, 0]
       immobilizedBy = ['Bola', 'Bear Trap', 'Large Bear Trap', 'Plant Species Y']
       breeding = {'gestationTime': 0, 'incubationTime': 5999.52004, 'eggTempMin': 29, 'eggTempMax': 32, 'maturationTime': 133333.333, 'matingCooldownMin': 64800, 'matingCooldownMax': 172800}
       colors = [{'name': 'Feathers', 'colors': ['Black', 'Dark Grey', 'Dino Albino', 'Dino Dark Brown', 'Dino Dark Green', 'Dino Dark Orange', 'Dino Dark Red', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Light Brown', 'Dino Light Green', 'Dino Light Orange', 'Dino Light Red', 'Dino Light Yellow', 'Dino Medium Brown', 'Dino Medium Green', 'Light Grey']}, None, None, None, None, {'name': 'Skin and Wind/Tail Tips', 'colors': ['Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Dark Green', 'Dino Dark Orange', 'Dino Dark Red', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Medium Brown', 'Dino Medium Green']}]
       taming = {'nonViolent': False, 'violent': True, 'tamingIneffectiveness': 3.125, 'affinityNeeded0': 1200, 'affinityIncreasePL': 60, 'torporDepletionPS0': 0.3, 'foodConsumptionBase': 0.001543, 'foodConsumptionMult': 216.0294}
       boneDamageAdjusters = {'c_neck4': 3, 'c_jaw': 3}
       TamedBaseHealthMultiplier = 1
       displayedStats = 927
