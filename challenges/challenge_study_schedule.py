def max_value(valores):
    maior_valor = (0, 0)
    for valor in valores:
        if valor[0] > maior_valor[0]:
            maior_valor = valor
    return maior_valor[0]


def study_schedule(permanence_period, target_time):
    if target_time:
        valores = []
        filtrado = []
        for period in permanence_period:
            if type(period[0]) != int or type(period[1]) != int:
                return None
            if period[0] <= target_time <= period[1]:
                filtrado.append(period)
        valores.append((len(filtrado), target_time))
        return max_value(valores)
    return None
