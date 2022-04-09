#pragma once
class Riser
{
private:
	double length;
	double EI;

public:
	Riser();
	Riser(double length, double EI);
	double getEI();
};

