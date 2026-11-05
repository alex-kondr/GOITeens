# Застосунок (консольний або простий Flask) приймає
# від користувача початкову та кінцеву точку і виводить топ-3
# найкоротші маршрути між ними — з довжиною/часом кожного.


import math
import heapq
import matplotlib.pyplot as plt

# ==========================================
# 1. СТРУКТУРА ДАНИХ ТА ГРАФ РАЙОНУ (Одеса / Центр)
# ==========================================

# База вершин: id -> {назва, широта, довгота}
vertices = {
    "v1": {"name": "Дерибасівська / Катерининська", "lat": 46.4851, "lon": 30.7388},
    "v2": {"name": "Дерибасівська / Рішельєвська", "lat": 46.4836, "lon": 30.7402},
    "v3": {"name": "Дерибасівська / Пушкінська", "lat": 46.4822, "lon": 30.7416},
    "v4": {"name": "Ланжеронівська / Катерининська", "lat": 46.4859, "lon": 30.7401},
    "v5": {"name": "Ланжеронівська / Рішельєвська", "lat": 46.4844, "lon": 30.7415},
    "v6": {"name": "Ланжеронівська / Пушкінська", "lat": 46.4829, "lon": 30.7429},
    "v7": {"name": "Грецька / Катерининська", "lat": 46.4842, "lon": 30.7373},
    "v8": {"name": "Грецька / Рішельєвська", "lat": 46.4827, "lon": 30.7387},
    "v9": {"name": "Грецька / Пушкінська", "lat": 46.4813, "lon": 30.7401},
    "v10": {"name": "Буніна / Катерининська", "lat": 46.4833, "lon": 30.7358},
    "v11": {"name": "Буніна / Рішельєвська", "lat": 46.4818, "lon": 30.7372},
    "v12": {"name": "Буніна / Пушкінська", "lat": 46.4804, "lon": 30.7386},
    "v13": {"name": "Опера та Балет", "lat": 46.4853, "lon": 30.7411},
    "v14": {"name": "Думська площа", "lat": 46.4866, "lon": 30.7436},
    "v15": {"name": "Приморський бульвар / Пушкінська", "lat": 46.4841, "lon": 30.7445},
}

# Геш-таблиця для підбору та швидкого пошуку id за назвою
name_to_id = {data["name"]: v_id for v_id, data in vertices.items()}


# ==========================================
# 2. РОЗРАХУНОК ВІДСТАНІ (Haversine Formula)
# ==========================================

def calculate_distance(lat1, lon1, lat2, lon2):
    """
    Обчислює реальну відстань у метрах між двома координатами (GPS).
    """
    R = 6371000  # Радіус Землі в метрах
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)

    a = (math.sin(delta_phi / 2.0) ** 2 +
         math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2.0) ** 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return round(R * c)  # відстань у метрах


# Автоматична побудова графа з вагами у метрах
def build_graph(edges_list):
    graph = {v_id: [] for v_id in vertices}
    for u, v in edges_list:
        dist = calculate_distance(
            vertices[u]["lat"], vertices[u]["lon"],
            vertices[v]["lat"], vertices[v]["lon"]
        )
        graph[u].append((v, dist))
        graph[v].append((u, dist))  # Двосторонній рух
    return graph


# Зв'язки між перехрестями (ребра графа)
raw_edges = [
    ("v1", "v2"), ("v2", "v3"),
    ("v4", "v5"), ("v5", "v6"),
    ("v7", "v8"), ("v8", "v9"),
    ("v10", "v11"), ("v11", "v12"),
    ("v1", "v4"), ("v4", "v13"), ("v13", "v14"),
    ("v2", "v5"), ("v5", "v13"),
    ("v3", "v6"), ("v6", "v15"),
    ("v1", "v7"), ("v7", "v10"),
    ("v2", "v8"), ("v8", "v11"),
    ("v3", "v9"), ("v9", "v12"),
    ("v14", "v15"), ("v13", "v15")
]

