import sys,sce
class Purlovia_Character_BP_Polar(sce.BaseCreature):
   def __init__(self):
       super().__init__(self)
       name = 'Polar Purlovia'
       blueprintPath = '/Game/PrimalEarth/Dinos/Purlovia/Purlovia_Character_BP_Polar.Purlovia_Character_BP_Polar'
       fullStatsRaw = [[550, 0.2, 0.27, 0.5, 0], [300, 0.1, 0.1, 0, 0], [500, 0.06, 0, 0.5, 0], [150, 0.1, 0.1, 0, 0], [4000, 0.1, 0.1, 0, 0], None, None, [400, 0.02, 0.04, 0, 0], [1, 0.05, 0.1, 0.5, 0.4], [1, 0, 0.01, 0, 0], None, None]
       altBaseStats = {'0': 275}
       immobilizedBy = ['Chain Bola', 'Large Bear Trap', 'Plant Species Y']
       breeding = {'gestationTime': 15037.594, 'incubationTime': 0, 'maturationTime': 175438.596, 'matingCooldownMin': 64800, 'matingCooldownMax': 172800}
       colors = [{'name': 'Unknown', 'colors': ['White']}, None, {'name': 'Unknown', 'colors': ['White']}, {'name': 'Unknown', 'colors': ['White']}, {'name': 'Unknown', 'colors': ['White']}, {'name': 'Unknown', 'colors': ['White']}]
       taming = {'nonViolent': False, 'violent': False, 'tamingIneffectiveness': 3.125, 'affinityNeeded0': 2250, 'affinityIncreasePL': 100, 'foodConsumptionBase': 0.001543, 'foodConsumptionMult': 288.0392}
       TamedBaseHealthMultiplier = 1
       displayedStats = 927
