#pragma once
#include <math.h>

class Abstract_BSF
{
/*
 * geometry in meters [m]
*/
public:
    // return the outerRadius at s position
    virtual double getRs(double s) = 0;
    virtual double getEI(double s) = 0;
	virtual void toString() = 0;
};

