import re
class TextHandler:
    
    def remove_links(text):
        http_inicio = text.find('https://')
        while(http_inicio != -1):
            http_len = text[http_inicio:].find(' ')
            if(http_len < 0):
                http_len = len(text[http_inicio:])

            text = text[:http_inicio] + '__link__' + text[http_inicio + http_len:]
            http_inicio = text.find('https://')
        return text
    
    def remove_whitespaces(text):
        return re.sub('\s+', ' ', text)

    def remove_substr_from_text(text,substr):
        return text.replace(substr,' ')