//Newton-Raphson Method
#include "TheProject.h" 
#include<iostream>
#include<cmath>
#include<iomanip>


double f(double x);    //declare the function for the given equation
double f(double x)    //define the function here, ie give the equation
{
    double a=std::pow(x,3.0)-x-11.0;    //write the equation whose roots are to be determined
    return a;
}
double fprime(double x);
double fprime(double x)
{
    double b=3*pow(x,2.0)-1.0;        //write the first derivative of the equation
    return b;
}
int main(int argc, char** argv)
{
    if(argc < 2) {
	std::cout << "Version " << TheProject_VERSION_MAJOR << "." << TheProject_VERSION_MINOR << std::endl;
    }

    double x,x1,e,fx,fx1;
    std::cout.precision(4);        //set the precision
    std::cout.setf(std::ios::fixed);    
    std::cout<<"Enter the initial Börje\n";    //take an intial guess
    std::cin>>x1;
    std::cout<<"Enter desired accuracy\n";    //take the desired accuracy
    std::cin>>e;
    fx=f(x);                
    fx1=fprime(x);
    std::cout <<"x{i}"<<"    "<<"x{i+1}"<<"        "<<"|x{i+1}-x{i}|"<< std::endl;                
                    
    do            
    {
        x=x1;                /*make x equal to the last calculated value of                             x1*/
        fx=f(x);            //simplifying f(x)to fx
        fx1=fprime(x);            //simplifying fprime(x) to fx1
        x1=x-(fx/fx1);            /*calculate x{1} from x, fx and fx1*/ 
        std::cout<<x<<"     "<<x1<<"           "<<std::abs(x1-x)<<std::endl;        
    }while (fabs(x1-x)>=e);            /*if |x{i+1}-x{i}| remains greater than the desired accuracy, continue the loop*/
    std::cout<<"The root of the equation is "<<x1<<std::endl;
    return 0;
}
