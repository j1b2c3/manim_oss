my_plane = NumberPlane(x_range= [-6,6], x_length=5,
y_range= [-8,8], y_length=6)

my_plane.shift(LEFT * 2)
my_function = my_plane.plot(lambda x : 0.1*(x-5)*x*(x+5), x_range=[-6,6], color=GREEN)

area = my_plane.get_area(graph = my_function, x_range=[-5,5], color=[BLUE,YELLOW,GREEN])
area2 = my_plane.get_riemann_rectangles(graph = my_function, dx=0.1, x_range=[-5,5], color=[BLUE,YELLOW,GREEN])

T1 = Tex("get area").next_to(area, RIGHT, buff=1)
T2 = Tex("get riemann rectangles").next_to(area2, RIGHT, buff=1)
 
VG1 = VGroup(area, T1)
VG2 = VGroup(area2, T2)

label = MathTex("f(x)=0.1(x-5)x(x+5)").next_to(my_plane, UP, buff=0.4)

horiz_line = Line(start = my_plane.c2p(6, my_function.underlying_function(-4)),
end = my_plane.c2p(-6, my_function.underlying_function(-4)),
stroke_color=RED, stroke_width=3)

T3 = MathTex("f(x) = f(-4)").next_to(horiz_line, buff=0.3)
VG3 = VGroup(horiz_line, T3)

self.play(DrawBorderThenFill(my_plane))
self.wait(1)

self.play(FadeIn(my_function), Write(label), run_time=2)
self.wait(1)

self.play(FadeIn(VG1))
self.wait(3)
self.play(FadeOut(VG1))
self.wait(2) 

self.play(FadeIn(VG2))
self.wait(3)
self.play(FadeOut(T2))

self.play(Create(VG3))
self.wait(3)