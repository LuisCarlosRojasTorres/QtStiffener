#pragma once
class Abstract_RSR
{
public:
    virtual double getEI(double curvature) = 0;
    virtual double getMoment(double curvature) = 0;
};

