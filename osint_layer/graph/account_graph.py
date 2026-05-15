from pyvis.network import Network
import os

def generate_account_graph(username, sherlock_data):

    net = Network(
        height="700px",
        width="100%",
        bgcolor="#0f172a",
        font_color="white",
        directed=False
    )

    net.add_node(
        username,
        label=username,
        color="#38bdf8",
        size=35
    )

    accounts = sherlock_data.get("accounts", [])

    for acc in accounts:

        platform = acc.get("platform")

        net.add_node(
            platform,
            label=platform,
            color="#22c55e",
            size=20
        )

        net.add_edge(username, platform)

    graph_folder = "static/graphs"
    os.makedirs(graph_folder, exist_ok=True)

    path = f"{graph_folder}/{username}_graph.html"

    net.write_html(path)

    print("Graph saved:", path)

    return path