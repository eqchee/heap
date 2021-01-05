# Heap Queues



## About The Project

From a set of projects, where the cost and revenue of each project is given, the algorithm has been designed to maximise profits after selecting a given number of projects. An initial capital is provided and only one project, where its cost does not exceed the available capital, can be selected each time. 

Two heap queues have been used in this algorithm:

1. costheap: Stores projects and their respective cost. This is a min heap where the project with least cost would be located at the root. 
2. profitheap: Stores shortlisted projects, where their cost is lower than the existing capital available, and their respective profits. This is a max heap, where the project with max profit would be located at the root. 

Before each selection of new project:

1. Keep popping the next cheapest project found at the root of costheap as long as the cost is lower or equal to the current capital available. 
2. Transfer the projects popped from costheap into profitheap.
3. Select the next most profitable project found at the root of profitheap and pop it. 



## Time Complexity

The time complexity of this algorithm in select function is O(nlog(n)) where n is the number of projects. Each heappop or heappush function would have a time complexity of O(log(n)). Considering the worst case where all the projects are selectable, then the heappop function would be repeatedly called on costheap which would involve at most log(n)+log(n-1)+log(n-2)+...+log(1) = log(n!) operations since the length of the costheap list decreases by 1 each time. Since log(n!) would be less than or equal to nlog(n), the time complexity of this heappop function called on costheap would be O(nlog(n)). Likewise for the heappush function called on profitheap, in the worst case scenario where all the projects are selectable, the heappush function would be repeatedly called on profitheap which would involve at most log(1)+log(2)+....+log(n) = log(n!) operations, which means a time complexity of O(nlog(n)) as well. Similarly, in the worst case scenario where k = n and all projects are selectable, the heappop function would be repeatedly called on profitheap would involve at most log(n)+log(n-1)+log(n-2)+...+log(1) = log(n!) operations, which means a time complexity of O(nlog(n)) as well. Thus, the overall time complexity for this algorithm would be O(nlog(n)).