graph = build_graph(raw_edges)


# ==========================================
# 3. АЛГОРИТМ ДЕЙКСТРИ ТА ТОП-3 МАРШРУТИ
# ==========================================

def dijkstra(graph, start, goal, disabled_edges=None):
    """
    Класичний алгоритм Дейкстри з можливістю ігнорування тимчасово "заблокованих" ребер.
    """
    if disabled_edges is None:
        disabled_edges = set()

    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    previous = {node: None for node in graph}

    pq = [(0, start)]

    while pq:
        current_dist, u = heapq.heappop(pq)

        if current_dist > distances[u]:
            continue

        if u == goal:
            break

        for v, weight in graph[u]:
            # Пропускаємо заблоковані ребра
            if (u, v) in disabled_edges or (v, u) in disabled_edges:
                continue

            distance = current_dist + weight
            if distance < distances[v]:
                distances[v] = distance
                previous[v] = u
                heapq.heappush(pq, (distance, v))

    # Реконструкція шляху
    if distances[goal] == float('inf'):
        return None, float('inf')

    path = []
    curr = goal
    while curr is not None:
        path.append(curr)
        curr = previous[curr]
    path.reverse()

    return path, distances[goal]


def find_top_k_routes(graph, start, goal, k=3):
    """
    Знаходить k найкоротших альтернативних шляхів (варіанти за принципом Yen's algorithm / penalty).
    """
    routes = []
    disabled_edges = set()

    for _ in range(k):
        path, dist = dijkstra(graph, start, goal, disabled_edges)
        if not path or path in [r[0] for r in routes]:
            break

        routes.append((path, dist))

        # Блокуємо одне з ребер знайденого шляху для наступної ітерації,
        # щоб змусити алгоритм шукати альтернативи
        if len(path) > 1:
            # Блокуємо ребро посередині або перше відкрите
            for i in range(len(path) - 1):
                edge = (path[i], path[i+1])
                if edge not in disabled_edges:
                    disabled_edges.add(edge)
                    break

    # Сортування вибірковою вибіркою (Selection Sort) для повторення теми сортувань
    selection_sort_routes(routes)
    return routes


def selection_sort_routes(routes_list):
    """
    Сортування вибіркою (Selection Sort) за довжиною маршруту.
    """
    n = len(routes_list)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if routes_list[j][1] < routes_list[min_idx][1]:
                min_idx = j
        routes_list[i], routes_list[min_idx] = routes_list[min_idx], routes_list[i]


# ==========================================
# 4. ІНТЕРФЕЙС ТА ПІДКАЗКИ
# ==========================================

def search_location(query):
    """
    Пошук вершин за підрядком назви.
    """
    query = query.strip().lower()
    matches = [name for name in name_to_id.keys() if query in name.lower()]
    return matches


def get_user_input(prompt_text):
    while True:
        user_in = input(prompt_text).strip()
        matches = search_location(user_in)

        if not matches:
            print("❌ Нічого не знайдено! Спробуйте ввести іншу назву.")
        elif len(matches) == 1:
            print(f"  → Обрано: {matches[0]}")
            return name_to_id[matches[0]]
        else:
            print("\nЗнайдено декілька варіантів:")
            for i, match in enumerate(matches, 1):
                print(f"  {i}. {match}")
            choice = input("Введіть номер потрібного місця (або уточніть запит): ")
            if choice.isdigit() and 1 <= int(choice) <= len(matches):
                selected_name = matches[int(choice) - 1]
                print(f"  → Обрано: {selected_name}")
                return name_to_id[selected_name]


# ==========================================
# 5. ВІЗУАЛІЗАЦІЯ (TEXT & GRAPHICS)
# ==========================================

