#pragma once
#include "Abstract_BSF.h"
class Conical_BSF :
    public Abstract_BSF
{
private:
    double length, outerRadius1, outerRadius2, internalRadius;

public:
    Conical_BSF();
    Conical_BSF(double length, double outerRadius1, double outerRadius2, double internalRadius);

    double getRs(double s);
    double getEI(double s);
};

