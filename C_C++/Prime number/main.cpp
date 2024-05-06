#include <iostream>
#include <vector>

// Function to find all prime numbers up to a given limit using the Sieve of Eratosthenes algorithm
std::vector<int> sieveOfEratosthenes(int limit)
{
    std::vector<bool> isPrime(limit + 1, true); // Initialize all numbers as prime
    std::vector<int> primes;                    // Vector to store prime numbers

    for (int p = 2; p * p <= limit; p++)
    {
        if (isPrime[p])
        {
            // Mark all multiples of p as non-prime
            for (int i = p * p; i <= limit; i += p)
            {
                isPrime[i] = false;
            }
        }
    }

    // Add prime numbers to the vector
    for (int p = 2; p <= limit; p++)
    {
        if (isPrime[p])
        {
            primes.push_back(p);
        }
    }

    return primes;
}

int main()
{
    int limit;
    std::cout << "Enter the limit to find prime numbers up to: ";
    std::cin >> limit;

    // Find prime numbers using the Sieve of Eratosthenes algorithm
    std::vector<int> primes = sieveOfEratosthenes(limit);

    // Print the prime numbers
    std::cout << "Prime numbers up to " << limit << " are:\n";
    for (int prime : primes)
    {
        std::cout << prime << " ";
    }
    std::cout << std::endl;

    return 0;
}
