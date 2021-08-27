import sys,sce
class MegaCarno_Character_BP(sce.Alphas):
   def __init__(self):
       super().__init__(self)
       name = 'Alpha Carnotaurus'
       blueprintPath = '/Game/PrimalEarth/Dinos/Carno/MegaCarno_Character_BP.MegaCarno_Character_BP'
       variants = ['Mega']
       fullStatsRaw = [[6400, 0.2, 0.27, 0.5, 0], [300, 0.1, 0.1, 0, 0], [350, 0.06, 0, 0.5, 0], [150, 0.1, 0.1, 0, 0], [2000, 0.1, 0.1, 0, 0.15], None, None, [300, 0.02, 0.04, 0, 0], [1, 0.05, 0.1, 0.5, 0.4], [1, 0, 0.01, 0, 0], None, None]
       immobilizedBy = ['Chain Bola']
       breeding = {'gestationTime': 0, 'incubationTime': 0, 'maturationTime': 166666.667, 'matingCooldownMin': 64800, 'matingCooldownMax': 172800}
       colors = [{'name': 'Unknown', 'colors': ['Black', 'Dark Red', 'Dino Albino', 'Red']}, {'name': 'Unknown', 'colors': ['Black', 'Dark Red', 'Dino Albino', 'Red']}, None, None, None, {'name': 'Unknown', 'colors': ['Black', 'Dark Red', 'Dino Albino', 'Red']}]
       taming = {'nonViolent': False, 'violent': False, 'tamingIneffectiveness': 1.875, 'affinityNeeded0': 2000, 'affinityIncreasePL': 100, 'foodConsumptionBase': 0.001852, 'foodConsumptionMult': 199.984}
       boneDamageAdjusters = {'Cnt_Head_JNT_SKL': 3, 'Cnt_Neck_002_JNT_SKL': 3, 'Cnt_Neck_000_JNT_SKL': 3}
       TamedBaseHealthMultiplier = 1
       displayedStats = 919
