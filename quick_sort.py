class Quick_sort:

    def sort(self, sequenza):
        if len(sequenza) <=1:
            return sequenza
        else:
            # 1) scegliere pivot
            pivot = sequenza[0]
            # 2) dividere in sottoliste
            sequenza_smaller = []
            for i in sequenza:
                if i<pivot:
                    sequenza_smaller.append(i)
            sequenza_pivot = [n for n in sequenza if n==pivot]
            sequenza_bigger = [n for n in sequenza if n>pivot]
            # 3) fare il sort delle sottoliste e appendere i risultati
            return (self.sort(sequenza_smaller)+sequenza_pivot+self.sort(sequenza_bigger))


if __name__ == '__main__':
    sequenza = [3,5,1,7,8,9,12,3,4,9,7,5]
    quick_sort = Quick_sort()
    print(f"Sequenza non ordinata {sequenza}")
    print(f"Sequenza ordinata {quick_sort.sort(sequenza)}")