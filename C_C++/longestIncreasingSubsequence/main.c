#include <stdio.h>

// Function to find the length of the longest increasing subsequence
int longestIncreasingSubsequence(int arr[], int size)
{
    int lis[size];      // Array to store the length of the longest increasing subsequence ending at each index
    int max_length = 1; // Initialize the maximum length to 1 (minimum possible length)

    // Initialize LIS values for all indexes as 1
    for (int i = 0; i < size; i++)
    {
        lis[i] = 1;
    }

    // Compute LIS values in bottom-up manner
    for (int i = 1; i < size; i++)
    {
        for (int j = 0; j < i; j++)
        {
            if (arr[i] > arr[j] && lis[i] < lis[j] + 1)
            {
                lis[i] = lis[j] + 1;
                if (lis[i] > max_length)
                {
                    max_length = lis[i]; // Update the maximum length if needed
                }
            }
        }
    }

    return max_length;
}

int main()
{
    int arr[] = {10, 22, 9, 33, 21, 50, 41, 60};
    int size = sizeof(arr) / sizeof(arr[0]);

    // Find the length of the longest increasing subsequence
    int length = longestIncreasingSubsequence(arr, size);

    // Print the result
    printf("The length of the longest increasing subsequence is: %d\n", length);

    return 0;
}
