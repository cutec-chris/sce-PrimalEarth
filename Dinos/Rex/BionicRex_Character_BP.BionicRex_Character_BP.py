import sys,sce
class BionicRex_Character_BP(sce.Tek Creatures):
   def __init__(self):
       super().__init__(self)
       name = 'Tek Rex'
       blueprintPath = '/Game/PrimalEarth/Dinos/Rex/BionicRex_Character_BP.BionicRex_Character_BP'
       fullStatsRaw = [[1100, 0.2, 0.27, 0.5, 0], [420, 0.1, 0.1, 0, 0], [1550, 0.06, 0, 0.5, 0], [150, 0.1, 0.1, 0, 0], [3000, 0.1, 0.1, 0, 0], None, None, [500, 0.02, 0.04, 0, 0], [1, 0.05, 0.1, 0.5, 0.4], [1, 0, 0.01, 0, 0], None, None]
       immobilizedBy = ['Chain Bola', 'Large Bear Trap']
       breeding = {'gestationTime': 0, 'incubationTime': 17998.5601, 'eggTempMin': 32, 'eggTempMax': 34, 'maturationTime': 333333.333, 'matingCooldownMin': 64800, 'matingCooldownMax': 172800}
       colors = [{'name': 'Head Main', 'colors': ['Black', 'Dark Grey', 'Dino Albino', 'Dino Dark Blue', 'Dino Dark Green', 'Dino Dark Yellow', 'Dino Darker Grey', 'DragonGreen0', 'DragonGreen2', 'DragonGreen3', 'Light Grey', 'NearWhite', 'WyvernBlue0']}, {'name': 'Spine', 'colors': ['Black', 'Dark Grey', 'Dino Albino', 'Dino Dark Blue', 'Dino Dark Green', 'Dino Darker Grey', 'DragonGreen0', 'DragonGreen3', 'Light Grey', 'NearWhite']}, {'name': 'Body Main', 'colors': ['Black', 'Dark Grey', 'Dino Albino', 'Dino Dark Blue', 'Dino Dark Green', 'Dino Dark Yellow', 'Dino Darker Grey', 'DragonGreen0', 'DragonGreen2', 'DragonGreen3', 'Light Grey', 'NearWhite', 'WyvernBlue0']}, {'name': 'Body Highlights', 'colors': ['Black', 'Dark Grey', 'Dino Albino', 'Dino Dark Blue', 'Dino Dark Green', 'Dino Darker Grey', 'DragonGreen0', 'DragonGreen3', 'Light Grey', 'NearWhite', 'WyvernBlue0']}, {'name': 'Internals', 'colors': ['Black', 'Dark Grey', 'Dino Albino', 'Dino Dark Blue', 'Dino Dark Green', 'Dino Darker Grey', 'Dino Deep Blue', 'Dino Medium Blue', 'DragonGreen0', 'DragonGreen3', 'Light Grey', 'NearWhite']}, {'name': 'Emissives', 'colors': ['Blue', 'Cyan', 'Dino Albino', 'Green', 'Magenta', 'Red', 'Yellow']}]
       taming = {'nonViolent': False, 'violent': True, 'tamingIneffectiveness': 1.25, 'affinityNeeded0': 3450, 'affinityIncreasePL': 150, 'torporDepletionPS0': 0.725, 'foodConsumptionBase': 0.002314, 'foodConsumptionMult': 180.0634}
       TamedBaseHealthMultiplier = 1
       displayedStats = 927
