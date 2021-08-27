import sys,sce
class BionicRaptor_Character_BP(sce.Tek Creatures):
   def __init__(self):
       super().__init__(self)
       name = 'Tek Raptor'
       blueprintPath = '/Game/PrimalEarth/Dinos/Raptor/BionicRaptor_Character_BP.BionicRaptor_Character_BP'
       fullStatsRaw = [[200, 0.2, 0.27, 0.5, 0], [150, 0.1, 0.1, 0, 0], [180, 0.06, 0, 0.5, 0], [150, 0.1, 0.1, 0, 0], [1200, 0.1, 0.1, 0, 0], None, None, [140, 0.02, 0.04, 0, 0], [1, 0.05, 0.1, 0.5, 0.4], [1, 0, 0.015, 0.2, 0], None, None]
       immobilizedBy = ['Bola', 'Bear Trap', 'Large Bear Trap', 'Plant Species Y']
       breeding = {'gestationTime': 0, 'incubationTime': 7199.42405, 'eggTempMin': 20, 'eggTempMax': 28, 'maturationTime': 133333.333, 'matingCooldownMin': 64800, 'matingCooldownMax': 172800}
       colors = [{'name': 'Inner Body', 'colors': ['Dark Grey', 'Dark Red', 'Dino Dark Brown', 'Dino Dark Orange', 'Dino Light Blue', 'Dino Light Yellow', 'DragonBase0', 'DragonBase1', 'DragonFire', 'Light Brown', 'Light Grey', 'Light Orange', 'Light Red', 'NearBlack', 'NearWhite']}, {'name': 'Legs and Head', 'colors': ['Dark Grey', 'Dark Red', 'Dino Dark Brown', 'Dino Dark Orange', 'Dino Light Blue', 'Dino Light Yellow', 'DragonBase0', 'DragonBase1', 'DragonFire', 'Light Brown', 'Light Grey', 'Light Orange', 'Light Red', 'NearBlack', 'NearWhite']}, {'name': 'Body', 'colors': ['Dark Grey', 'Dark Red', 'Dino Dark Brown', 'Dino Dark Orange', 'Dino Light Blue', 'Dino Light Yellow', 'DragonBase0', 'DragonBase1', 'DragonFire', 'Light Brown', 'Light Grey', 'Light Orange', 'Light Red', 'NearBlack', 'NearWhite']}, {'name': 'Gears', 'colors': ['Dark Grey', 'Dark Red', 'Dino Dark Brown', 'Dino Dark Orange', 'Dino Light Blue', 'Dino Light Yellow', 'DragonBase0', 'DragonBase1', 'DragonFire', 'Light Brown', 'Light Grey', 'Light Orange', 'Light Red', 'NearBlack', 'NearWhite']}, {'name': 'Spikes and Tail', 'colors': ['Dark Grey', 'Dark Red', 'Dino Dark Brown', 'Dino Dark Orange', 'Dino Light Blue', 'Dino Light Yellow', 'DragonBase0', 'DragonBase1', 'DragonFire', 'Light Brown', 'Light Grey', 'Light Orange', 'Light Red', 'NearBlack', 'NearWhite']}, {'name': 'Emissive', 'colors': ['Dino Albino', 'Dino Light Blue', 'Dino Light Purple', 'Light Green', 'Light Orange', 'Light Red', 'Light Yellow']}]
       taming = {'nonViolent': False, 'violent': True, 'tamingIneffectiveness': 3.125, 'affinityNeeded0': 1200, 'affinityIncreasePL': 60, 'torporDepletionPS0': 0.3, 'foodConsumptionBase': 0.001543, 'foodConsumptionMult': 648.0881}
       boneDamageAdjusters = {'Cnt_Head_JNT_SKL': 3, 'Cnt_Neck_002_JNT_SKL': 3, 'Cnt_Neck_000_JNT_SKL': 3}
       TamedBaseHealthMultiplier = 1
       displayedStats = 927
