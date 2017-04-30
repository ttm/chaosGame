import pylab as p, numpy as n
#############
# data structure, list of lists of positions
# meaning sets of sets of points [x,y,z], [x_n].
# Each set of attractors can be transisioned with probability p
# attractor_structure=[[[0,0][1,1],[2,2]],[[7,7],[8,8],[9,9]]] # 2 triangles
attractor_structure=[[[0,0],[1,1],[0,2]],[[7,7],[8,8],[7,9]]] # 2 triangles
# ponto inicial
p0=[4,4]

# passo
step=.5

ninteractions=1000

# probabilidade de transição entre conjuntos de attratores
prob=.5

#########
# Processamento
pts=[p0] # all points from interactions
meta_attractor=0

for i in range(ninteractions):
    roulette = n.random.random()
    outcome = prob > roulette
    meta_attractor = (meta_attractor+outcome)%len(attractor_structure)
    roulette = n.random.random() 
    intervalo01 = 1/len(attractor_structure[meta_attractor])
    attractor = int(roulette/intervalo01)
    attractor_point = attractor_structure[meta_attractor][attractor] 
    # p(n+1) = (p(n)+point)/2
    pointx = (attractor_point[0]+pts[-1][0])/2
    pointy = (attractor_point[1]+pts[-1][1])/2
    x = [i[0] for i in pts]
    y = [i[1] for i in pts]
    if len(pts[0]) == 3:
        pointz = (attractor_point[2]+pts[-1][2])/2
        pts.append([pointx, pointy, pointz])
        z = [i[2] for i in pts]
        # p.plot(x,y,z,"ro") plot 3D
    else:
        pts.append([pointx, pointy])
        p.plot(x,y,"ro")
    if i %100 == 0:
        p.savefig("aqui%d.png"%(i))
        print("aqui%05d.png"%(i))


    


