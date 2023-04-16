# CS577 (Algorithms) Assignments

These are all of the homework assignments that were assigned to me during the time I was taking this course. They're mostly different implementations of different algorithms that we've learned about in the course. Unless otherwise noted, my solutions pass all the tests given by course instructors and *should (hopefully)* fit within the runtime of the prompt.

I haven't found anything in the files that says I shouldn't be allowed to post this while completing the course, but if anyone has a problem with me posting this, just shoot me an email at max.r.rountree@gmail.com.

## Homework 1: Hello World

- Didn't include because there's nothing really to show

---

## Homework 2: Asymptotic Analysis & Graphs **(DFS)**

- **Prompt:** Implement depth-first search. Given an undirected graph with *n* nodes and *m* edges, your code should run in *O(n + m)* time.

- **Input:** First line contains integer *t*, indicating the number of instances that follow. For each instance, the first line contains an integer *n*, indicating the number of nodes in the graph. Each of the following *n* lines contains several space-separated strings, where the first string *s* represents the name of a node, and the following strings represent the names of nodes that are adjacent to node *s*. You can assume that the nodes are listed line-by-line in lexicographic order, and that the adjacent nodes of a node are listed in lexicographic order.

- **Output:** For each instance, print the names of nodes visited in depth-first traversal of the graph *with ties between nodes visiting the first node in input order*. Start your traversal with the first node in input order. The names of nodes should be space-separated, and each line should be terminated by a newline.

Sample input:

```text
2
3
A B
B A
C
9
1 2 9
2 1 6 5 3
4 6
6 2 4
5 2
3 2 7
7 3
8 9
9 1 8
```

Sample output:

```text
A B C
1 2 6 4 5 3 7 9 8
```

---

## Homework 3: Greedy Algorithms **(Interval Scheduling)**

- **Prompt:** Implement the optimal algorithm for interval scheduling. Be efficient and implement it in *O(n log n)* time, where *n* is the number of jobs.

- **Input:** Input starts with a positive integer, giving the number of instances that follow. For each instance, there will be a positive integer, giving the number of jobs. For each job, there will be a pair of positive integers *i* and *j*, where *i < j*, and *i* is the start time, and *j* is the end time.

- **Output:** Number of intervals scheduled, each output terminated by a newline.

Sample input:

```text
2
1
1 4
3
1 2
3 4
2 6
```

Sample output:

```text
1
2
```

---

## Homework 4: More Greedy **(FIF Paging)**

- **Prompt:** Implement the Furthest in future paging.

- **Input:** Input starts with a positive integer, giving the number of instances that follow. For each instance, the first line will be a positive integer, giving the number of pages in the cache. The second line of the instance will be a positive integer giving the number of page requests. The third and final line of each instance will be space-delimited positive integers which will be the request sequence.

- **Output:** Number of page faults achieved by furthest in the future paging, assuming the cache is initially empty. One output per line.

Sample input:

```text
3
2
7
1 2 3 2 3 1 2
4
12
12 3 33 14 12 20 12 3 14 33 12 20
3
20
1 2 3 4 5 1 2 3 4 5 1 2 3 4 5 1 2 3 4 5
```

Sample output:

```text
4
6
12
```

---

## Homework 5: Divide and Conquer **(Inversion Counting)**

- **Prompt:** Implement the optimal algorithm for inversion counting. Be efficient and implement it in *O(n log n)* time, where *n* is the number of elements in the ranking.

- **Input:** Input starts with a positive integer, giving the number of instances that follow. For each instance, there will be a positive integer, giving the number of elements in the ranking.

- **Output:** Number of inversions. Each output line should be terminated by a newline.

Sample input:

```text
2
5
5 4 3 2 1
4
1 5 9 8
```

Sample output:

```text
10
1
```

---

## Homework 6: Divide and Conquer 2 **(Parallel Line Intersections)**

- **Prompt:** Implement a solution to the following problem:

> Suppose you are given two sets of n points, one set *{p~1, p~2, . . . , p~n}* on the line *y = 0* and the other set *{q~1, q~2, . . . , q~n}* on the line *y = 1*. Create a set of *n* line segments by connecting each point *p~i* to the corresponding point *q~i*. Your goal is to develop an algorithm to determine how many pairs of these line segments intersect. Your algorithm should take the 2n points as input, and return the number of intersections. Using divide-and-conquer, you should be able to develop an algorithm that runs in *O(n log n)* time.

- **Input:** Input starts with a positive integer, giving the number of instances that follow. For each instance, the first line will contain the number of pairs of points (*n*). The next *n* lines each contain the location *x* of a point *q~i* on the top line. Followed by the final *n* lines of the instance containing the location *x* of the corresponding point *p~i* on the bottom line.

