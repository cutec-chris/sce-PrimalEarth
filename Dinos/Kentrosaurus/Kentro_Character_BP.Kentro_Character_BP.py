import sys,sce
class Kentro_Character_BP(sce.Dinos):
   def __init__(self):
       super().__init__(self)
       name = 'Kentrosaurus'
       blueprintPath = '/Game/PrimalEarth/Dinos/Kentrosaurus/Kentro_Character_BP.Kentro_Character_BP'
       fullStatsRaw = [[650, 0.2, 0.27, 0.5, 0], [300, 0.1, 0.1, 0, 0], [500, 0.06, 0, 0.5, 0], [150, 0.1, 0.1, 0, 0], [6000, 0.1, 0.1, 0, 0], None, None, [500, 0.02, 0.04, 0, 0], [1, 0.05, 0.1, 0.5, 0.4], [1, 0, 0.01, 0, 0], None, None]
       immobilizedBy = ['Chain Bola', 'Bear Trap', 'Large Bear Trap', 'Plant Species Y']
       breeding = {'gestationTime': 0, 'incubationTime': 9999.20006, 'eggTempMin': 24, 'eggTempMax': 30, 'maturationTime': 185185.185, 'matingCooldownMin': 64800, 'matingCooldownMax': 172800}
       colors = [{'name': 'Body Main', 'colors': ['Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Dark Orange', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Medium Brown', 'Dino Medium Green', 'DragonBase0', 'DragonGreen0']}, {'name': 'Plates Main', 'colors': ['Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Dark Orange', 'Dino Darker Grey', 'Dino Medium Brown', 'DragonBase0', 'DragonBase1', 'DragonFire', 'DragonGreen0', 'DragonGreen1', 'DragonGreen3']}, {'name': 'Spikes', 'colors': ['BigFoot4', 'Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Darker Grey', 'Dino Medium Brown', 'DragonGreen2', 'NearBlack', 'WolfFur']}, {'name': 'Plates Highlights', 'colors': ['BigFoot5', 'Black', 'Dark Grey', 'Dino Dark Orange', 'Dino Light Blue', 'Dino Light Brown', 'Dino Light Green', 'Dino Medium Brown', 'DragonBase1', 'DragonFire']}, {'name': 'Body Highlights', 'colors': ['Black', 'Dino Dark Brown', 'Dino Dark Orange', 'Dino Darker Grey', 'Dino Medium Brown', 'DragonBase0', 'DragonGreen0', 'DragonGreen3', 'NearBlack', 'WyvernBlue1', 'WyvernPurple0']}, {'name': 'Underbelly', 'colors': ['BigFoot0', 'BigFoot4', 'BigFoot5', 'Black', 'Dino Light Brown', 'Dino Light Orange', 'Dino Medium Brown', 'Light Grey']}]
       taming = {'nonViolent': False, 'violent': True, 'tamingIneffectiveness': 0.1, 'affinityNeeded0': 5500, 'affinityIncreasePL': 285, 'torporDepletionPS0': 0.3, 'foodConsumptionBase': 0.005341, 'foodConsumptionMult': 208.0343}
       TamedBaseHealthMultiplier = 1
       displayedStats = 927
