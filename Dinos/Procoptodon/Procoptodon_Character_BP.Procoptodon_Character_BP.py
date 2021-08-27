import sys,sce
class Procoptodon_Character_BP(sce.Dinos):
   def __init__(self):
       super().__init__(self)
       name = 'Procoptodon'
       blueprintPath = '/Game/PrimalEarth/Dinos/Procoptodon/Procoptodon_Character_BP.Procoptodon_Character_BP'
       fullStatsRaw = [[400, 0.2, 0.27, 0.75, 0], [350, 0.1, 0.1, 0.1, 0], [350, 0.06, 0, 0.5, 0], [150, 0.1, 0.1, 0, 0], [1500, 0.1, 0.1, 0, 0], None, None, [550, 0.02, 0.04, 0, 0], [1, 0.05, 0.1, 0.2, 0.25], [1, 0, 0.01, 0, 0], None, None]
       immobilizedBy = ['Chain Bola', 'Large Bear Trap']
       breeding = {'gestationTime': 14285.7143, 'incubationTime': 0, 'maturationTime': 166666.667, 'matingCooldownMin': 64800, 'matingCooldownMax': 172800}
       colors = [{'name': 'Body', 'colors': ['BigFoot0', 'BigFoot4', 'BigFoot5', 'Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Dark Orange', 'Dino Darker Grey', 'Dino Light Brown', 'Dino Light Orange', 'Dino Medium Brown', 'Light Grey']}, None, None, None, {'name': 'Back Stripes', 'colors': ['BigFoot0', 'BigFoot4', 'BigFoot5', 'Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Dark Orange', 'Dino Darker Grey', 'Dino Light Brown', 'Dino Light Orange', 'Dino Medium Brown', 'Light Grey']}, {'name': 'Inner Ear, Snout, Belly, Appendages', 'colors': ['BigFoot0', 'BigFoot4', 'BigFoot5', 'Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Dark Orange', 'Dino Darker Grey', 'Dino Light Brown', 'Dino Light Orange', 'Dino Medium Brown', 'Light Grey']}]
       taming = {'nonViolent': False, 'violent': True, 'tamingIneffectiveness': 0.2, 'affinityNeeded0': 3000, 'affinityIncreasePL': 150, 'torporDepletionPS0': 0.6666, 'foodConsumptionBase': 0.001929, 'foodConsumptionMult': 648.0041}
       TamedBaseHealthMultiplier = 1
       displayedStats = 927
