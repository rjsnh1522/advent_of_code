from collections import defaultdict, deque


def find_correct_order(queries, page_map, page_map_2):
    p1 = 0
    p2 = 0
    for query in queries:
        vs = [int(x) for x in query.strip().split(",")]
        ok = True
        for i, x in enumerate(vs):
            for j, y in enumerate(vs):
                if i < j and y in page_map[x]:
                    ok = False
        if ok:
            p1 += vs[len(vs) // 2]
        else:
            good = []
            Q = deque([])
            D = {v: len(page_map[v] & set(vs)) for v in vs}
            for v in vs:
                if D[v] == 0:
                    Q.append(v)
            while Q:
                x = Q.popleft()
                good.append(x)
                for y in page_map_2[x]:
                    if y in D:
                        D[y] -= 1
                        if D[y] == 0:
                            Q.append(y)
            # print(f"{vs=} {good=}")
            p2 += good[len(good)//2]
    print(p2)
    return p1


def read_input():
    left_page_number = []
    right_page_number = []
    page_map = defaultdict(set)
    page_map_2 = defaultdict(set)
    with open("input.txt") as file:
        for line in file.readlines():
            if line:
                l, r = line.strip().split("|")
                page_map[int(r)].add(int(l))
                page_map_2[int(l)].add(int(r))

    queries = []
    with open("page.txt") as file:
        for line in file.readlines():
            if line:
                queries.append(line.strip())

    ans = find_correct_order(
        queries=queries,
        page_map=page_map,
        page_map_2=page_map_2

    )
    print(ans)


if __name__ == "__main__":
    read_input()