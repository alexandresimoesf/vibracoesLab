from vpython import box, helix, vector, graph, color, gcurve, cos, sin, rate

alunos = [('Alexandre Augusto Simões Filho', '2019013357'), ('WELINGTON DE SOUZA SOARES', '2018011616')]
for nome_matricula in alunos:
    print('Nome: {},\nMatrícula: {}\n'.format(*nome_matricula))
else:
    print('Git: https://github.com/alexandresimoesf/vibracoesLab')

# ___ Dados ___
m = 30  # [kg]
k = 1200  # [N/m]
print('__Parâmetros__')
print('Massa: m = %f kg' % m)
print('Constante elástica: k = %f N/m' % k)
print('#' * 10)

# ___ Frequência Natural ___
Wn = (k / m) ** 0.5  # [rad/s]
print('Frequência Natural: Wn = %f rad/s' % Wn)

base = box(pos=vector(0, 1, 0), size=vector(0.2, 3, 2), color=color.green)
apoio = box(pos=vector(6, -0.6, 0), size=vector(14, 0.2, 4), color=color.blue)
massa = box(pos=vector(12, 0, 0), velocity=vector(0, 0, 0), size=vector(2, 1, 2), massa=m, color=color.blue)
pivot = vector(0, 0, 0)
mola = helix(pos=pivot, axis=massa.pos - pivot, radius=0.4, constant=k, thickness=0.1, coils=20, color=color.red)
eq = vector(9, 0, 0)

gp, gv, ga = graph(title='<b>Posição</b>', xtitle='<i>x [m]</i>', ytitle='<sup>Tempo</sup>'), \
             graph(title='<b>Velocidade</b>', xtitle='<i>v [m/s]</i>', ytitle='<sup>Tempo</sup>'), \
             graph(title='<b>Aceleracao</b>', xtitle='<i>a [m/s^2]</i>', ytitle='<sup>Tempo</sup>')

posicao, velocidade, aceleracao = gcurve(graph=gp, color=color.cyan), \
                                  gcurve(graph=gv, color=color.green), \
                                  gcurve(graph=ga, color=color.blue)

t = 0
t_final = 10
dt = 0.01

x_0 = (massa.pos + massa.velocity * dt).mag
v_0 = (massa.velocity + ((eq - massa.pos) * (mola.constant / massa.massa)) * dt).mag

print('Deslocamento inicial: x_0 = %f m' % x_0)
print('Velocidade Inicial: v_0 = %f m/s' % v_0)

# ___ Máxima Amplitude ___
ampl_max = ((v_0 / Wn) ** 2 + (x_0) ** 2) ** 0.5
print('Amplitude Máxima: Xmáx = %f m' % ampl_max)

# ___ Velocidade Máxima ___
vel_max = (v_0 ** 2 + (x_0 * Wn) ** 2) ** 0.5
print('Velocidade Máxima: Vmáx = %f m/s' % vel_max)

while t < t_final:
    rate(100)
    acc = (eq - massa.pos) * (mola.constant / massa.massa)
    massa.velocity = massa.velocity + acc * dt
    massa.pos = massa.pos + massa.velocity * dt
    mola.axis = massa.pos - mola.pos

    # Resposta do sistema:  x(t)
    x = massa.pos.x * cos(Wn * t) + (massa.velocity.x / Wn) * sin(Wn * t)
    posicao.plot(x, t)

    # Velocidade do sistema: v(t)
    v = - massa.pos.x * Wn * sin(Wn * t) + massa.velocity.x * cos(Wn * t)
    velocidade.plot(v, t)

    # Aceleração do sistema: a(t)
    a = - massa.pos.x * Wn ** 2 * cos(Wn * t) + massa.velocity.x * Wn * -sin(Wn * t)
    aceleracao.plot(a, t)

    t = t + dt
