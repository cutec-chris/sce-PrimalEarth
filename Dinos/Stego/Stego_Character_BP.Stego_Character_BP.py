import sys,sce
class Stego_Character_BP(sce.Dinos):
   def __init__(self):
       super().__init__(self)
       name = 'Stegosaurus'
       blueprintPath = '/Game/PrimalEarth/Dinos/Stego/Stego_Character_BP.Stego_Character_BP'
       fullStatsRaw = [[650, 0.2, 0.27, 0.5, 0], [300, 0.1, 0.1, 0, 0], [500, 0.06, 0, 0.5, 0], [150, 0.1, 0.1, 0, 0], [6000, 0.1, 0.1, 0, 0], None, None, [500, 0.02, 0.04, 0, 0], [1, 0.05, 0.1, 0.5, 0.4], [1, 0, 0.02, 0.964, 0], None, None]
       immobilizedBy = ['Chain Bola', 'Large Bear Trap', 'Plant Species Y']
       breeding = {'gestationTime': 0, 'incubationTime': 9999.20006, 'eggTempMin': 22, 'eggTempMax': 28, 'maturationTime': 185185.185, 'matingCooldownMin': 64800, 'matingCooldownMax': 172800}
       colors = [{'name': 'Body', 'colors': ['Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Dark Green', 'Dino Dark Orange', 'Dino Dark Red', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Medium Brown', 'Dino Medium Green']}, {'name': 'Spine', 'colors': ['Black', 'Dark Grey', 'Dino Dark Blue', 'Dino Dark Brown', 'Dino Dark Green', 'Dino Dark Orange', 'Dino Dark Purple', 'Dino Dark Red', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Medium Brown', 'Dino Medium Green']}, {'name': 'Plate Base and Spike Base', 'colors': ['Black', 'Dark Grey', 'Dino Dark Blue', 'Dino Dark Brown', 'Dino Dark Orange', 'Dino Dark Purple', 'Dino Dark Red', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Medium Brown']}, {'name': 'Back', 'colors': ['Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Dark Green', 'Dino Dark Orange', 'Dino Dark Red', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Medium Brown', 'Dino Medium Green']}, {'name': 'Plate Edge and Spike Tips', 'colors': ['BigFoot0', 'BigFoot4', 'BigFoot5', 'Black', 'Cream', 'Dino Light Blue', 'Dino Light Brown', 'Dino Light Orange', 'Dino Light Purple', 'Dino Light Yellow', 'Dino Medium Brown', 'Light Grey', 'WolfFur']}, {'name': 'Belly', 'colors': ['Black', 'Dino Light Brown', 'Dino Light Green', 'Dino Light Orange', 'Dino Light Yellow', 'Dino Medium Brown', 'Dino Medium Green', 'Light Grey']}]
       taming = {'nonViolent': False, 'violent': True, 'tamingIneffectiveness': 0.1, 'affinityNeeded0': 6000, 'affinityIncreasePL': 300, 'torporDepletionPS0': 0.3, 'foodConsumptionBase': 0.005341, 'foodConsumptionMult': 208.0343}
       boneDamageAdjusters = {'Cnt_Head_JNT_SKL': 1.67, 'Cnt_Jaw_JNT_SKL': 1.67, 'Cnt_Neck_004_JNT_SKL': 1.67, 'Cnt_Spine_002_JNT_SKL': 0.7, 'Cnt_Spine_001_JNT_SKL': 0.7, 'Cnt_Spine_000_JNT_SKL': 0.7, 'Cnt_Spine_003_JNT_SKL': 0.7, 'Cnt_Tail_000_JNT_SKL': 0.7}
       TamedBaseHealthMultiplier = 1
       displayedStats = 927
