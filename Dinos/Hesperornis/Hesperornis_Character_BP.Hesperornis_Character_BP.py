import sys,sce
class Hesperornis_Character_BP(sce.Dinos):
   def __init__(self):
       super().__init__(self)
       name = 'Hesperornis'
       blueprintPath = '/Game/PrimalEarth/Dinos/Hesperornis/Hesperornis_Character_BP.Hesperornis_Character_BP'
       fullStatsRaw = [[95, 0.2, 0.27, 0.5, 0], [200, 0.1, 0.1, 0, 0], [300, 0.06, 0, 0.5, 0], [150, 0.1, 0.1, 0, 0], [900, 0.1, 0.1, 0, 0.15], None, None, [70, 0.02, 0.04, 0, 0], [1, 0.05, 0.1, 1, 0.4], [1, 0, 0.01, 0, 0], None, None]
       immobilizedBy = []
       breeding = {'gestationTime': 0, 'incubationTime': 5454.10913, 'eggTempMin': 22, 'eggTempMax': 30, 'maturationTime': 101010.101, 'matingCooldownMin': 64800, 'matingCooldownMax': 172800}
       colors = [{'name': 'Body Main', 'colors': ['BigFoot0', 'Black', 'Dark Grey', 'Dino Albino', 'Dino Dark Brown', 'Dino Dark Orange', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Medium Brown', 'DragonGreen3', 'WyvernBlue1']}, None, {'name': 'Feet', 'colors': ['Black', 'Dark Grey', 'Dino Albino', 'Dino Dark Brown', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Medium Brown', 'DragonBase0', 'DragonBase1', 'DragonGreen1', 'DragonGreen2', 'DragonGreen3', 'WyvernPurple1']}, None, {'name': 'Back Highlights', 'colors': ['Black', 'Dino Albino', 'Dino Dark Brown', 'Dino Dark Orange', 'Dino Dark Purple', 'Dino Dark Yellow', 'Dino Darker Grey', 'NearBlack', 'WyvernBlue1']}, {'name': 'Underbelly', 'colors': ['BigFoot0', 'BigFoot4', 'Dino Albino', 'Dino Light Blue', 'Dino Light Brown', 'Dino Light Orange', 'Dino Light Purple', 'Dino Light Yellow']}]
       taming = {'nonViolent': True, 'violent': False, 'tamingIneffectiveness': 4.166667, 'affinityNeeded0': 1200, 'affinityIncreasePL': 45, 'wakeAffinityMult': 1.6, 'wakeFoodDeplMult': 1.2, 'foodConsumptionBase': 0.001389, 'foodConsumptionMult': 1079.914}
       boneDamageAdjusters = {'c_neck4': 3, 'c_head': 3}
       TamedBaseHealthMultiplier = 1
       displayedStats = 919
