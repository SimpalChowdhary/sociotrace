import networkx as nx
import matplotlib.pyplot as plt
import os


def generate_account_graph(username, sherlock_data):

    # Validate Sherlock output
    if not sherlock_data or sherlock_data.get("status") != "success":
        return

    accounts = sherlock_data.get("accounts", [])

    if not accounts:
        return

    # Create graph
    G = nx.Graph()

    # Central node (username)
    G.add_node(username)

    # Add platforms as nodes
    for account in accounts:
        platform = account["platform"]

        G.add_node(platform)
        G.add_edge(username, platform)

    # Graph layout
    pos = nx.spring_layout(G, seed=42)

    plt.figure(figsize=(12, 10))

    nx.draw(
        G,
        pos,
        with_labels=True,
        node_size=2500,
        node_color="skyblue",
        font_size=9,
        font_weight="bold"
    )

    # Create output folder
    os.makedirs("analysis", exist_ok=True)

    # Save graph
    file_path = f"analysis/{username}_graph.png"

    plt.title(f"Cross‑Platform Identity Graph for {username}")

    plt.savefig(file_path)

    plt.close()

    print(f"\nAccount relationship graph saved to: {file_path}")