def plot_routes(routes):
    """
    Малює схему району та наносить 3 найкоротші маршрути різними кольорами.
    """
    plt.figure(figsize=(10, 7))
    plt.title("Топ-3 альтернативні маршрути (Алгоритм Дейкстри)", fontsize=14)

    # 1. Малюємо всі ребра графа (сірим кольором)
    for u in graph:
        for v, _ in graph[u]:
            lat1, lon1 = vertices[u]["lat"], vertices[u]["lon"]
            lat2, lon2 = vertices[v]["lat"], vertices[v]["lon"]
            plt.plot([lon1, lon2], [lat1, lat2], color="gainsboro", linewidth=2, zorder=1)

    # 2. Малюємо всі вершини (точки)
    for v_id, data in vertices.items():
        plt.scatter(data["lon"], data["lat"], color="gray", s=40, zorder=2)
        plt.text(data["lon"] + 0.0001, data["lat"] + 0.0001, data["name"], fontsize=7, alpha=0.7)

    # 3. Наносимо знайдені маршрути
    colors = ["#E63946", "#1D3557", "#2A9D8F"]  # Червоний (1-й), Синій (2-й), Зелений (3-й)
    styles = ["-", "--", "-."]

    for idx, (path, dist) in enumerate(routes):
        path_lons = [vertices[node]["lon"] for node in path]
        path_lats = [vertices[node]["lat"] for node in path]

        # Розрахунок приб. часу пішки (5 км/год = ~83 м/хв)
        walk_time = round(dist / 83.3)

        label = f"Маршрут #{idx+1}: {dist} м (~{walk_time} хв)"
        plt.plot(path_lons, path_lats, color=colors[idx % len(colors)],
                 linestyle=styles[idx % len(styles)], linewidth=3.5, label=label, zorder=3 + idx)

    # Виділяємо старт і фініш
    start_id, goal_id = routes[0][0][0], routes[0][0][-1]
    plt.scatter(vertices[start_id]["lon"], vertices[start_id]["lat"], color="green", s=120, label="СТАРТ", zorder=10)
    plt.scatter(vertices[goal_id]["lon"], vertices[goal_id]["lat"], color="red", s=120, label="ФІНІШ", zorder=10)

    plt.xlabel("Довгота (Longitude)")
    plt.ylabel("Широта (Latitude)")
    plt.legend(loc="upper left")
    plt.grid(True, linestyle=":", alpha=0.6)
    plt.tight_layout()
    plt.show()


# ==========================================
# 6. ГОЛОВНА ПРОГРАМА (MAIN)
# ==========================================

def main():
    print("==================================================")
    print(" 🗺️ НАВІГАТОР МІСТА: ПОШУК ОПТИМАЛЬНИХ МАРШРУТІВ")
    print("==================================================\n")

    print("Доступні локації для орієнтиру:")
    for name in list(name_to_id.keys())[:5]:
        print(f" • {name}")
    print(" ...та інші.\n")

    start_id = get_user_input("Введіть початкову точку (наприклад, 'Буніна' або 'Катерининська'): ")
    goal_id = get_user_input("Введіть кінцеву точку (наприклад, 'Опера' або 'Думська'): ")

    if start_id == goal_id:
        print("\n⚠️ Початкова та кінцева точки збігаються!")
        return

    routes = find_top_k_routes(graph, start_id, goal_id, k=3)

    if not routes:
        print("\nНеможливо прокласти маршрут між вказаними точками.")
        return

    print("\n" + "="*50)
    print(f"📌 РЕЗУЛЬТАТИ ПОШУКУ МАРШРУТІВ")
    print("="*50)

    for i, (path, dist) in enumerate(routes, 1):
        walk_time = round(dist / 83.3)  # пішки ~5 км/год
        path_names = " ➔ ".join([vertices[node]["name"] for node in path])

        print(f"\n🟢 **Маршрут #{i}** [{dist} метрів | ~{walk_time} хв пішки]")
        print(f"   Шлях: {path_names}")

    # Візуалізація
    print("\nБудуємо графічну карту маршрутів...")
    plot_routes(routes)


if __name__ == "__main__":
    main()