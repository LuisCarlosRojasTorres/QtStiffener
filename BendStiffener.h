#pragma once
class BendStiffener
{
public:
	virtual double getEI(double x) = 0;
	virtual void toString() = 0;
};

