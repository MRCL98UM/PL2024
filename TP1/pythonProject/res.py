import sys

def readlinecsv():
    file1 = open("emd.csv",'r')
    Lines = file1.readlines()
    return Lines


def main():
    # matriz de faixa etaria
    faixaEtaria = [[]]
    lines = readlinecsv()
    modalidadesSet = set()
    aptos = 0
    tamanho = len(lines) - 1

    # Initialize faixaEtaria based on maximum possible etaria value
    max_etaria = 120 // 5  # Assuming maximum age of 120 years
    for _ in range(max_etaria):
        faixaEtaria.append([])

    for line in lines:
        lineparts = line.split(',')
        modalidadesSet.add(lineparts[8])

        if 'true' in lineparts[12]:
            aptos += 1

        if 'idade' in lineparts[5]:
            continue
        else:
            etaria = int(lineparts[5]) // 5
            faixaEtaria[etaria].append(lineparts[0])
            print(etaria)

    modalidadesSet = sorted(modalidadesSet)
    print(faixaEtaria)
    print(modalidadesSet)
    print(aptos)

    perc = (aptos / tamanho) * 100
    print(perc)


if __name__ == "__main__":
    main()

if __name__ == "__main__":
    main()