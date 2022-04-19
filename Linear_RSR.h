#ifndef LINEAR_RSR_H
#define LINEAR_RSR_H

#include "Abstract_RSR.h"

class Linear_RSR : public Abstract_RSR
{

private:
    double EI;
public:
    Linear_RSR();
    Linear_RSR(double EI);

    double getEI(double curvature);
    double getMoment(double curvature);
};

#endif // LINEAR_RSR_H
