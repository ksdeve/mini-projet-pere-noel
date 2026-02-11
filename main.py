class SantaError(Exception):
    "Classe de base pour les erreurs de la fabrique."
    pass

class GiftCreationError(SantaError):
    "Levée quand le cadeau ne peut pas être créé."
    pass



class Command:
    
    def __init__(self, facade, type_gift, decoration, delivery):
        self.facade = facade
        self.type_gift = type_gift
        self.decoration = decoration
        self.delivery = delivery

    def execute(self):
        try:
            self.facade.create_and_delivery_gift(self.type_gift, self.decoration, self.delivery)
        except SantaError as e:
            print(f"Erreur lors de l'exécution de la commande : {e}")    
    
class Books:
    def description(self):
        return "Ceci est un livre"

class Clothing:
    def description(self):
        return "Ceci est un vetement"
        
class Jewellery:
    def description(self):
        return "Ceci est un bijou"
        
        
class EmballageDecorator:
    def __init__(self, gift):
        self.gift = gift
        
    def description(self):
        return self.gift.description() + " avec un emballage cadeau"
    
class RubanDecorator:
    def __init__(self, gift):
        self.gift = gift
        
    def description(self):
        return self.gift.description() + " avec un ruban"
    
class MessageDecorator:
    def __init__(self, gift):
        self.gift = gift
        
    def description(self):
        return self.gift.description() + " avec un message personnalisé"
    
    
class StrategyDelivery:
    def __init__(self, strategy):
        self.strategy = strategy
        
    def delivery(self):
        result = self.strategy.delivery()
        if result:
            return f"{result} \nLivraison effectuée"
        else:
            return "Livraison échouée"
            
            
class RennesDelivery:
    def delivery(self):
        return "Livraison express par les rennes du père noël"

class TraineauDelivery:
    def delivery(self):
        return "Livraison traditionnelle en traîneau"

class DroneDelivery:
    def delivery(self):
        return "Livraison moderne par drone"
    
    
class Lutin:
    def __init__(self, nom):
        self.nom = nom

    def update(self, message):
        print(f"[Lutin {self.nom}] Reçu : {message}")
        
    def description(self):
        return f"Lutin {self.nom}"
        
        

class NotificationService:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._lutins = []
        return cls._instance

    def add_lutin(self, lutin):
        if lutin not in self._lutins:
            self._lutins.append(lutin)

    def notifyLutin(self, message):
        for lutin in self._lutins:
            lutin.update(message)
            
            
class FactoryTraditionnelle:
    @staticmethod
    def createGift():
        return Books()
    
    @staticmethod
    def createDelivery():
        return TraineauDelivery()


class FactoryModerne:
    @staticmethod
    def createGift():
        return Jewellery()
    @staticmethod
    def createDelivery():
        return DroneDelivery()
            
            
class FactoryGift:
    @staticmethod
    def createGift(type_gift):
        types = {
            "books": Books,
            "clothing": Clothing,
            "jewellery": Jewellery
        }
        if type_gift not in types:
            raise GiftCreationError(f"Le type de cadeau '{type_gift}' est introuvable dans l'atelier")
        return types[type_gift]()
        
    
class WorkFacade:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.factory = FactoryGift()
            cls._instance.notifier = NotificationService()
            cls._instance.notifier.add_lutin(Lutin("Lutin1"))
        return cls._instance
    
    def create_themed_pack(self, factory_type):
        if factory_type == "traditionnel":
            factory = FactoryTraditionnelle()
        else:
            factory = FactoryModerne()
            
        gift = factory.createGift()
        delivery = factory.createDelivery()
        
        self.notifier.notifyLutin(f"Pack {factory_type} prêt : {gift.description()}")
        print(f"Description : {gift.description()}")
        print(f"Expédition : {delivery.delivery()} \n")

    def create_and_delivery_gift(self, type_gift, decoration_types, delivery_mode="traineau"):
        gift = self.factory.createGift(type_gift)
        
        for decor in decoration_types:
            if decor == "emballage":
                gift = EmballageDecorator(gift)
            elif decor == "ruban":
                gift = RubanDecorator(gift)
            elif decor == "message":
                gift = MessageDecorator(gift)
            
        self.notifier.notifyLutin(f"Nouveau cadeau prêt : {gift.description()}")
        
        if delivery_mode == "rennes":
            instance = RennesDelivery()
        elif delivery_mode == "drone":
            instance = DroneDelivery()
        else:
            instance = TraineauDelivery()

        gestionnaire = StrategyDelivery(instance)
        print(f"Description : {gift.description()}")
        print(f"Expédition : {gestionnaire.delivery()}\n")

class SantaInterface:
    def __init__(self):
        self.facade = WorkFacade()
        self.gifts = {"1": "books", "2": "clothing", "3": "jewellery"}
        self.decorations = {"1": "emballage", "2": "ruban", "3": "message", "4": "aucun"}
        self.deliveries = {"1": "rennes", "2": "traineau", "3": "drone"}
        self.themes = {"1": "traditionnel", "2": "moderne"}

    def get_input(self, prompt, options, default_key):
        choice = input(prompt)
        if choice not in options:
            print(f"Choix invalide. Utilisation de l'option par défaut : {options[default_key]}")
            return options[default_key]
        return options[choice]

    def afficher_interfarce(self):
        print("FABRIQUE DU PÈRE NOËL \n")
        print("1 - Commande personnalisée")
        print("2 - Pack thématique (Abstract Factory)")
        mode = input("> ")

        if mode == "2":
            print("Choisissez un thème : \n")
            print("1. Traditionnel (Livre + Traîneau)")
            print("2. Moderne (Bijou + Drone)")
            theme = self.get_input("> ", self.themes, "1")
            
            print("Préparation du Pack \n")
            self.facade.create_themed_pack(theme)

        else:
            print("Types de cadeaux : \n")
            for k, v in self.gifts.items(): print(f"{k}. {v.capitalize()}")
            gift = self.get_input("> ", self.gifts, "1")

            print("Décorations (choisissez plusieurs numéros séparés par une virgule, ex: 1,2) : \n")
            for k, v in self.decorations.items(): print(f"{k}. {v.capitalize()}")
            
            decor_choice = input("> ")

            selected_decors = []
            for char in decor_choice.split(','):
                char = char.strip()
                if char in self.decorations and self.decorations[char] != "aucun":
                    selected_decors.append(self.decorations[char])

            print("Livraison : \n")
            for k, v in self.deliveries.items(): print(f"{k}. {v.capitalize()}")
            delivery = self.get_input("> ", self.deliveries, "2")

            print("Traitement de la commande \n")
            try:

                cmd = Command(self.facade, gift, selected_decors, delivery)
                cmd.execute()
            except Exception as e:
                print(f"Erreur : {e}")

    def run(self):
        while True:
            self.afficher_interfarce()
            cont = input("Continuer ? (o/n) : ").lower()
            if cont != 'o':
                print("Fin du programme.")
                break

if __name__ == "__main__":
    ui = SantaInterface()
    ui.run()