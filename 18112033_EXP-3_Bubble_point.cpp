#include<iostream>
#include<conio.h>
#include<math.h>
using namespace std;
int main()
{
    float p,p1sat,p2sat,p1satn,t1sat,t2sat;
    float told,tnew,x1,x2,y1,y2,z1,a1,b1,c1,a2,b2,c2;
    float f,f1;
    cout<<"\nEnter the mole fraction of component 1 : ";
    cin>>z1;
    cout<<"\nEnter the pressure in kPa : ";
    cin>>p;

    a1=14.39155;
    b1=2795.317;
    c1=230.002;
    a2=16.26205;
    b2=3799.887;
    c2=226.346;

    x1=z1;
    x2=1-z1;
    t1sat=b1/(a1-log(p))-c1;
    t2sat=b2/(a2-log(p))-c2;
    tnew=x1*t1sat+x2*t2sat;
    do
    {
        told=tnew;
        p1sat=exp(a1-b1/(told+c1));
        p2sat=exp(a2-b2/(told+c2));
        f=p-x1*p1sat-x2*p2sat;
        f1=-x1*p1sat*b1/((told+c1)*(told+c1))-x2*p2sat*b2/((told+c2)*(told+c2));
        tnew=told-f/f1;

    }
    while(fabs(tnew-told)>1e-6);
    cout<<"\nThe bubble point temperature is:"<<tnew;
    // y1=z1;
    // y2=1-z1;
    // t1sat=b1/(a1-log(p))-c1;
    // t2sat=b2/(a2-log(p))-c2;
    // tnew=y1*t1sat+y2*t2sat;
    // do
    // {
    //     told=tnew;
    //     p1sat=exp(a1-b1/(told+c1)); p2sat=exp(a2-b2/(told+c2));
    //     f=(1/p)-(y1/p1sat)-(y2/p2sat);
    //     f1=(y1*b1/((told+c1)*(told+c1)))/(p1sat)+(y2*b2/ ((told+c2)*(told+c2)))/(p2sat);
    //     tnew=told-f/f1;

    // }
    // while(fabs(tnew-told)>1e-6);
    // cout<<"\nThe dew point temperature is "<<tnew; getch();
    return 0;
}
