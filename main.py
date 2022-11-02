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
    plt.pie(sizes, labels=labels, explode=explode)

    # Таблица с уточнениями, что какой цвет означает
    plt.legend(loc="lower left", bbox_to_anchor=(-0.35, -0.1))
    plt.show()


def bar_chart():
    # Количество людей использовавших это оружие
    weapon_names = ['Бейсбольная бита', 'Бензопила',
                    'Бита для Крикета', 'Монтировка',
                    'Электрогитара', 'Пожарный топор',
                    'Сковорода', 'Катана',
                    'Мачете', 'Дубинка',
                    'Клюшка для гольфа', 'Вилы',
                    'Лопата', 'Нож']
    baseball_users = df[df['Baseball_Bat_Kills'] > 0].count().loc['Baseball_Bat_Kills']
    chainsaw_users = df[df['Chainsaw_Kills'] > 0].count().loc['Chainsaw_Kills']
    cricket_users = df[df['Cricket_Bat_Kills'] > 0].count().loc['Cricket_Bat_Kills']
    crowbar_users = df[df['Crowbar_Kills'] > 0].count().loc['Crowbar_Kills']
    electric_guitar_users = df[df['Electric_Guitar_Kills'] > 0].count().loc['Electric_Guitar_Kills']
    fire_axe_users = df[df['Fire_Axe_Kills'] > 0].count().loc['Fire_Axe_Kills']
    frying_pan_users = df[df['Frying_Pan_Kills'] > 0].count().loc['Frying_Pan_Kills']
    katana_users = df[df['Katana_Kills'] > 0].count().loc['Katana_Kills']
    machete_users = df[df['Machete_Kills'] > 0].count().loc['Machete_Kills']
    tonfa_users = df[df['Tonfa_Kills'] > 0].count().loc['Tonfa_Kills']
    golf_club_users = df[df['Golf_Club_Kills'] > 0].count().loc['Golf_Club_Kills']
    pitchfork_users = df[df['Pitchfork_Kills'] > 0].count().loc['Pitchfork_Kills']
    shovel_users = df[df['Shovel_Kills'] > 0].count().loc['Shovel_Kills']
    knife_users = df[df['Knife_Kills'] > 0].count().loc['Knife_Kills']
    melee_weapon_users = [baseball_users, chainsaw_users,
                          cricket_users, crowbar_users,
                          electric_guitar_users, fire_axe_users,
                          frying_pan_users, katana_users,
                          machete_users, tonfa_users,
                          golf_club_users, pitchfork_users,
                          shovel_users, knife_users]

    # Создание графика
    fig = plt.figure(figsize=(16, 9))
    # Сетка по x
    plt.grid(color='black', axis='x')
    # Сам график
    plt.barh(weapon_names[11:14], melee_weapon_users[11:14], color="green", edgecolor='black')
    plt.barh(weapon_names[0], melee_weapon_users[0], color="blue", edgecolor='black')
    plt.barh(weapon_names[2:5], melee_weapon_users[2:5], color="blue", edgecolor='black')
    plt.barh(weapon_names[6], melee_weapon_users[6], color="blue", edgecolor='black')
    plt.barh(weapon_names[8:11], melee_weapon_users[8:11], color="blue", edgecolor='black')
    plt.barh([weapon_names[1], weapon_names[5], weapon_names[7]],
             [melee_weapon_users[1], melee_weapon_users[5], melee_weapon_users[7]],
             color='red', edgecolor='black')
    # Настройки обозначений по осям
    plt.xlabel('Количество использовавших данное оружие', fontweight='bold', fontsize=20)
    plt.ylabel('Название оружия ближнего боя', fontweight='bold', fontsize=20)
    # аннотации
    for melee in melee_weapon_users:
        plt.bar_label(melee)
    plt.show()


def scatter_plot():
    # Количество огня по своим при повышении сложности
    print('scatter plot')


def heat_map():
    # Как изменяется количество убийств оружием ближнего боя при повышении сложности
    print('heat map')


if __name__ == '__main__':
    main()
