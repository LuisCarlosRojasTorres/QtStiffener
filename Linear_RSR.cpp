#include "Linear_RSR.h"

Linear_RSR::Linear_RSR()
{
    EI = 45000;
}

Linear_RSR::Linear_RSR(double EI)
{
    this->EI = EI;
}

double Linear_RSR::getEI(double curvature)
{
    return this->EI;
}

double Linear_RSR::getMoment(double curvature)
{
    return curvature*this->EI;
}
