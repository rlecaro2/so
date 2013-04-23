import proceso as p
class Quicksort:

    def __init__(self):

        self.divisiones=0
        

    def quicksort(self, lista, inicio, fin):

        self.mitad=(int)(inicio+fin)/2
        self.temp
        if(lista[medio]<lista[inicio]):

            self.temp=lista[medio]
            lista[medio]=lista[inicio]
            lista[inico]=self.temp

        if(lista[fin]<lista[inicio]):
            self.temp=lista[fin]
            lista[fin]=lista[inicio]
            lista[inicio]=self.temp

        if(lista[fin]<lista[medio]):

            self.temp=lista[fin]
            lista[fin]=lista[medio]
            lista[medio]=self.temp
        
        self.temp=lista[medio]
        lista[medio]=lista[inicio]
        lista[inicio]=temp

        self.pivote= division(lista,inicio,fin)
        quicksort(lista,inicio, self.pivote-1)
        quicksot(lista,self.pivote+1,fin)

    def division(self,lista,inicio,hasta):
        
        self.divisiones+=1
        i=inicio
        j=hasta +1
        pivote=lista[inicio]

        while(True):

            j=j-1
            while(lista[j]>pivote):
                
                j = j-1
                if(j == inicio):
                    break

            i=i+1

            while(lista[i]<pivote):
                    i=i+1
            if(i >= j):
                    break
            temp = lista[i]
            lista[i] = lista [j]
            lista[j] = temp

        temp1= lista[inicio]
        lista[inicio]=lista[j]
        lista[j]=temp1
        return j

     
    def sort(self,lista, largo):

        self.quicksort(lista,0,largo-1)

        



            

