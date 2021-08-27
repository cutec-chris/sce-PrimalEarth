import sys,sce
class MegaMegalodon_Character_BP(sce.BaseCreature):
   def __init__(self):
       super().__init__(self)
       name = 'Alpha Megalodon'
       blueprintPath = '/Game/PrimalEarth/Dinos/Megalodon/MEgaMegalodon_Character_BP.MegaMegalodon_Character_BP'
       variants = ['Mega']
       fullStatsRaw = [[9600, 0.2, 0.27, 0.3, 0], [320, 0.1, 0.1, 0, 0], [800, 0.06, 0, 0.5, 0], [150, 0.1, 0.1, 0, 0], [2000, 0.1, 0.1, 0, 0.15], None, None, [250, 0.02, 0.04, 0, 0], [1, 0.05, 0.1, 1, 0.4], [1, 0, 0.01, 0, 0], None, None]
       immobilizedBy = []
       breeding = {'gestationTime': 21978.022, 'incubationTime': 0, 'maturationTime': 256410.256, 'matingCooldownMin': 64800, 'matingCooldownMax': 172800}
       colors = [{'name': 'Unknown', 'colors': ['Black', 'Dino Albino']}, None, None, None, {'name': 'Unknown', 'colors': ['Black', 'Dark Red', 'Dino Albino', 'Red']}, {'name': 'Unknown', 'colors': ['Black', 'Dark Red', 'Dino Albino', 'Red']}]
       taming = {'nonViolent': False, 'violent': False, 'tamingIneffectiveness': 1.875, 'affinityNeeded0': 2000, 'affinityIncreasePL': 100, 'foodConsumptionBase': 0.001852, 'foodConsumptionMult': 199.984}
       TamedBaseHealthMultiplier = 1
       displayedStats = 919
