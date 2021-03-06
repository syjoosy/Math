import matplotlib.pyplot as plt

matrix = [
            [
                [41.3, 89.6, 12.6, 23.2, 10.7, 13.8],
                [42.1, 90.5, 12.6, 19.5, 9.8, 12.8],
                [38.3, 85.1, 11.5, 20.7, 9.4, 14.0],
                [38.6, 85.1, 12.0, 23.2, 9.1, 13.3],
                [39.2, 89.2, 8.7, 23.5, 11.6, 13.7]
            ],
            [
                [42.3, 88.3, 11.0, 24.3, 10.7, 15.2],
                [42.6, 90.5, 10.3, 23.3, 10.2, 15.7],
                [40.7, 88.4, 10.0, 23.3, 10.7, 15.8],
                [39.3, 87.4, 8.9, 22.6, 11.4, 15.2],
                [35.1, 84.8, 7.8, 24.7, 10.7, 13.7]
            ],
            [
                [43.3, 90.9, 13.8, 24.7, 9.5, 15.1],
                [43.4, 91.1, 13.5, 23.2, 9.3, 13.9],
                [39.7, 83.0, 8.8, 23.4, 8.4, 13.8],
                [38.8, 81.9, 8.8, 22.4, 8.8, 14.0],
                [38.4, 82.2, 5.4, 22.7, 10.5,15.2]
            ],
            [
                [40.8, 90.4, 15.6, 26.1, 9.8, 14.7],
                [32.2, 87.4, 16.1, 24.4, 10.2, 13.3],
                [38.7, 84.2, 15.3, 25.1, 9.0, 13.8],
                [40.3, 87.2, 14.4, 26.5, 10.9, 15.1],
                [37.7, 83.5, 10.7, 29.4, 11.3, 15.9]
            ],
            [
                [40.2, 87.9, 13.8, 23.2, 9.5, 14.8],
                [42.2, 89.1, 12.4, 22.0, 9.6, 14.0],
                [41.3, 87.4, 11.8, 21.8, 9.8, 13.4],
                [39.2, 84.4, 8.8, 24.7, 10.6, 12.7],
                [36.7, 81.3, 8.6, 26.7, 10.2, 13.1]
            ]
        ]

def eFG(yr):
    res_eFG = (yr[0] + 0.5 * yr[2])/yr[1]
    # print('eFG = ', res_eFG)
    return(res_eFG)

def poss(yr):
    res_Poss = (0.96 * (yr[1] - yr[4] + yr[5] + (0.44 * yr[3])))
    # print('poss = ', res_Poss)
    return(res_Poss)

i = 0
yr = []
x = []
y = []
name = 0
teams_name = ["BostonCeltics" , "Los Angeles Lakers" , "Milwaukee Bucks" , "Houston Rockets" , "Toronto Raptors"]
for komanda in matrix:
    i += 1
    for stroka in komanda:
        for element in stroka:
            yr.append(element)

        y.append(eFG(yr))
        x.append(poss(yr))
        yr.clear()

    x.sort()
    y.sort()

    plt.figure(figsize=(9, 6))
    plt.title("Зависимость eFG(процента попадний) от Possesions(кол-во владений) Команда {}".format(teams_name[name]))  # заголовок
    name += 1
    plt.xlabel("Possesions(Темпа-владения)")
    plt.ylabel("eFG(процента попадний)")
    plt.grid(True)
    plt.plot(x, y)
    plt.show()

