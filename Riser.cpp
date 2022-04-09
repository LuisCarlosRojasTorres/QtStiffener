#include "Riser.h"

Riser::Riser()
{
	this->length = 3.2;
	this->EI = 45000;
}

Riser::Riser(double length, double EI)
{
	this->length = length;
	this->EI = EI;
}

double Riser::getEI()
{
	return this->EI;
}
