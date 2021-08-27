import sys,sce
class BionicTrike_Character_BP(sce.BaseCreature):
   def __init__(self):
       super().__init__(self)
       name = 'Tek Triceratops'
       blueprintPath = '/Game/PrimalEarth/Dinos/Trike/BionicTrike_Character_BP.BionicTrike_Character_BP'
       fullStatsRaw = [[375, 0.2, 0.27, 0.5, 0], [150, 0.1, 0.1, 0, 0], [250, 0.06, 0, 0.5, 0], [150, 0.1, 0.1, 0, 0], [3000, 0.1, 0.1, 0, 0], None, None, [365, 0.02, 0.04, 0, 0], [1, 0.05, 0.1, 0.5, 0.4], [1, 0, 0.015, 1.2, 0], None, None]
       immobilizedBy = ['Chain Bola', 'Large Bear Trap', 'Plant Species Y']
       breeding = {'gestationTime': 0, 'incubationTime': 8999.28006, 'eggTempMin': 22, 'eggTempMax': 28, 'maturationTime': 166666.667, 'matingCooldownMin': 64800, 'matingCooldownMax': 172800}
       colors = [{'name': 'Internals', 'colors': ['Dark Grey', 'Dino Dark Brown', 'Dino Dark Orange', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Light Blue', 'Dino Light Yellow', 'Dino Medium Brown', 'DragonBase0', 'DragonBase1', 'DragonFire', 'Light Brown', 'Light Grey', 'Light Orange', 'Light Yellow', 'NearBlack', 'NearWhite']}, {'name': 'Legs', 'colors': ['Dark Grey', 'Dino Dark Brown', 'Dino Dark Orange', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Light Blue', 'Dino Light Yellow', 'Dino Medium Brown', 'DragonBase0', 'DragonBase1', 'DragonFire', 'Light Brown', 'Light Grey', 'Light Orange', 'Light Yellow', 'NearBlack', 'NearWhite']}, {'name': 'Body Main', 'colors': ['Dark Grey', 'Dino Dark Brown', 'Dino Dark Orange', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Light Blue', 'Dino Light Yellow', 'Dino Medium Brown', 'DragonBase0', 'DragonBase1', 'DragonFire', 'Light Brown', 'Light Grey', 'Light Orange', 'Light Yellow', 'NearBlack', 'NearWhite']}, {'name': 'Head Main', 'colors': ['Dark Grey', 'Dino Dark Brown', 'Dino Dark Orange', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Light Blue', 'Dino Light Yellow', 'Dino Medium Brown', 'DragonBase0', 'DragonBase1', 'DragonFire', 'Light Brown', 'Light Grey', 'Light Orange', 'Light Yellow', 'NearBlack', 'NearWhite']}, {'name': 'UnderBelly', 'colors': ['Dark Grey', 'Dino Dark Brown', 'Dino Dark Orange', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Light Blue', 'Dino Light Yellow', 'Dino Medium Brown', 'DragonBase0', 'DragonBase1', 'DragonFire', 'Light Brown', 'Light Grey', 'Light Orange', 'Light Yellow', 'NearBlack', 'NearWhite']}, {'name': 'Emissive', 'colors': ['Dino Albino', 'Dino Light Blue', 'Dino Light Purple', 'Light Green', 'Light Orange', 'Light Red', 'Light Yellow']}]
       taming = {'nonViolent': False, 'violent': True, 'tamingIneffectiveness': 0.2, 'affinityNeeded0': 3000, 'affinityIncreasePL': 150, 'torporDepletionPS0': 0.3, 'foodConsumptionBase': 0.003156, 'foodConsumptionMult': 352.0631}
       boneDamageAdjusters = {'c_head': 0.15, 'c_jaw': 0.15}
       TamedBaseHealthMultiplier = 1
       displayedStats = 927
