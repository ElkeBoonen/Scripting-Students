def count_chars(text, char):
    """ Counts specific character in given text
    Parameters
        text: string
        char: single character
    Returns:
        count
    """
    count = 0
    for c in text:
        if c == char:
            count+=1
    return count

def translate(text, lang):
    """ Translates text from English to given language
    Parameters
        text: string
        lang: ISO code language
    Returns
        translated text
    """

    import requests

    url = "https://translo.p.rapidapi.com/api/v3/translate"

    payload = {
        "from": "en",
        "to": lang,
        "text": text
    }
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "X-RapidAPI-Key": "",
        "X-RapidAPI-Host": "translo.p.rapidapi.com"
    }

    response = requests.post(url, data=payload, headers=headers)

    return response.json()["translated_text"]
