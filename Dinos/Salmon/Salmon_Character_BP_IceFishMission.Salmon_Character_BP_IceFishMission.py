import sys,sce
class Salmon_Character_BP_IceFishMission(sce.BaseCreature):
   def __init__(self):
       super().__init__(self)
       name = 'Sabertooth Salmon'
       blueprintPath = '/Game/PrimalEarth/Dinos/Salmon/Salmon_Character_BP_IceFishMission.Salmon_Character_BP_IceFishMission'
       variants = ['IceFishing']
       fullStatsRaw = [[65, 0.2, 0.27, 0.5, 0], [100, 0.1, 0.1, 0, 0], [15, 0.06, 0, 0.5, 0], [150, 0.1, 0.1, 0, 0], [100, 0.1, 0.1, 0, 0], None, None, [18, 0.02, 0.04, 0, 0], [1, 0.05, 0.1, 0.5, 0.4], [1, 0, 0.01, 0, 0], None, None]
       immobilizedBy = []
       noGender = True
       colors = [{'name': 'Unknown', 'colors': ['BigFoot0', 'BigFoot4', 'BigFoot5', 'Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Dark Orange', 'Dino Darker Grey', 'Dino Light Brown', 'Dino Light Orange', 'Dino Medium Brown', 'Light Grey']}, None, None, None, {'name': 'Unknown', 'colors': ['BigFoot0', 'BigFoot4', 'BigFoot5', 'Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Dark Orange', 'Dino Darker Grey', 'Dino Light Brown', 'Dino Light Orange', 'Dino Medium Brown', 'Light Grey']}, {'name': 'Unknown', 'colors': ['BigFoot0', 'BigFoot4', 'BigFoot5', 'Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Dark Orange', 'Dino Darker Grey', 'Dino Light Brown', 'Dino Light Orange', 'Dino Medium Brown', 'Light Grey']}]
       taming = {'nonViolent': False, 'violent': False, 'tamingIneffectiveness': 2000, 'affinityNeeded0': 10000, 'affinityIncreasePL': 5, 'foodConsumptionBase': 0.01, 'foodConsumptionMult': 0.05}
       TamedBaseHealthMultiplier = 1
       displayedStats = 919
