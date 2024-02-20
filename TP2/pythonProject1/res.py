import re
def cabecalho(texto):
    regex = r"#"
    # Replace '#' with '<h1>'
    modified_string = re.sub(regex, "<h1>", texto)
    modified_string = modified_string + "</h1>"
    print(modified_string)
    return modified_string
def convert_to_bold(match):
    bold_text = match.group(1)
    html_bold = f"<b>{bold_text}</b>"
    return html_bold
def bold(texto):
    regex = r"\*\*(.*?)\*\*"
    modified_text = re.sub(regex, convert_to_bold, texto)
    return modified_text

def italic(texto):
    return f"<i>{texto}<"
def lista(texto):
    return texto.split()
def link(texto):
    return f"<a href='{texto}'>"
def imagem(texto):
    return f"<img src='{texto}'"
def main ():
    texto = "Este é um **exemplo** # Exemplo"
    print(cabecalho(texto))
    print(bold(texto))


if __name__ == "__main__":
    main()