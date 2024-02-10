
class Node:
    def __init__(self, modalidade, num_atletas):
        self.modalidade = modalidade
        self.num_atletas = num_atletas
        self.atletas = []
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, modalidade, num_atletas):
        new_node = Node(modalidade, num_atletas)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def display(self):
        current = self.head
        while current:
            print(f"Modalidade: {current.modalidade}, Número de Atletas: {current.num_atletas}")
            current = current.next

    def add_atleta(self, modalidade, id_atleta):
        if not self.head:
            self.head = Node(modalidade, 1)
            self.head.atletas.append(id_atleta)
            return

        current = self.head
        while current:
            if current.modalidade == modalidade:
                current.num_atletas += 1
                current.atletas.append(id_atleta)
                return
            if current.next is None:
                break
            current = current.next

        current.next = Node(modalidade, 1)
        current.next.atletas.append(id_atleta)

    def sort_by_modalidade(self):
        if not self.head or not self.head.next:
            return

        # Inicializar a lista ordenada com o primeiro nó
        sorted_list = LinkedList()
        sorted_list.append(self.head.modalidade, self.head.num_atletas)

        # Percorrer os nós restantes na lista vinculada original
        current = self.head.next
        while current:
            # Encontrar o local apropriado para inserir o nó na lista ordenada
            prev_sorted = None
            sorted_current = sorted_list.head
            while sorted_current and current.modalidade > sorted_current.modalidade:
                prev_sorted = sorted_current
                sorted_current = sorted_current.next

            # Inserir o nó na lista ordenada
            if prev_sorted:
                new_node = Node(current.modalidade, current.num_atletas)
                new_node.next = sorted_current
                prev_sorted.next = new_node
            else:
                sorted_list.head = Node(current.modalidade, current.num_atletas)
                sorted_list.head.next = sorted_current

            current = current.next

        # Atualizar a lista vinculada original com a lista ordenada
        self.head = sorted_list.head


def readlinecsv():
    file1 = open("emd.csv", 'r', encoding='utf-8')
    Lines = file1.readlines()
    return Lines


def main():
    # Dicionário de faixas etárias
    faixaEtaria = {}
    lines = readlinecsv()
    modalidadesSet = set()
    aptos = 0
    tamanho = len(lines) - 1
    modalidadesLinkListe = LinkedList()

    for line in lines:
        lineparts = line.split(',')
        modalidadesSet.add(lineparts[8])

        if 'true' in lineparts[12]:
            aptos += 1

        if 'idade' in lineparts[5]:
            continue
        else:
            idade = int(lineparts[5])
            etaria = idade // 5
            faixa = f"{etaria * 5}-{(etaria + 1) * 5 - 1}"
            if faixa in faixaEtaria:
                faixaEtaria[faixa].append(lineparts[0])
            else:
                faixaEtaria[faixa] = [lineparts[0]]
        modalidadesLinkListe.add_atleta(lineparts[8], lineparts[0])

    modalidadesSet = sorted(modalidadesSet)
    print("Faixas Etárias e Id's Correspondentes:")
    for faixa, ids in faixaEtaria.items():
        print(f"{faixa}: {ids}")
    print("Modalidades e numero de Pessoas a praticar:")
    modalidadesLinkListe.sort_by_modalidade()
    modalidadesLinkListe.display()
    print(modalidadesSet)
    print("numero de Pessoas que estao aptas a Praticar: ")
    print(aptos)
    print("percentagem:")
    perc = (aptos / tamanho) * 100
    print(perc)


if __name__ == "__main__":
    main()
