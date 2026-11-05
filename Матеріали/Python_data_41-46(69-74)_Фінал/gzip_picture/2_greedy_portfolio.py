# Розглянемо інший проект, на минулих уроках ми вивчили жадібні алгоритми.
# Тому напишемо застосунок для оптимізації вибору активів з метою
# максимізації доходу або мінімізації ризику.
# Метою є створення системи, яка на основі даних
# про активи (наприклад, акції, облігації, фонди)
# визначає оптимальний портфель інвестицій,
# використовуючи жадібний підхід для кожного кроку прийняття рішень.

# Зробіть клас, який зчитує дані про активи з CSV або JSON файлу.
# Дані повинні містити інформацію про назву активу, прогнозований дохід, ризик, вартість і т.д.

# Об'єкти аналізу (активи):
# Визначаються 6 інвестиційних активів (Asset A – Asset F), кожен з яких має три ключові параметри:
# expected_return — очікуваний дохід;   risk — рівень ризику;   price — вартість активу.
# Критерій вибору (жадібна стратегія):
# Для кожного активу розраховується коефіцієнт співвідношення доходу до ризику:
# $\text{ratio} = \frac{\text{expected\_return}}{\text{risk}}$.
# Активи сортуються у порядку спадання цього коефіцієнта (від найбільш вигідного
# з точки зору дохідності на одиницю ризику до найменш вигідного):
# Asset D: $120 / 10 = \mathbf{12.0}$
# Asset E: $90 / 15 = \mathbf{6.0}$
# Asset C: $150 / 30 = \mathbf{5.0}$
# Asset F: $300 / 60 = \mathbf{5.0}$
# Asset A: $100 / 20 = \mathbf{5.0}$
# Asset B: $200 / 50 = \mathbf{4.0}$
# Обмеження та вибір:
# Програма послідовно додає активи до портфеля, доки
# загальна вартість не перевищує заданий бюджет — 200 units:
# Додається Asset D (ціна 60, витрачено 60 $\le$ 200)
# Додається Asset E (ціна 40, витрачено $60 + 40 = 100 \le 200$).
# Додається Asset C (ціна 80, витрачено $100 + 80 = 180 \le 200$).
# Наступні активи (Asset F з ціною 150, Asset A з ціною 50, Asset B з ціною 100)
# пропускаються, оскільки їхня покупка перевищить залишок бюджету (20 units).
# Результат виконання програмиПід час запуску виводиться наступне значення:
# Обрані активи (selected): [Asset D, Asset E, Asset C]
# Загальна витрачена сума (spent): 180 (60 + 40 + 80)
# Загальний очікуваний дохід (total_ret): 360 (120 + 90 + 150)


class Asset:
    def __init__(self, name, expected_return, risk, price):
        self.name = name
        self.expected_return = expected_return
        self.risk = risk
        self.price = price

    def ratio(self):
        return self.expected_return / self.risk if self.risk != 0 else float('inf')

    def __str__(self):
        return self.name


def greedy_portfolio(assets: list[Asset], budget):
    sorted_assets = sorted(assets, key=lambda asset: asset.ratio(), reverse=True)
    selected_assets = []
    total_spent = 0
    total_return = 0

    for asset in sorted_assets:
        if total_spent + asset.price <= budget:
            selected_assets.append(asset)
            total_spent += asset.price
            total_return += asset.expected_return

            print(total_spent)

    return selected_assets, total_spent, total_return


assets = [
    Asset("Asset A", expected_return=100, risk=20, price=50),
    Asset("Asset B", expected_return=200, risk=50, price=100),
    Asset("Asset C", expected_return=150, risk=30, price=80),
    Asset("Asset D", expected_return=120, risk=10, price=60),
    Asset("Asset E", expected_return=90, risk=15, price=40),
    Asset("Asset F", expected_return=300, risk=60, price=150)
]
budget = 200
selected, spent, total_ret = greedy_portfolio(assets, budget)
print(f"{selected = }\n{spent = }\n{total_ret = }")