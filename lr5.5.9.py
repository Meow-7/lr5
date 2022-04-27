"""
Описати функцію Replace1(P, R, Q) - заміни підслова P на слово R в слові Q. Скласти
програму, яка робить в рядку пошук і заміну підслова P на слово R в слові Q до тих
пір, поки це можливо.
"""
q = "milopitamilopita"
p = "milo"
r = "tiro"


def replace1(p, r, q):
    print(q)
    q2 = q.replace(p, r)
    print(q2)


replace1(p, r, q)
