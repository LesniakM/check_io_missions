VOWELS = "aeiou"


class Chat:
    def __init__(self):
        self.chat_data = []
        self.participants = []

    def connect_human(self, human):
        human.update_chat = self.update_chat

    def connect_robot(self, robot):
        robot.update_chat = self.update_chat

    def update_chat(self, data):
        self.chat_data.append((f"{data[0]} said: ", data[1]))

    def show_human_dialogue(self):
        return "\n".join(x[0] + x[1] for x in self.chat_data)

    def show_robot_dialogue(self):
        return "\n".join(x[0] + "".join(list(self.translate_to_robot(x[1]))) for x in self.chat_data)

    @staticmethod
    def translate_to_robot(data):
        for char in data.lower():
            if char in VOWELS:
                yield "0"
            else:
                yield "1"


class Participant:
    def __init__(self, name):
        self.update_chat = None
        self.name = name

    def send(self, data):
        self.update_chat((self.name, data))


class Human(Participant):
    pass


class Robot(Participant):
    pass


chat = Chat()
carl = Human("Carl")
chat.connect_human(carl)
carl.send("Sram ostro mordo")
carl.send("serio")
chat.show_human_dialogue()
chat.show_robot_dialogue()
