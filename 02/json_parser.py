import json


def keyword_callback_func(key, word):
    return key, word


def parse_json(json_str, keyword_callback=None, required_fields=None, keywords=None):
    if not required_fields or not keywords or not keyword_callback:
        return None

    lower_keywords = [i.lower() for i in keywords]
    json_doc = None
    try:
        json_doc = json.loads(json_str)
    except json.decoder.JSONDecodeError:
        print("Некорректный формат json строки")
        return None
    except TypeError:
        print("Некорректный тип json строки")
        return None

    for key, value in json_doc.items():
        if key in required_fields:
            split_json_value = value.strip().lower().split()
            for word in split_json_value:
                if word in lower_keywords:
                    keyword_callback(key, word)
    return json.dumps(json_doc)
