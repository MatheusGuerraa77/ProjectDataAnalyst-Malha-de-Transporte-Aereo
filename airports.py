import math
import matplotlib.pyplot as plt
import networkx as nx
from PIL import Image

# Função para calcular a distância euclidiana entre dois pontos
def calculate_distance(coord1, coord2):
    return math.sqrt((coord2[0] - coord1[0]) ** 2 + (coord2[1] - coord1[1]) ** 2)

# Aeroportos e suas coordenadas
airports_project = {
    "Seattle (SEA)": (220, 1150),
    "San Francisco (SFO)": (85, 690),
    "Las Vegas (LAS)": (325, 570),
    "Denver (DEN)": (710, 680),
}

# Definição das rotas e cálculo dos pesos (distância entre os aeroportos)
routes_project = [
    ("Seattle (SEA)", "San Francisco (SFO)"),
    ("San Francisco (SFO)", "Las Vegas (LAS)"),
    ("Las Vegas (LAS)", "Denver (DEN)"),
    ("Seattle (SEA)", "Denver (DEN)"),
]

# Criar o grafo
G_project = nx.Graph()
for airport, coord in airports_project.items():
    G_project.add_node(airport, pos=coord)

for route in routes_project:
    coord1 = airports_project[route[0]]
    coord2 = airports_project[route[1]]
    distance = calculate_distance(coord1, coord2)
    G_project.add_edge(route[0], route[1], weight=distance)

# Obter posições dos nós
pos_project = nx.get_node_attributes(G_project, "pos")

# Implementação para encontrar a rota mais curta entre todos os pares
def find_shortest_path(graph, source, target):
    path = nx.shortest_path(graph, source=source, target=target, weight="weight")
    distance = nx.shortest_path_length(graph, source=source, target=target, weight="weight")
    return path, distance

# Encontrar a rota mais curta entre todos os pares de aeroportos
shortest_overall_path = None
shortest_overall_distance = float('inf')

for source in airports_project:
    for target in airports_project:
        if source != target:
            path, distance = find_shortest_path(G_project, source, target)
            if distance < shortest_overall_distance:
                shortest_overall_distance = distance
                shortest_overall_path = path

# Carregar o mapa
image_path = "data/mapaairport.png"
map_image = Image.open(image_path)

# Plotar o grafo com a menor rota destacada
fig, ax = plt.subplots(figsize=(12, 8))
ax.imshow(map_image, extent=[0, 2000, 0, 1200], alpha=0.8)

# Desenhar o grafo completo
nx.draw_networkx_nodes(G_project, pos_project, node_size=100, node_color="red", ax=ax)
nx.draw_networkx_edges(G_project, pos_project, edge_color="blue", alpha=0.5, ax=ax)

# Destacar a menor rota entre todos os aeroportos
shortest_edges = [(shortest_overall_path[i], shortest_overall_path[i + 1]) for i in range(len(shortest_overall_path) - 1)]
nx.draw_networkx_edges(G_project, pos_project, edgelist=shortest_edges, edge_color="green", width=2, ax=ax)

# Exibir pesos das arestas (distâncias)
edge_labels = nx.get_edge_attributes(G_project, 'weight')
nx.draw_networkx_edge_labels(
    G_project, pos_project, edge_labels={k: f"{v:.1f}" for k, v in edge_labels.items()}, font_size=8, ax=ax
)

# Adicionar título com a menor rota encontrada
plt.title(
    f"Malha de Transporte Aéreo - Menor Rota: {shortest_overall_path} com distância {shortest_overall_distance:.1f}",
    fontsize=14,
)
plt.axis("off")
plt.show()
