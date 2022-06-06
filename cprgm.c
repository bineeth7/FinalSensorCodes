#include<stdio.h>
#include<stdlib.h>
#include<shunyaInterfaces.h>
#include<pcf8591.h>

int main(){
        int x,y,z;
        /*Initialize Shunya Interfaces library*/
        shunyaInterfacesSetup();
        pcf8591Setup();    
        while (1)
        {
                x = pcf8591Read(A1);
                y = pcf8591Read(A2);
                z = pcf8591Read(A3);
                
                printf("---------------------\n\n");
                printf( "x-axis=%d \n"
                        "y-axis=%d \n"
                        "z-axis=%d \n",x,y,z);
                printf("---------------------\n\n");
                
                delay (500);
        }
        return 0;       
}
