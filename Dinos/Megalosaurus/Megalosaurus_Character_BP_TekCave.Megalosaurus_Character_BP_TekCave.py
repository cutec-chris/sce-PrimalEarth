import sys,sce
class Megalosaurus_Character_BP_TekCave(sce.BaseCreature):
   def __init__(self):
       super().__init__(self)
       name = 'Megalosaurus'
       blueprintPath = '/Game/PrimalEarth/Dinos/Megalosaurus/Megalosaurus_Character_BP_TekCave.Megalosaurus_Character_BP_TekCave'
       variants = ['Cave', 'TekCave']
       fullStatsRaw = [[1025, 0.2, 0.27, 0.5, 0], [300, 0.1, 0.1, 0, 0], [775, 0.06, 0, 0.5, 0], [150, 0.1, 0.1, 0, 0], [2000, 0.1, 0.1, 0, 0.15], None, None, [300, 0.02, 0.04, 0, 0], [1, 0.05, 0.1, 0.5, 0.4], [1, 0, 0.01, 0, 0], None, None]
       immobilizedBy = ['Chain Bola', 'Large Bear Trap', 'Plant Species Y']
       breeding = {'gestationTime': 0, 'incubationTime': 5999.52004, 'eggTempMin': 26, 'eggTempMax': 32, 'maturationTime': 333333.333, 'matingCooldownMin': 64800, 'matingCooldownMax': 172800}
       colors = [{'name': 'Face, Appendages, Sides', 'colors': ['Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Dark Orange', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Light Brown', 'Dino Light Green', 'Dino Light Orange', 'Dino Light Yellow', 'Dino Medium Brown', 'DragonBase0', 'DragonGreen0', 'DragonGreen1', 'Light Grey']}, None, None, None, {'name': 'Feathers, Osteoderms, Patterning', 'colors': ['Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Dark Orange', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Medium Brown', 'DragonBase0', 'DragonGreen0', 'DragonGreen1']}, {'name': 'Belly', 'colors': ['Black', 'Dino Light Blue', 'Dino Light Brown', 'Dino Light Green', 'Dino Light Yellow', 'Dino Medium Brown', 'DragonGreen2', 'Light Grey']}]
       taming = {'nonViolent': False, 'violent': True, 'tamingIneffectiveness': 1.875, 'affinityNeeded0': 3450, 'affinityIncreasePL': 150, 'torporDepletionPS0': 0.3, 'foodConsumptionBase': 0.001852, 'foodConsumptionMult': 199.984}
       boneDamageAdjusters = {'Cnt_Head_JNT_SKL': 3, 'Cnt_Neck_002_JNT_SKL': 3, 'Cnt_Neck_000_JNT_SKL': 3}
       TamedBaseHealthMultiplier = 1
       displayedStats = 927
