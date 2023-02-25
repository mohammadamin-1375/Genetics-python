import random
global dimension
dimension = 5
iteration = 0
class Genetic():
    def __init__(self):
        self.population = []
        
        self.fit = []
        
        self.pool = []
        self.fit_pool = []
        
        self.length=0
        
    def fitness(self,x): 
        s = 0
        for i in range(len(x)):
            s += x[i] ** 2
        return s
    
    def crossover(self):

        for i in range( len(self.population)-1):
           
            p_cross = random.random()
            if p_cross < 0.7:
                hel = []
                for d in range(dimension):
                    hel.append( (self. population[i][d] + self.population[i+1][d] )/2 )
                
                self.pool.append(hel)        
                self.fit_pool.append(self. fitness(self.pool[self.length]) )
                self.length += 1

    def mutation(self):
        for i in range( len(self.population)-1 ):
            p_mutation = random.random()
            if p_mutation < 0.1:
                hel = []
                for d in range(dimension):
                    hel.append( ( self.population[i][d] * random.random() * 2 ))
            
                self.pool.append(hel)        
                self.fit_pool.append( self.fitness(self.pool[self.length]) )
                self.length += 1
    
    def bubble_sort(self):
        for i in range( len(self.population) ):
            for d in range( i+1, len(self.population) ):
                if self.fit[i] > self.fit[i+1]:
                    self.fit[i], self.fit[i+1] = self.fit[i+1], self.fit[i]
                    self.population[i], self.population[i+1] = self.population[i+1], self.population[i]
    def selection(self):
        n = int( len(self.population)/4 )
        for b in range(n):
            self.pool.append( self.population[b] )
            self.fit_pool.append( self.fit[b] )
    def pool_sort(self):
        for i in range( len(self.pool) ):
            for d in range( i+1, len(self.pool) ):
               if self.fit_pool[i] > self.fit_pool[i+1]:
                    self.fit_pool[i], self.fit_pool[i+1] = self.fit_pool[i+1], self.fit_pool[i]
                    self.pool[i], self.pool[i+1] = self.pool[i+1], self.pool[i]

G=Genetic()
for i in range(50):
    hel = []
    for d in range(dimension):
        hel.append( random.random()*(512/100) * -1 ** d )
    G.population.append( hel )    
    G.fit.append( G.fitness(G.population[i]) )
print("Population:\n",G.population)
print("\nFitness:\n",G.fit)

G.bubble_sort()
g_best = G.population[0]
g_best_fit = G.fit[0]

while(g_best_fit < 0.05 and iteration < 100):
    G.crossover()
    G.mutation()
    G.bubble_sort()
    G.selection()
    G.pool_sort()
    if G.fit_pool[0] < g_best_fit:
        g_best_fit = G.fit_pool[0]
        g_best = G.pool[0]
    for i in range(50):
        try:
            G.population[i] = G.pool[i]
            G.fit[i] = G.fit_pool[i]
        except IndexError:
            print("IndexError")
    iteration=iteration+1

print("\nG best:\n",g_best)
print("\nFitness G best:\n",g_best_fit)


