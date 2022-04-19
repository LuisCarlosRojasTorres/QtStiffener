#include "Conical_BSF.h"

Conical_BSF::Conical_BSF()
{
    this->length = 1.9;
    this->outerRadius1 = 0.325;
    this->outerRadius2 = 0.10;
    this->internalRadius = 0.09;
}

Conical_BSF::Conical_BSF(double length, double outerRadius1, double outerRadius2, double internalRadius)
{
    this->length = length;
    this->outerRadius1 = outerRadius1;
    this->outerRadius2 = outerRadius2;
    this->internalRadius = internalRadius;
}

double Conical_BSF::getRs(double s)
{
    return this->outerRadius2 + (this->outerRadius1-this->outerRadius2)*((this->length-s)/this->length);
}

double Conical_BSF::getEI(double s)
{
    return 0.25*M_PI*(pow(this->getRs(s),4)-pow(this->internalRadius,4));
}
