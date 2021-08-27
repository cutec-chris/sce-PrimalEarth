import sys,sce
class MegaRaptor_Character_BP(sce.Alphas):
   def __init__(self):
       super().__init__(self)
       name = 'Alpha Raptor'
       blueprintPath = '/Game/PrimalEarth/Dinos/Raptor/MegaRaptor_Character_BP.MegaRaptor_Character_BP'
       variants = ['Mega']
       fullStatsRaw = [[3600, 0.2, 0.27, 0.5, 0], [150, 0.1, 0.1, 0, 0], [180, 0.06, 0, 0.5, 0], [150, 0.1, 0.1, 0, 0], [1200, 0.1, 0.1, 0, 0], None, None, [140, 0.02, 0.04, 0, 0], [1, 0.05, 0.1, 0.5, 0.4], [1, 0, 0.015, 0.2, 0], None, None]
       immobilizedBy = ['Chain Bola']
       breeding = {'gestationTime': 0, 'incubationTime': 0, 'maturationTime': 133333.333, 'matingCooldownMin': 64800, 'matingCooldownMax': 172800}
       colors = [{'name': 'Unknown', 'colors': ['Black', 'Dark Red', 'Dino Albino', 'Dino Dark Orange']}, {'name': 'Unknown', 'colors': ['Black', 'Dark Red', 'Dino Albino', 'Dino Dark Orange']}, None, {'name': 'Unknown', 'colors': ['Black', 'Dark Red', 'Dino Albino', 'Dino Dark Orange']}, None, {'name': 'Unknown', 'colors': ['Black', 'Dark Red', 'Dino Albino', 'Dino Dark Orange']}]
       taming = {'nonViolent': False, 'violent': False, 'tamingIneffectiveness': 3.125, 'affinityNeeded0': 1200, 'affinityIncreasePL': 60, 'foodConsumptionBase': 0.001543, 'foodConsumptionMult': 648.0881}
       boneDamageAdjusters = {'Cnt_Head_JNT_SKL': 3, 'Cnt_Neck_002_JNT_SKL': 3, 'Cnt_Neck_000_JNT_SKL': 3}
       TamedBaseHealthMultiplier = 1
       displayedStats = 919