- **Output:** Number of inversions. Each output line should be terminated by a newline.

Sample input:

![sample input](https://i.imgur.com/D7WgfHB.png)

Sample output:

```text
4
```

---

## Homework 7: Dynamic Programming **(Weighted Interval Scheduling)**

- **Prompt:** Implement the optimal algorithm for Weighted Interval Scheduling. Be efficient and implement it in *O(n^2^)* time, where *n* is the number of jobs. The objective of the problem is to determine a schedule of non-overlapping intervals with maximum weight and to return this maximum weight. To note, endpoints are exclusive, so it's okay to include a job ending at time *t* and another job starting at time *t* in the same schedule.

- **Input:** Input starts with a positive integer, giving the number of instances that follow. For each instance, there will be a positive integer, giving the number of jobs. For each job, there will be a trio of positive integers *i*, *j*, and *k*, where *i < j*, and *i* is the start time, *j* is the end time, and *k* is the weight.

- **Output:** Return the maximum weight possible while avoiding overlap between jobs. Each output line should be terminated by a newline.

Sample input:

```text
2
1
1 4 5
3
1 2 1
3 4 2
2 6 4
```

Sample output:

```text
5
5
```

---

## Homework 8: Dynamic Programming 2 **(Knapsack)**

- **Prompt:** Implement the algorithm for the Knapsack Problem. Be efficient and implement it in *O(nW)* time, where *n* is the number of items and *W* is the capacity.

- **Input:** Input starts with a positive integer, giving the number of instances that follow. For each instance, there will be a two positive integers, representing the number of items to follow and the capacity. For each item, there will be two nonnegative integers, representing the weight and value, respectively.

- **Output:** Output the maximum possible value while taking into account the weight restriction. Each output should be terminated by a newline.

Sample input:

```text
2
1 3
4 100
3 4
1 2
3 3
2 4
```

Sample output:

```text
0
6
```

---

## Homework 9: Network Flow **(Max-Flow / Min-Cut)**

- **Prompt:** Implement the Ford-Fulkerson method for finding maximum flow in graphs with only integer edge-capacities. Be efficient and implement it in *O(mF)* time, where *m* is the number of edges in the graph and *F* is the value of the maximum flow in the graph.

- **Input:** Input starts with a positive integer, giving the number of instances that follow. For each instance, there will be a two positive integers, indicating the number of nodes *n = |V|* in the gaph and the number of edges *|E|* in the gaph. Following this, there will be *|E|* additional lines describing the edges. Each edge line consists of a number indicating the source code, a number indicating the destination node, and a capacity. The nodes are not listed separately, but are numbered *{1 ... n}*.

- **Output:** Output the maximum flow value from node 1 to node *n* in each given graph.

- I don't believe I implemented this solution in the required time, but I still passed all the tests without timing out. Next week's 'hw9_opt.py' runs about 20x faster in my testing.

Sample input:

```text
2
3 2
2 3 4
1 2 5
6 9
1 2 9
1 3 4
2 4 1
2 5 6
3 4 4
3 5 5
4 6 8
5 6 5
5 6 3
```

Sample output:

```text
4
11
```

---

## Homework 10: More Network Flow **(Bipartite Matching)**

- **Prompt:** Implement an algorithm to determine the maximum matching in a bipartite graph, and if that matching is perfect (all nodes are matched). Be efficient and use your max-flow implementation from the previous week *(spoiler: I didn't!)*.

- **Input:** Input starts with a positive integer, giving the number of instances that follow. For each instance, there will be three positive integers *m*, *n*, and *q*. Numbers *m* and *n* are the number of nodes in node set *A* and node set *B*. Number *q* is the number of edges in the bipartite graph. For each edge, there will be 2 more positive integers *i* and *j* representing an edge between node 1 <= *i* <= *m* in *A* and node 1 <= *i* <= *n* in *B*.

- **Output:** Output the size of the maximum matching, followed by a space, followed by an *N* if the matching is not perfect and a *Y* if the matching is perfect. Each output line should be terminated by a newline.

- I don't believe I implemented this solution in the required time, but I still passed all the tests without timing out. Next week's 'hw9_opt.py' runs about 20x faster in my testing.

Sample input:

```text
3
2 2 4
1 1
1 2
2 1
2 2
2 3 4
2 3
2 1
1 2
2 2
5 5 10
1 1
1 3
2 1
2 2
2 3
2 4
3 4
4 4
5 4
5 5
```

Sample output:

```text
2 Y
2 N
4 N
```
