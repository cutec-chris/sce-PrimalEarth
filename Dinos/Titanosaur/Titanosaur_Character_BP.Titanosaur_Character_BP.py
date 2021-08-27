import sys,sce
class Titanosaur_Character_BP(sce.BaseCreature):
   def __init__(self):
       super().__init__(self)
       name = 'Titanosaur'
       blueprintPath = '/Game/PrimalEarth/Dinos/Titanosaur/Titanosaur_Character_BP.Titanosaur_Character_BP'
       fullStatsRaw = [[230000, 0, 0, -80000, 0], [2000, 0, 0, 0, 0], [25000, 0.06, 0, 0.5, 0], [600, 0, 0, 0, 0], [8640, 0, 0, 0, 0], None, None, [50000, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0, 0, 0], None, None]
       immobilizedBy = []
       colors = [{'name': 'Body', 'colors': ['Black', 'Dino Light Brown', 'Dino Light Green', 'Dino Light Orange', 'Dino Light Yellow', 'Dino Medium Brown', 'Dino Medium Green', 'Light Grey']}, None, None, None, {'name': 'Back', 'colors': ['Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Dark Green', 'Dino Dark Orange', 'Dino Dark Red', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Medium Brown', 'Dino Medium Green']}, {'name': 'Underside', 'colors': ['Black', 'Dino Light Brown', 'Dino Light Green', 'Dino Light Orange', 'Dino Light Yellow', 'Dino Medium Brown', 'Dino Medium Green', 'Light Grey']}]
       taming = {'nonViolent': False, 'violent': True, 'tamingIneffectiveness': 0.06, 'affinityNeeded0': 10000, 'affinityIncreasePL': 500, 'torporDepletionPS0': 0, 'foodConsumptionBase': 0.1, 'foodConsumptionMult': 13}
       TamedBaseHealthMultiplier = 1.8
       displayedStats = 927
