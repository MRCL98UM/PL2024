import re
def cabecalho(texto):
    regex = r"# (.*?)\n"
    modified_string = re.sub(regex, r"<h1>\1</h1>", texto)

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
    regex = r"\*(.*?)\*"
    modified_text = re.sub(regex, r"<i>\1</i>", texto)
    return modified_text
def lista(texto):
    regex = r"\* (.*?)\n"
    modified_text = re.sub(regex, r"<li>\1</li>", texto)
    return modified_text

def link(texto):
    regex = r"\[(.*?)\]\((.*?)\)"
    modified_text = re.sub(regex, r"<a href='\2'>\1</a>", texto)
    return modified_text

def imagem(texto):
    regex = r"!\[(.*?)\]\((.*?)\)"
    modified_text = re.sub(regex, r"<img src='\2' alt='\1'>", texto)
    return modified_text
def main ():
   texto= ("# Título"
           " **negrito**"
           " *itálico*"
           "Isso é um exemplo de texto com elementos diferentes:\n"
           "1. Item 1\n"
           "2. Item 2\n"
           "3. Item 3\n"
           "Links são importantes, [veja aqui](https://www.example.com).\n"
           "E também temos uma imagem: ![imagem](https://www.example.com/image.jpg)")

   texto = cabecalho(texto)
   texto = bold(texto)
   texto = italic(texto)
   texto = lista(texto)
   texto = link(texto)
   texto = imagem(texto)
   print(texto)


if __name__ == "__main__":
    main()