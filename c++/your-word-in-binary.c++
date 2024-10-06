#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main()
{
    string a;
    cin >> a;
    
    for (int i = 0; i < int(a.size()); i++)
    {
        int b = int(a[i]);
        vector<int> c;

        // Converting character to binary and storing in vector c
        while (b > 0)
        {
            c.push_back(b % 2);
            b /= 2;
        }

        // Print the character and its binary equivalent
        cout << a[i] << " = ";

        // Print leading zeroes to make it 8-bit
        for (int j = 0; j < int(8 - c.size()); j++)
            cout << 0;

        // Print the binary digits stored in reverse order in the vector
        for (int j = c.size() - 1; j >= 0; j--)
            cout << c[j];

        // If the character is null or doesn't have binary digits, handle case of zero padding
        if (c.size() == 0) cout << "00000000";
        
        cout << "\n";
    }

    return 0;
}
