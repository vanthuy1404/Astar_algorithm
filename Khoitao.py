# # Khai báo dữ liệu đồ thị và trọng số h
# adjacency_list = {
#     'A': [('B', 1), ('C', 3), ('D', 7)],
#     'B': [('D', 5)],
#     'C': [('D', 12)]
# }
#
# h = {
#     'A': 1,
#     'B': 1,
#     'C': 1,
#     'D': 1
# }
import networkx as nx
import matplotlib.pyplot as plt

def input_adjacency_list():
    print("=============NHÂP DANH SÁCH MA TRÂN KỀ=============")
    adjacency_list = {}

    num_nodes = int(input("Nhập số lượng đỉnh của đồ thị: "))

    # Nhập thông tin cho từng đỉnh
    for i in range(num_nodes):
        node = input(f"Nhập tên đỉnh {i+1}: ")
        adjacency_list[node] = []

        # Nhập số lượng cạnh kề
        num_edges = int(input(f"Nhập số lượng cạnh kề của đỉnh {node}: "))

        # Nhập thông tin cho từng cạnh kề
        for j in range(num_edges):
            neighbor, weight = input(f"Nhập tên đỉnh kề và trọng số của cạnh {j+1} (ví dụ: B 5): ").split()
            weight = int(weight)
            adjacency_list[node].append((neighbor, weight))

    return adjacency_list

def input_h_values():
    print('=============NHẬP giá trị h cho các đỉnh=============')
    h = {}
    num_nodes = int(input("Nhập số lượng đỉnh của đồ thị: "))

    # Nhập giá trị h cho từng đỉnh
    for i in range(num_nodes):
        node = input(f"Nhập tên đỉnh {i+1}: ")
        h_value = int(input(f"Nhập giá trị h cho đỉnh {node}: "))
        h[node] = h_value

    return h

if __name__ == "__main__":
    adjacency_list = input_adjacency_list()
    h = input_h_values()
    print(adjacency_list)
    print(h)

    # Khởi tạo đồ thị
    G = nx.DiGraph()

    # Thêm các đỉnh và cạnh vào đồ thị
    for node, neighbors in adjacency_list.items():
        for neighbor, weight in neighbors:
            G.add_edge(f"{node}({h[node]})", f"{neighbor}({h[neighbor]})", weight=weight)

    # Vẽ đồ thị
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=1000, node_color='skyblue', font_size=12, font_weight='bold')
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')

    # Hiển thị đồ thị
    plt.title("Đồ thị có trọng số g và h")
    plt.show()
