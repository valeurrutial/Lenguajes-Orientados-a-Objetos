/******************************************************************************
Valeria Urrutia Lopez 00604582 Ing. en TI
*******************************************************************************/
#include <iostream>
#include "Pizzeria.h"
using namespace std;

int main()
{
   PedidoPizza objeto 1;
   
   objeto1.setTamanio("grande");
   objeto1.setDescripcion("Masa tradicional");
   objeto1.setIngredientes(2);
   objeto1.generarResumenPedido();
   
   cout << endl;
   cout << endl;
   
   PedidoPizza objeto 2("chica", 0, "Vegana");
   obejto2.generarResumenPedido();
   
   cout << endl;
   
   return 0;
}