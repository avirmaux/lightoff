# Solve the lightsoff problem
#
# On considère un graphe G avec un interrupteur et une ampoule à chaque sommet.
# Initiallement toutes les lumières sont éteintes. Un interrupteur change
# l'étant de l'ampoule d'un sommet et de tous ses voicins.
# Comment allumer tout le graphe ? Réponse sur le plot en rouge.

def lightsoff_solve(G):
    A = matrix(GF(2), G)
    AI = A + A.parent().one()
    sol = AI.solve_left(matrix(GF(2), AI.nrows() * [1]))[0]
    return sol

def write_tikz(m, n, name_file=None):
    G = graphs.Grid2dGraph(m, n)
    sol = lightsoff_solve(G)
    if name_file is None:
        name_file = "lightsoff_solution_" + str(m) + "_" + str(n) +".tex"
    outfile = open(name_file, "w")
    infile = open("head", "r")
    outfile.write("\\begin{tikzpicture}[auto, scale=0.6]\n")
    outfile.write("\\def\\x{" + str(m-1) + "}\n")
    outfile.write("\\def\\y{" + str(n-1) + "}\n")
    for line in infile:
        outfile.write(line)

    outfile.write("% Solution\n")
    outfile.write("\\def\\clicks{\n")
    for i in range(len(sol)):
        if sol[i] == 1:
            v = G.vertices()[i]
            outfile.write(str(v[0]) + "/" + str(v[1]) + ", ")
    outfile.write("}\n")

    infile.close()
    infile = open("tail", "r")
    for line in infile:
        outfile.write(line)

    outfile.write("\\end{tikzpicture}")

    infile.close()
    outfile.close()
