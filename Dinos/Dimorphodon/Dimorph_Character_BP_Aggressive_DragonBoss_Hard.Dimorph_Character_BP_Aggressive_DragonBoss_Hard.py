import sys,sce
class Dimorph_Character_BP_Aggressive_DragonBoss_Hard(sce.BaseCreature):
   def __init__(self):
       super().__init__(self)
       name = 'Dimorphodon'
       blueprintPath = '/Game/PrimalEarth/Dinos/Dimorphodon/Dimorph_Character_BP_Aggressive_DragonBoss_Hard.Dimorph_Character_BP_Aggressive_DragonBoss_Hard'
       variants = ['Alpha', 'Boss', 'Minion']
       isFlyer = True
       fullStatsRaw = [[792, 0.2, 0.27, 0.5, 0], [150, 0.1, 0.1, 0, 0], [100, 0.06, 0, 0.5, 0], [150, 0.1, 0.1, 0, 0], [900, 0.1, 0.1, 0, 0], None, None, [50, 0.02, 0.04, 0, 0], [1, 0.05, 0.1, 0.5, 0.4], [1, 0, 0.01, 0, 0], None, None]
       altBaseStats = {'0': 264}
       immobilizedBy = []
       breeding = {'gestationTime': 0, 'incubationTime': 4864.47571, 'eggTempMin': 35, 'eggTempMax': 38, 'maturationTime': 90090.0901, 'matingCooldownMin': 64800, 'matingCooldownMax': 172800}
       colors = [{'name': 'Unknown', 'colors': ['Black', 'Dark Grey', 'Dino Albino', 'Dino Dark Brown', 'Dino Dark Orange', 'Dino Dark Red', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Light Brown', 'Dino Light Orange', 'Dino Light Yellow', 'Dino Medium Brown', 'Light Grey']}, None, None, None, {'name': 'Unknown', 'colors': ['Black', 'Dark Grey', 'Dino Albino', 'Dino Dark Blue', 'Dino Dark Brown', 'Dino Dark Green', 'Dino Dark Orange', 'Dino Dark Purple', 'Dino Dark Red', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Light Blue', 'Dino Light Brown', 'Dino Light Green', 'Dino Light Orange', 'Dino Light Purple', 'Dino Light Red', 'Dino Light Yellow', 'Dino Medium Brown', 'Dino Medium Green', 'Light Grey']}, {'name': 'Unknown', 'colors': ['Black', 'Dark Grey', 'Dino Albino', 'Dino Dark Blue', 'Dino Dark Brown', 'Dino Dark Green', 'Dino Dark Orange', 'Dino Dark Purple', 'Dino Dark Red', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Light Blue', 'Dino Light Brown', 'Dino Light Green', 'Dino Light Orange', 'Dino Light Purple', 'Dino Light Red', 'Dino Light Yellow', 'Dino Medium Brown', 'Dino Medium Green', 'Light Grey']}]
       taming = {'nonViolent': False, 'violent': True, 'tamingIneffectiveness': 4.166666, 'affinityNeeded0': 900, 'affinityIncreasePL': 45, 'torporDepletionPS0': 0.8333, 'foodConsumptionBase': 0.001302, 'foodConsumptionMult': 1152.074}
       boneDamageAdjusters = {'c_head': 3}
       TamedBaseHealthMultiplier = 1
       displayedStats = 927
