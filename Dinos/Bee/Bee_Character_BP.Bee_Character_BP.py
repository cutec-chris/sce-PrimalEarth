import sys,sce
class Bee_Character_BP(sce.Dinos):
   def __init__(self):
       super().__init__(self)
       name = 'Giant Bee'
       blueprintPath = '/Game/PrimalEarth/Dinos/Bee/Bee_Character_BP.Bee_Character_BP'
       isFlyer = True
       fullStatsRaw = [[80, 0.2, 0.27, 0.5, 0], [200, 0.1, 0.1, 0, 0], [400, 0.06, 0, 0.5, 0], [150, 0.1, 0.1, 0, 0], [450, 0.1, 0.1, 0, 0], None, None, [150, 0.02, 0.04, 0, 0], [1, 0.05, 0.1, 0.5, 0.4], [1, 0, 0.01, 0, 0], None, None]
       immobilizedBy = []
       noGender = True
       colors = [{'name': 'BodyHighlights', 'colors': ['Dino Dark Orange', 'Dino Dark Red', 'Dino Dark Yellow', 'Dino Light Blue', 'Dino Light Orange', 'Dino Light Purple', 'Dino Light Red', 'Dino Light Yellow', 'DragonBase1', 'DragonFire']}, None, {'name': 'Legs Highlight', 'colors': ['Black', 'Dino Albino', 'Dino Dark Orange', 'Dino Dark Red', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Light Blue', 'Dino Light Orange', 'Dino Light Purple', 'Dino Light Red', 'Dino Light Yellow', 'DragonBase1', 'DragonFire']}, None, None, {'name': 'BodyDark', 'colors': ['Black', 'DarkWolfFur', 'Dino Dark Blue', 'Dino Dark Brown', 'Dino Dark Purple', 'Dino Darker Grey', 'NearBlack', 'WyvernBlue1']}]
       taming = {'nonViolent': False, 'violent': False, 'tamingIneffectiveness': 8.333333, 'affinityNeeded0': 450, 'affinityIncreasePL': 22.5, 'foodConsumptionBase': 0.001736, 'foodConsumptionMult': 864.0553}
       TamedBaseHealthMultiplier = 1
       displayedStats = 927
