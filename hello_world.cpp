#include <iostream>

class Atmosphere
{
public:
    Atmosphere()
    {
        std::cout << "Atmosphere()" << std::endl;
    }
    ~Atmosphere()
    {
        std::cout << "~Atmosphere()" << std::endl;
    }

    double temperature_at(double altitude)
    {
        double lapse_rate = -0.0065;
        return 288.15 - lapse_rate * altitude;
    }

private:
    double temperature;
    double pressure;
    double humidity;
};

int main()
{
    printf("Hello, World!\n");
    return 0;
}