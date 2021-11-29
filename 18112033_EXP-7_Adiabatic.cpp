#include<bits/stdc++.h>
using namespace std;

 int main()
{

    float sa,sb,sc,sd,da,db,dc,dd,t,tnew,t0=298.15,t1,n1,n2,n3,n4,f,f1,h0;
    float u1=1,u2=3.5,u3=2,u4=3;

    float a1=1.648,a2=6.085,a3=5.316,a4=7.700;
    float b1=4.12e-2,b2=.3631e-2,b3=1.4285e-2,b4=.04594e-2;
    float c1=-1.530e-5,c2=-.1709e-5,c3=-.8362e-5,c4=.2521e-5;
    float d1=1.740e-9,d2=.3133e-9,d3=1.784e-9,d4=-.8587e-9;
    
    cout<<"Enter the value of n1,n2,n3,n4"<<endl;
    cin>>n1>>n2>>n3>>n4;

    cout<<"Enter the inlet temperature in deg C";
    cin>>t1;
    t1=t1+273.15;
    sa=n1*a1+n2*a2+n3*a3+n4*a4;
    sb=n1*b1+n2*b2+n3*b3+n4*b4;
    sc=n1*c1+n2*c2+n3*c3+n4*c4;
    sd=n1*d1+n2*d2+n3*d3+n4*d4;
    da=u4*a4+u3*a3-u2*a2-u1*a1;
    db=u4*b4+u3*b3-u2*b2-u1*b1;
    dc=u4*c4+u3*c3-u2*c2-u1*c1;
    dd=u4*d4+u3*d3-u2*d2-u1*d1;

    h0=(u4*(-57.7979)+u3*(-94.052)-u2*0-u1*(-20.236))*1000;
    tnew=1000;

    do{

        t=tnew;
        f=sa*(t-t1)+(sb/2)*(t*t-t1*t1)+(sc/3)*(t*t*t-t1*t1*t1)+(sd/4)*(t*t*t*t-t1*t1*t1*t1);
        f=f+h0+da*(t-t0)+(db/2)*(t*t-t0*t0)+(dc/3)*(t*t*t-t0*t0*t0)+(dd/4)*(t*t*t*t-t0*t0*t0*t0);
        f1=sa+sb*t+sc*t*t+sd*t*t*t+da+db*t+dc*t*t+dd*t*t*t;
        tnew=t-f/f1;
    }while(fabs((tnew-t)/tnew)>1e-6);
    cout<<"AFT= "<<tnew;
   
    

    return 0;
}