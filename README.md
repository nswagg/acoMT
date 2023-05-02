# acoMT
Particle Swarm Optimization algorithm experiment with moving/degrading target
Was initially designed to implement Ant Colony Optimization, but has been refactored for particle swarm with targets 
decaying on convergence (inversely proportional to swarm velocity). Decay rate defined as `carry_capacity` of particles
`
# defines the number of particles required to be in proximity to target for it to decay
self.particles_for_decay = self.NumParticles * (1 - self.w) if 0 < w <= 1 else self.NumParticles
`
## Demo
![demo gif](tests/test6.0.gif)

This project modifies Axel Thevenot's PSO metaheuristic from [this online article](https://towardsdatascience.com/particle-swarm-optimization-visually-explained-46289eeb2e14).
[Metaheuristic GitHub Repository](https://github.com/AxelThevenot/Particle_Swarm_Optimization)
