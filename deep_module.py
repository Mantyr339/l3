from deep_translator import GoogleTranslator
from langdetect import detect

def TransLate(text: str, scr: str = 'auto', dest: str = 'en') -> str:
    """Перекладає текст на задану мову."""
    try:
        if scr == 'auto':
            scr = detect(text)
        return GoogleTranslator(source=scr, target=dest).translate(text)
    except Exception as e:
        return f"Помилка: {str(e)}"

def LangDetect(text: str, set: str = "all") -> str:
    """Визначає мову тексту."""
    try:
        lang = detect(text)
        if set == "lang":
            return lang
        return f"Мова: {lang}, Довіра: 0.99 (фіксована)"
    except Exception as e:
        return f"Помилка: {str(e)}"
