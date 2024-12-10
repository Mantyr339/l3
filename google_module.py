from googletrans import Translator
from googletrans.constants import LANGUAGES

translator = Translator()


def TransLate(text: str, scr: str = 'auto', dest: str = 'en') -> str:
    """Перекладає текст на задану мову."""
    try:
        result = translator.translate(text, src=scr, dest=dest)
        return result.text
    except Exception as e:
        return f"Помилка: {str(e)}"


def LangDetect(text: str, set: str = "all") -> str:
    """Визначає мову тексту та коефіцієнт довіри."""
    try:
        detected = translator.detect(text)
        if set == "lang":
            return detected.lang
        elif set == "confidence":
            return detected.confidence
        return f"Мова: {detected.lang}, Довіра: {detected.confidence}"
    except Exception as e:
        return f"Помилка: {str(e)}"


def CodeLang(lang: str) -> str:
    """Повертає код мови або назву за введеними даними."""
    try:
        if lang in LANGUAGES.values():
            return list(LANGUAGES.keys())[list(LANGUAGES.values()).index(lang)]
        elif lang in LANGUAGES.keys():
            return LANGUAGES[lang]
        return "Помилка: Мова не знайдена."
    except Exception as e:
        return f"Помилка: {str(e)}"


def LanguageList(out: str = "screen", text: str = None) -> str:
    """Виводить список мов з перекладом заданого тексту."""
    try:
        rows = []
        for idx, (code, lang) in enumerate(LANGUAGES.items(), start=1):
            translation = translator.translate(text, dest=code).text if text else ""
            rows.append(f"{idx:<3} {lang:<15} {code:<10} {translation:<20}")

        if out == "screen":
            print("N   Language         ISO-639    Text")
            print("-" * 50)
            print("\n".join(rows))
        elif out == "file":
            with open("languages.txt", "w", encoding="utf-8") as f:
                f.write("\n".join(rows))
        return "Ok"
    except Exception as e:
        return f"Помилка: {str(e)}"
