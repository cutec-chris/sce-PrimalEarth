import sys,sce
class Kaprosuchus_Character_BP(sce.Dinos):
   def __init__(self):
       super().__init__(self)
       name = 'Kaprosuchus'
       blueprintPath = '/Game/PrimalEarth/Dinos/Kaprosuchus/Kaprosuchus_Character_BP.Kaprosuchus_Character_BP'
       fullStatsRaw = [[200, 0.2, 0.27, 0.5, 0], [350, 0.1, 0.1, 0, 0], [200, 0.06, 0, 0.5, 0], [150, 0.1, 0.1, 0, 0], [1200, 0.1, 0.1, 0, 0], None, None, [140, 0.02, 0.04, 0, 0], [1, 0.05, 0.1, 0.5, 0.4], [1, 0, 0.01, 0.2, 0], None, None]
       immobilizedBy = ['Chain Bola', 'Bear Trap', 'Large Bear Trap', 'Plant Species Y']
       breeding = {'gestationTime': 0, 'incubationTime': 7199.42405, 'eggTempMin': 29, 'eggTempMax': 35, 'maturationTime': 133333.333, 'matingCooldownMin': 64800, 'matingCooldownMax': 172800}
       colors = [{'name': 'Body', 'colors': ['Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Dark Green', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Light Yellow', 'Dino Medium Brown', 'Dino Medium Green']}, {'name': 'Top Fins', 'colors': ['Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Dark Green', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Light Yellow', 'Dino Medium Brown', 'Dino Medium Green']}, None, None, {'name': 'Top Scales', 'colors': ['Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Dark Green', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Light Yellow', 'Dino Medium Brown', 'Dino Medium Green']}, {'name': 'Underbelly', 'colors': ['Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Dark Green', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Light Yellow', 'Dino Medium Brown', 'Dino Medium Green']}]
       taming = {'nonViolent': False, 'violent': True, 'tamingIneffectiveness': 2.5, 'affinityNeeded0': 2000, 'affinityIncreasePL': 75, 'torporDepletionPS0': 0.3, 'foodConsumptionBase': 0.001543, 'foodConsumptionMult': 648.0881}
       TamedBaseHealthMultiplier = 1
       displayedStats = 919
