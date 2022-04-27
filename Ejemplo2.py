#Venta:
#¿Quiero comprar?, true or false
#¿Presupuesto?. Tres opciones. ciclo if
import random

plata_posible = (500,1500,10000)
cartera_productos = {
    'producto1' : {'pan' : 500},
    'producto2' : {'bebida' : 1500},
    'producto3' : {'hierba' : 10000}
}

decision = input('¿Cual es tu decisión?: ')


def conciencia(resultado) :
    if resultado == 'Si':
        return True
    else:
        return False

    

def suerte () :
    return random.randint(1, 3)

def plata(resultado):
    if resultado == 1:
        print ('Tu cantidad de dinero es','',plata_posible[0],'.')
        return plata_posible[0]
    elif resultado > 1 and resultado < 3:
        print ('Tu cantidad de dinero es','',plata_posible[1],'.')
        return plata_posible[1]
    else:
        print ('Tu cantidad de dinero es','',plata_posible[2],'.')
        return plata_posible[2]

def main():
    bandera = conciencia(decision)
    plata_total = plata(suerte())
    
    if bandera == True:
        if plata_total == cartera_productos['producto1']['pan']:
            print ('Usted a elegido','',cartera_productos['producto1']['pan'],'.')
        elif plata_total == cartera_productos['producto2']['bebida']:
            print ('Usted a elegido','',cartera_productos['producto2']['bebida'],'.')
        elif plata_total == cartera_productos['producto3']['hierba']:
            print ('Usted a elegido','',cartera_productos['producto3']['hierba'],'.')
    else:
        print ('Que tenga un buen día!')
        exit()


if __name__ == '__name__':
    main()



#data_frame = {
#    'variable11' : [1,2,3,4,5],
#    'variable22' : [1,2,3,4,5,6]
#}

#print(data_frame['variable11'][0])