import json
from VOVkl3.google_module import TransLate

def read_config():
    try:
        with open("config.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"Помилка читання конфігураційного файлу: {str(e)}")
        return None

def main():
    config = read_config()
    if not config:
        return

    try:
        with open(config["text_file"], "r", encoding="utf-8") as f:
            text = f.read()
        translated_text = TransLate(text, dest=config["target_language"])
        if config["output"] == "screen":
            print(f"Переклад:\n{translated_text}")
        else:
            with open(f"output_{config['target_language']}.txt", "w", encoding="utf-8") as out:
                out.write(translated_text)
            print("Ok")
    except Exception as e:
        print(f"Помилка: {str(e)}")

if __name__ == "__main__":
    main()
