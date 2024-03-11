from collections import deque
from Khoitao import input_adjacency_list, input_h_values


class Graph:
    def __init__(self, adjac_lis):
        self.adjac_lis = adjac_lis

    def get_neighbors(self, v):
        return self.adjac_lis[v]

    # Hàm heuristic, có giá trị bằng nhau cho tất cả các nút
    def h(self, H, n):
        return H[n]

    def a_star_algorithm(self, start, stop):
        # open_lst chứa các nút đã được ghé thăm nhưng chưa kiểm tra hết các đỉnh kề
        # closed_lst chứa các nút đã được ghé thăm và đã kiểm tra hết các đỉnh kề
        open_lst = set([start])
        closed_lst = set([])

        # poo chứa các khoảng cách từ start tới các nút khác
        # giá trị mặc định là + vô cùng
        poo = {}
        poo[start] = 0

        # par Phần này khởi tạo một từ điển có tên là par, được sử dụng để lưu trữ thông tin về cha của mỗi nút trong quá trình tìm kiếm A*
        par = {}
        par[start] = start

        while len(open_lst) > 0:
            n = None

            # Tìm nút có giá trị f() nhỏ nhất trong open_lst
            for v in open_lst:
                if n == None or poo[v] + self.h(H,v) < poo[n] + self.h(H,n):
                    n = v

            if n == None:
                print('Không tìm thấy đường đi!')
                return None

            # Nếu nút hiện tại là nút đích, bắt đầu lại từ đầu
            if n == stop:
                reconst_path = []

                while par[n] != n:
                    reconst_path.append(n)
                    n = par[n]

                reconst_path.append(start)

                reconst_path.reverse()

                print('Đường đi được tìm thấy: {}'.format(reconst_path))
                return reconst_path

            # Duyệt qua tất cả các nút kề của nút hiện tại
            for (m, weight) in self.get_neighbors(n):
                # Nếu nút hiện tại không nằm trong open_lst và closed_lst
                # Thêm nút vào open_lst và gán n là cha của nó
                if m not in open_lst and m not in closed_lst:
                    open_lst.add(m)
                    par[m] = n
                    poo[m] = poo[n] + weight

                # Nếu có thể đi từ nút n tới nút m nhanh hơn
                # Cập nhật par và poo
                # Nếu nút đã nằm trong closed_lst, chuyển nó sang open_lst
                else:
                    if poo[m] > poo[n] + weight:
                        poo[m] = poo[n] + weight
                        par[m] = n

                        if m in closed_lst:
                            closed_lst.remove(m)
                            open_lst.add(m)

            # Loại bỏ nút n khỏi open_lst và thêm nó vào closed_lst
            # Vì đã kiểm tra hết các đỉnh kề của nó
            open_lst.remove(n)
            closed_lst.add(n)

        print('Không tìm thấy đường đi!')
        return None


if __name__ == "__main__":
    H = input_h_values()
    adjac_lis = input_adjacency_list()
    print(adjac_lis)
    print(H)
    graph1 = Graph(adjac_lis)
    graph1.a_star_algorithm('A', 'D')
