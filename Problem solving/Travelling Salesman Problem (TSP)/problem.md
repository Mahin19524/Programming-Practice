Travelling Salesman Problem (TSP)
Problem Statement
The Travelling Salesman Problem (TSP) is a classic problem in computer science and optimization. Given a list of cities and the distances between each pair of cities, find the shortest possible route that visits each city exactly once and returns to the original city.

Task
Given a list of cities and the distances between each pair of cities, determine the shortest possible route that visits each city exactly once and returns to the original city.

Input Format
Number of cities,
𝑁
N.
Distance matrix of size
𝑁
×
𝑁
N×N representing the distances between each pair of cities. The distance matrix is a symmetric matrix where
𝑑
𝑖
𝑗
d
ij
​
represents the distance between city
𝑖
i and city
𝑗
j.
Constraints
2
≤
𝑁
≤
15
2≤N≤15
0
≤
Distance
≤
1000
0≤Distance≤1000 (for simplicity, assume distances are integers)
Output Format
A sequence of city indices representing the shortest route. The route should start and end at the same city.
Sample Input
Copy code
4
0 10 15 20
10 0 35 25
15 35 0 30
20 25 30 0
Sample Output
Copy code
0 1 3 2 0
Explanation
In this example, there are 4 cities, and the distance matrix represents the distances between each pair of cities. The shortest route that visits each city exactly once and returns to the original city is 0 -> 1 -> 3 -> 2 -> 0, with a total distance of 80 units.
