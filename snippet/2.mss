

e = ValueTracker(0.01)


plane = PolarPlane(radius_max=3).add_coordinates().shift(LEFT * 2)

graph1 = always_redraw(lambda :

ParametricFunction(lambda t : plane.polar_to_point(2*np.sin(3*t), t),

t_range=[0, e.get_value()], color=GREEN)
)


dot1 = always_redraw(lambda : Dot(fill_color=GREEN, fill_opacity=0.8).scale(0.5).move_to(graph1.get_end()))



axes = Axes(x_range=[0,4,1], x_length=4, y_range=[-3,3,1], y_length=4).shift(RIGHT * 4)

axes.add_coordinates()

graph2 = always_redraw(lambda : 

axes.plot(lambda x : 2*np.sin(3*x), x_range=[0, e.get_value()], color=GREEN))

dot2 = always_redraw(lambda : Dot(fill_color=GREEN, fill_opacity=0.8).scale(0.5).move_to(graph2.get_end()))



title = MathTex("f(\\theta) = 2sin(3\\theta)", color=GREEN).next_to(axes, UP, buff=0.2)



VG = VGroup(graph1, graph2, dot1, dot2)



self.play(LaggedStart(

Write(plane), Create(axes), Write(title), run_time=3, lag_ratio=0.5

))

self.wait(1)

self.add(VG)



self.play(e.animate.set_value(PI), run_time=4, rate_func=linear)

self.wait(2)