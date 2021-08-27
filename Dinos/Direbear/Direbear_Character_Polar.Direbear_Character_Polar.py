import sys,sce
class Direbear_Character_Polar(sce.BaseCreature):
   def __init__(self):
       super().__init__(self)
       name = 'Polar Bear'
       blueprintPath = '/Game/PrimalEarth/Dinos/Direbear/Direbear_Character_Polar.Direbear_Character_Polar'
       fullStatsRaw = [[800, 0.2, 0.27, 0.5, 0], [500, 0.1, 0.1, 0, 0], [1000, 0.06, 0, 0.5, 0], [270, 0.1, 0.1, 0, 0], [3000, 0.1, 0.1, 0, 0], None, None, [650, 0.02, 0.04, 0, 0], [1, 0.05, 0.1, 0.5, 0.4], [1, 0, 0.01, 1.226, 0], None, None]
       altBaseStats = {'0': 400}
       immobilizedBy = ['Chain Bola', 'Large Bear Trap']
       breeding = {'gestationTime': 14285.7143, 'incubationTime': 0, 'maturationTime': 166666.667, 'matingCooldownMin': 64800, 'matingCooldownMax': 172800}
       colors = [{'name': 'Unknown', 'colors': ['White']}, {'name': 'Unknown', 'colors': ['White']}, None, {'name': 'Unknown', 'colors': ['White']}, {'name': 'Unknown', 'colors': ['White']}, {'name': 'Unknown', 'colors': ['White']}]
       taming = {'nonViolent': False, 'violent': False, 'tamingIneffectiveness': 1.25, 'affinityNeeded0': 4000, 'affinityIncreasePL': 125, 'foodConsumptionBase': 0.003156, 'foodConsumptionMult': 150}
       TamedBaseHealthMultiplier = 1
       displayedStats = 927
