import sys,sce
class BionicStego_Character_BP_Malfunctioned(sce.BaseCreature):
   def __init__(self):
       super().__init__(self)
       name = 'Malfunctioned Tek Stegosaurus'
       blueprintPath = '/Game/PrimalEarth/Dinos/Stego/BionicStego_Character_BP_Malfunctioned.BionicStego_Character_BP_Malfunctioned'
       fullStatsRaw = [[650, 0.2, 0.27, 0.5, 0], [300, 0.1, 0.1, 0, 0], [500, 0.06, 0, 0.5, 0], [150, 0.1, 0.1, 0, 0], [6000, 0.1, 0.1, 0, 0], None, None, [500, 0.02, 0.04, 0, 0], [1, 0.05, 0.1, 0.5, 0.4], [1, 0, 0.02, 0.964, 0], None, None]
       immobilizedBy = ['Chain Bola', 'Large Bear Trap', 'Plant Species Y']
       breeding = {'gestationTime': 0, 'incubationTime': 9999.20006, 'eggTempMin': 22, 'eggTempMax': 28, 'maturationTime': 185185.185, 'matingCooldownMin': 64800, 'matingCooldownMax': 172800}
       colors = [{'name': 'Head Main', 'colors': ['Black', 'Dark Grey', 'Dino Darker Grey', 'Light Grey']}, {'name': 'Spine', 'colors': ['Black', 'Dark Grey', 'Dino Darker Grey', 'Light Grey']}, {'name': 'Body Main', 'colors': ['Black', 'Dark Grey', 'Dino Darker Grey', 'Light Grey']}, {'name': 'Body Highlights', 'colors': ['Black', 'Dark Grey', 'Dino Darker Grey', 'Light Grey']}, {'name': 'Internals', 'colors': ['Red']}, {'name': 'Emissives', 'colors': ['Red']}]
       taming = {'nonViolent': False, 'violent': False, 'tamingIneffectiveness': 0.1, 'affinityNeeded0': 6000, 'affinityIncreasePL': 300, 'foodConsumptionBase': 0.005341, 'foodConsumptionMult': 208.0343}
       boneDamageAdjusters = {'Cnt_Head_JNT_SKL': 1.67, 'Cnt_Jaw_JNT_SKL': 1.67, 'Cnt_Neck_004_JNT_SKL': 1.67, 'Cnt_Spine_002_JNT_SKL': 0.7, 'Cnt_Spine_001_JNT_SKL': 0.7, 'Cnt_Spine_000_JNT_SKL': 0.7, 'Cnt_Spine_003_JNT_SKL': 0.7, 'Cnt_Tail_000_JNT_SKL': 0.7}
       TamedBaseHealthMultiplier = 1
       displayedStats = 927
