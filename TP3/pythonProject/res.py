#Somador on/off: criar o programa em Python
#1Pretende-se um programa que some todas as sequências de dígitos que encontre num texto;
#2Sempre que encontrar a string “Off” em qualquer combinação de maiúsculas e minúsculas, esse comportamento é desligado;
#3Sempre que encontrar a string “On” em qualquer combinação de maiúsculas e minúsculas, esse comportamento é novamente ligado;
#4Sempre que encontrar o caráter “=”, o resultado da soma é colocado na saída.
import re

def somador(texto):
    soma =0
    on = True
    lista_numeros=[]

    for line in texto:
        tokens = re.finditer(r'OFF|ON|=|[+\-]?\d+', line,re.IGNORECASE)
        for token in tokens:
            if on == True:
                if token.group().upper() == 'ON':
                    on = True
                elif token.group().upper() == 'OFF':
                    on = False
                elif token.group().upper() == '=':
                    print(soma)
                else:
                    soma = soma + int(token.group())
            elif on == False:
                if token.group().upper() == 'ON':
                    on = True
                elif token.group().upper() == 'OFF':
                    on = False
                elif token.group().upper() == '=':
                    print(soma)
                else:
                    pass


def main():
    texto = ["ON 123 456","OFF 123 456","ON 123 456","= 123 456"]
    print(texto)
    somador(texto)

if __name__ == "__main__":
    main()
