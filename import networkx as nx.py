import networkx as nx
import matplotlib.pyplot as plt

def draw_organizational_chart():
    G = nx.DiGraph()
    
    # Define the hierarchy
    hierarchy = {
        "Unit Direction": [
            "Administration & Finance Department", 
            "Commercial Department", 
            "Production-Maintenance Department"
        ],
        "Administration & Finance Department": [
            "IT Service", "Investment Unit", "Methods Office Service", "Modeling Service",
            "Personnel & Training Management Service", "Security Assistant", "Accounting Service",
            "Audit & Management Control", "B.E.T Service", "Purchasing Service"
        ],
        "Commercial Department": [
            "Sales Service", "Common Resources Service", "Preparation Service", "Stock Management Service"
        ],
        "Production-Maintenance Department": [
            "Manufacturing Service (CRU)", "Manufacturing Service (CUIT)", "Quality Management & Product Development",
            "Electrical Service", "Mechanical Service", "Assistance", "Litigation", "Laboratory Service"
        ]
    }
    
    # Add nodes and edges
    for parent, children in hierarchy.items():
        for child in children:
            G.add_edge(parent, child)
    
    # Define positions using Graphviz layout for better visualization
    pos = nx.nx_agraph.graphviz_layout(G, prog="dot")
    
    # Draw the graph
    plt.figure(figsize=(14, 10))
    nx.draw(G, pos, with_labels=True, node_size=4000, node_color="lightblue", edge_color="gray", 
            font_size=10, font_weight="bold", arrows=False, linewidths=1.5)
    
    # Show the plot
    plt.title("Ceram Divindus Ghazaouet Organizational Chart", fontsize=16)
    plt.show()

# Call the function
draw_organizational_chart()
