import random
from tqdm import tqdm
import time

# ANSI escape codes for text styles
BOLD = "\033[1m"
RESET = "\033[0m"

# ANSI escape codes for colors (example colors)
BLACK = "\033[30m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"

def rgb_color(r, g, b):
    return f"\033[38;2;{r};{g};{b}m"

def pt(text, color_code):
    print(f"{BOLD}{color_code}{text}{RESET}")

# Функция для создания вертикального градиента от красного к желтому
def vertical_gradient_text(text):
    # Задаем список RGB-кодов для градиента
    gradient_colors = [
        "\033[38;2;255;0;0m",  # Красный
        "\033[38;2;255;51;0m",  # Оранжевый
        "\033[38;2;255;102;0m",  # Более светлый оранжевый
        "\033[38;2;255;153;0m",  # Ещё более светлый оранжевый
        "\033[38;2;255;204;0m",  # Желтый оранжевый
        "\033[38;2;255;255;0m"  # Желтый
    ]
    lines = text.split("\n")
    num_lines = len(lines)

    # Вычисляем сколько строк должен занимать каждый цвет
    num_colors = len(gradient_colors)
    lines_per_color = num_lines / num_colors

    for i, line in enumerate(lines):
        color_index = min(int(i / lines_per_color), num_colors - 1)
        color = gradient_colors[color_index]
        print(color + line + "\033[0m")  # \033[0m сбрасывает цвет


class Emotion:
    def __init__(self, name, intensity=0):
        self.name = name
        self.intensity = intensity  # Интенсивность эмоции от 0 до 100

    def __repr__(self):
        return f"{self.name} (Интенсивность: {self.intensity})"


class Human:
    def __init__(self, name):
        self.name = name
        self.mood = "нейтральное"
        self.emotions = {
            "счастье": Emotion("Счастье", random.randint(10, 50)),
            "грусть": Emotion("Грусть", random.randint(0, 50)),
            "злость": Emotion("Злость", random.randint(0, 50)),
            "страх": Emotion("Страх", random.randint(0, 50)),
            "любовь": Emotion("Любовь", random.randint(10, 50)),
            "скука": Emotion("Скука", random.randint(0, 50)),
        }
        self.energy = random.randint(50, 100)
        self.health = random.randint(60, 100)

    def assess_mood(self):
        if self.emotions["счастье"].intensity > 50:
            self.mood = "счастливое"
        elif self.emotions["грусть"].intensity > 50:
            self.mood = "грустное"
        elif self.emotions["злость"].intensity > 50:
            self.mood = "злое"
        elif self.emotions["страх"].intensity > 50:
            self.mood = "испуганное"
        else:
            self.mood = "нейтральное"

    def experience_event(self, event):
        if event == "хорошие новости":
            self.emotions["счастье"].intensity += random.randint(10, 30)
            self.emotions["грусть"].intensity -= random.randint(0, 20)
        elif event == "плохие новости":
            self.emotions["грусть"].intensity += random.randint(10, 30)
            self.emotions["счастье"].intensity -= random.randint(0, 20)
        elif event == "оскорбление":
            self.emotions["злость"].intensity += random.randint(20, 40)
            self.emotions["счастье"].intensity -= random.randint(0, 10)
        elif event == "страшное событие":
            self.emotions["страх"].intensity += random.randint(20, 40)
            self.emotions["счастье"].intensity -= random.randint(0, 10)
        elif event == "романтическое событие":
            self.emotions["любовь"].intensity += random.randint(10, 40)
        elif event == "скука":
            self.emotions["скука"].intensity += random.randint(10, 30)

        self.limit_emotions()
        self.assess_mood()

    def limit_emotions(self):
        for emotion in self.emotions.values():
            emotion.intensity = max(0, min(emotion.intensity, 100))

    def react(self):
        reactions = {
            "счастливое": f"{self.name} улыбается и чувствует себя прекрасно!",
            "грустное": f"{self.name} выглядит печальным и унылым.",
            "злое": f"{self.name} очень сердит и может накричать.",
            "испуганное": f"{self.name} выглядит испуганным и тревожным.",
            "нейтральное": f"{self.name} спокоен и нейтрален.",
        }
        return reactions[self.mood]

    def __repr__(self):
        return (f"Человек: {self.name}\n"
                f"Энергия: {self.energy}\n"
                f"Здоровье: {self.health}\n"
                f"Настроение: {self.mood}\n"
                f"Эмоции: {self.emotions}")


# ASCII оформление с градиентом
def print_ascii_art():
    art = r"""
                                                                                                    v0.1
███████╗███╗   ███╗ ██████╗ ████████╗███████╗███████╗████████╗    ██████╗ ███████╗████████╗ █████╗ 
██╔════╝████╗ ████║██╔═══██╗╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝    ██╔══██╗██╔════╝╚══██╔══╝██╔══██╗
█████╗  ██╔████╔██║██║   ██║   ██║   █████╗  ███████╗   ██║       ██████╔╝█████╗     ██║   ███████║
██╔══╝  ██║╚██╔╝██║██║   ██║   ██║   ██╔══╝  ╚════██║   ██║       ██╔══██╗██╔══╝     ██║   ██╔══██║
███████╗██║ ╚═╝ ██║╚██████╔╝   ██║   ███████╗███████║   ██║       ██████╔╝███████╗   ██║   ██║  ██║
╚══════╝╚═╝     ╚═╝ ╚═════╝    ╚═╝   ╚══════╝╚══════╝   ╚═╝       ╚═════╝ ╚══════╝   ╚═╝   ╚═╝  ╚═╝                                                                                                              
    """
    vertical_gradient_text(art)


# Генерация простой нейронной сети (ASCII форма)
def generate_neural_network():
    for i in tqdm(range(100), ncols=80, desc='Процесс'):
        time.sleep(0.5)

    pt("Нейронная сеть сгенерирована:", rgb_color(255, 145, 0))


def main():
    print_ascii_art()

    # Создание объекта человека
    names = ['Алексей', 'Роман', 'Владимир', 'Артём', 'Павел', 'Сергей', 'Максим', 'Тимофей']
    person = Human(random.choice(names))
    pt(str(person), rgb_color(255, 145, 0))

    # Генерация нейронной сети
    generate_neural_network()

    # Испытание различных событий
    events = ["хорошие новости", "плохие новости", "оскорбление", "страшное событие", "романтическое событие", "скука"]

    event = random.choice(events)
    pt(f"\nПроизошло событие: {event}", rgb_color(255, 145, 0))
    person.experience_event(event)
    pt(person.react(), rgb_color(255, 145, 0))
    time.sleep(1)


if __name__ == "__main__":
    main()