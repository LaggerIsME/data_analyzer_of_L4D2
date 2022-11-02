import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('l4d2_player_stats_final.csv')


# pandas для чтения и фильтрации информации из CSV, JSON, SQL и т.д.
# matplotlib для визуализации отфильтрованных данныхa
def main():
    pie_chart()

def percent(h_n, h_all):
    result = 100 * float(h_n) / float(h_all)
    return result

def pie_chart():
    # Датафрейм[Вытащить ряды, где часов меньше 100], посчитать все колонны, вытащить колонну с часами игры

    # Количество людей, сидящих определенное количество времени в игре
    h1 = df[df['Playtime_(Hours)'] <= 100].count().loc['Playtime_(Hours)']
    h2 = df[df['Playtime_(Hours)'] <= 200].count().loc['Playtime_(Hours)']
    h3 = df[df['Playtime_(Hours)'] <= 500].count().loc['Playtime_(Hours)']
    h4 = df[df['Playtime_(Hours)'] > 500].count().loc['Playtime_(Hours)']
    # Общее количество людей
    h_all = h1 + h2 + h3 + h4

    # Процент людей, сидящих определенное количество времени в игре
    p1 = percent(h1, h_all)
    p2 = percent(h2, h_all)
    p3 = percent(h3, h_all)
    p4 = percent(h4, h_all)

    # Настройки Pie Chart

    labels = ['до 100 часов игры', 'до 200 часов игры', 'до 500 часов игры', 'от 500 часов игры']
    sizes = [p1, p2, p3, p4]
    explode = (0.1, 0, 0, 0)

    # Сама диаграмма
    plt.pie(sizes, labels=labels, explode = explode)

    # Таблица с уточнениями, что какой цвет означает
    plt.legend(loc="lower left", bbox_to_anchor=(-0.35, -0.1))
    plt.show()

def bar_chart():
    #Какое самое популярное оружие рукопашного боя в L4D2
    print("bar chart")

def scatter_plot():
    #Количество огня по своим при повышении сложности
    print('scatter plot')

def heat_map():
    #Как изменяется количество убийств оружием ближнего боя при повышении сложности
    print('heat map')
if __name__ == '__main__':
    main()

