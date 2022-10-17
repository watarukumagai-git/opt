# 要約
## Abstruct
The traditional particle swarm optimization algorithm is fast and efficient, but it is easy to fall into a local optimum.
An improved PSO algorithm is proposed and applied in 3D path planning of UAV to solve the problem. 
Improvement methods are described as follows: combining PSO algorithm with genetic algorithm (GA), setting dynamic inertia weight, adding sigmoid function to improve the crossover and mutation probability of genetic algorithm, and changing the selection method. 
Simulation results show that the route results solved by the improved PSO algorithm are better, which is 10% higher than that of PSO, and 58.3% better than that of GA.

## 1章
- At present, as robots enter our lives, boring, repetitive work is transformed into more unmanned and intelligent work using machines instead. 
Among them, the development of UAV-related technology has brought great convenience to our lives, such as the use of UAV for plant protection operations, logistics and distribution. 
Due to the short flight duration of UAV, path planning is one of the key issues in the automatic control of UAVs.
- Path planning algorithms suitable for UAVs can be divided into two categories, one is the global path planning algorithm in the continuous domain, and the other is the local path planning algorithm in the continuous domain (1). 
Threedimensional path planning belongs to global path planning, which can be optimized by using traditional algorithms or swarm intelligence. 
Qiang Bian and others (2) used greedy search, adaptive processing of search direction and other methods to improve the A* algorithm for path planning.
Wang Yihu and others (3) introduced the chemotaxis and migration operations of the bacterial foraging algorithm (BFO) into the PSO algorithm, which effectively improved some of the defects of the PSO algorithm and improved its search ability. 
Wang Zhihui and others (4) proposed the moth to flame algorithm, which introduced a dynamic adjustment strategy, and constantly generated new individuals to avoid falling into local optimum and enhance population diversity.
Sun and others (5) proposed a high-performance bacterial foraginggenetic particle swarm hybrid algorithm to improve the computing speed and the availability of the method.Kong (6) introduced the artificial potential field method and added random pheromones to improve the ant colony algorithm to improve the problem of slow convergence and the tendency to fall into local optima.
Xie and Kong (7) proposed a high performance bacterial foraging-genetic-particle swarm hybrid algorithm to address the shortcomings of the particle swarm algorithm, improving the computational speed and capability of the algorithm and further enhancing the usability of the method.
Pan (8) designed a step-based A* algorithm that not only guarantees path planning but also optimises search time.
Particle swarm optimization algorithm is easy to fall into local optimization in the later stage, so Fu and Hu (9) mixed particle swarm optimization with longicorn beetle beard algorithm (BAS) to obtain the more reasonable path and the higher search-efficiency.
Chengyang Lu and others (10)introduced the A* idea on the basis of RRT, which enables RRT to be targeted in the search and improves the path quality.
Manh Duong Phung and Quang Phuc Ha (11) proposed a particle swarm optimization algorithm based on spherical vector (SPSO), which transforms the path planning problem into an optimization problem with UAV feasibility and safe operation requirements and constraints. 
Through the corresponding relationship between the particle position and the UAV speed, turning angle and pitch angle, the SPSO algorithm is used to find the optimal path. 
B. Abhishek (12) et al. proposed a particle swarm optimization algorithm based on harmony search algorithm, which performs exploratory search and utilization search at the same time.
In order to solve the problem of UAV path planning under unknown threats, Jong-Jin Shin and Hyochoong Bang (13) proposed an improved particle swarm optimization algorithm consisting of preprocessing steps, multi-swarm PSO algorithm and postprocessing steps.
- The paper designs a hybrid particle swarm optimization algorithm to solve the 3-dimensional path planning problem of UAV. 
Build a 3D environment model, and constructing a fitness function based on obstacles and path lengths. At the same time, the inertia weights of the particle swarm algorithm are improved. The selection operation of Genetic Algorithm (GA) is introduced, and the crossover and mutation probability models are improved. 
Finally, the proposed algorithm is simulated by MATLAB to verify the effectiveness.

## 2章

## 3章

## 4章
