import sys,sce
class Therizino_Character_BP(sce.Dinos):
   def __init__(self):
       super().__init__(self)
       name = 'Therizinosaur'
       blueprintPath = '/Game/PrimalEarth/Dinos/Therizinosaurus/Therizino_Character_BP.Therizino_Character_BP'
       fullStatsRaw = [[870, 0.2, 0.27, 0.5, 0], [300, 0.1, 0.1, 0, 0], [925, 0.06, 0, 0.5, 0], [150, 0.1, 0.1, 0, 0], [3000, 0.1, 0.1, 0, 0], None, None, [365, 0.02, 0.04, 0, 0], [1, 0.05, 0.1, 0.5, 0.4], [1, 0, 0.01, 0, 0], None, None]
       immobilizedBy = ['Chain Bola', 'Large Bear Trap', 'Plant Species Y']
       breeding = {'gestationTime': 0, 'incubationTime': 5999.52004, 'eggTempMin': 26, 'eggTempMax': 32, 'maturationTime': 416666.667, 'matingCooldownMin': 64800, 'matingCooldownMax': 172800}
       colors = [{'name': 'Feathers Main', 'colors': ['Black', 'Dark Grey', 'Dino Albino', 'Dino Dark Brown', 'Dino Dark Orange', 'Dino Dark Red', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Medium Brown', 'NearBlack', 'WyvernBlue1']}, None, {'name': 'Body Highlights', 'colors': ['Dino Albino', 'Dino Dark Yellow', 'Dino Light Brown', 'Dino Light Green', 'Dino Light Yellow', 'DragonGreen3', 'Light Grey', 'WyvernPurple1']}, None, {'name': 'Feather Highlights', 'colors': ['Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Dark Green', 'Dino Dark Orange', 'Dino Dark Red', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Medium Brown', 'Dino Medium Green']}, {'name': 'Body Main', 'colors': ['Black', 'Dino Darker Grey', 'Dino Light Brown', 'Dino Light Orange', 'Dino Light Yellow', 'Dino Medium Brown', 'DragonGreen2', 'Light Grey', 'WyvernBlue1']}]
       taming = {'nonViolent': False, 'violent': True, 'tamingIneffectiveness': 0.06, 'affinityNeeded0': 6800, 'affinityIncreasePL': 160, 'torporDepletionPS0': 2.8333332, 'foodConsumptionBase': 0.002314, 'foodConsumptionMult': 180.0634}
       boneDamageAdjusters = {'Cnt_Head_JNT_SKL': 3, 'Cnt_Neck_002_JNT_SKL': 3, 'Cnt_Neck_000_JNT_SKL': 3}
       TamedBaseHealthMultiplier = 1
       displayedStats = 927
