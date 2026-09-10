/******************************************************************************
Valeria Urrutia Lopez 00604582 Ing. en TI
*******************************************************************************/
#include <iostream>
#include "Pizzeria.h"
using namespace std;
 
 PedidoPizza::PedidoPizza() {
     this->tamanio = "";
     this->noIngredientes = 0;
     this->descripcion = "";
     this->precioBase = 0.0;
 }
 
 PedidoPizza::PedidioPizza(string t, int i, string d) {
     this->tamanio = t;
     this->noIngredientes = i;
     this->descrpcion = d;
     
     if (t == "chica") this->precioBase = 80.00;
     if (t == "mediana") this->precioBase = 100.00;
     if (t == "grande") this->precioBase = 120.00;
     
 }
 
 string PedidoPizza::getTamanio() {
     return this->tamanio;
 }
 void PedidoPizza::setTamanio(string t) {
     this->tamanio = t;
     
     if (t == "chica") this->precioBase = 80.00;
     if (t == "mediana") this->precioBase = 100.00;
     if (t == "grande") this->precioBase = 120.00;
 }
 
 int PedidoPizza::getIngredientes() {
     return tis->noIngredientes;
 }
 void PedidoPizza::setIngredientes(int i) {
     this->noIngredientes = i;
 }
 
 string PedidoPizza::getDescripcion() {
     return this->descripcion;
 }
 void PedidoPizza::setDescripcion(string d) {
     this->descripcion = d;
 }
 
 double PedidoPizza::calcularTotal() {
     return this->precioBase + this->noIngredientes * 15;
 }
 
 void PedidoPizza::generarResumenPedido() {
     cout << "-----TICKET PIZZERIA-----";
     cout << "Pizza" << getTamanio() << " " << getDescripcion() << endl;
     cout << "Ingredientes extra" << getIngredientes() << endl;
     cout << "Precio pizza: $" << this->precioBase << endl;
     cout << "Total a pagar: $" << calcularTotal() << endl;
     cout << "-----GRACIAS POR SU COMPRA-----";
 }