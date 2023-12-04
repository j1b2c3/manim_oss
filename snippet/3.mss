plane = NumberPlane(x_range=[-5,5,1], x_length=8, 
y_range=[-4,4,1], y_length=6).add_coordinates()
plane.shift(RIGHT * 2)

vec1 = Line(start=plane.c2p(0, 0), end = plane.c2p(3, 2), stroke_color=YELLOW).add_tip(tip_width=0.2)
vec1_name = MathTex('\\vec{v}').next_to(vec1, RIGHT, buff=0.1).set_color(YELLOW)

vec2 = Line(start=plane.c2p(0, 0), end=plane.c2p(-2, 1), stroke_color=RED).add_tip(tip_width=0.2)
vec2_name = MathTex('\\vec{u}').next_to(vec2, LEFT, buff=0.1).set_color(RED)

vec3 = Line(start = plane.c2p(3,2),
end = plane.c2p(1,3),
stroke_color=RED).add_tip(tip_width=0.2)

vec4 = Line(start = plane.c2p(0, 0),
end   = plane.c2p(1, 3),
stroke_color=WHITE).add_tip(tip_width=0.2)
vec4_name = MathTex('\\vec{u}+\\vec{v}').next_to(vec4, LEFT, buff=0.1).set_color(WHITE)

stuff = VGroup(plane, vec1, vec1_name, vec2, vec2_name, vec3, vec4, vec4_name)
box = RoundedRectangle(height =1.5, width =1.5, corner_radius=0.1, stroke_color=PINK).to_edge(DL)

T1 = Tex('DrawBorderThenFill').to_edge(UL)
T2 = Tex('GrowFromPoint').to_edge(UL)
T3 = Tex('Transform').to_edge(UL)
T4 = Tex('LaggedStart').to_edge(UL)
T5 = Tex('FadeIn').to_edge(UL)

self.play(DrawBorderThenFill(plane), Write(T1), run_time=2)
self.wait()
self.play(Unwrite(T1))

self.play(GrowFromPoint(vec1, point=vec1.get_start()), 
Write(vec1_name),
Write(T2),
run_time=2)
self.wait()

self.play(GrowFromPoint(vec2, point=vec2.get_start()),
Write(vec2_name),
run_time=2)
self.wait()
self.play(Unwrite(T2))

self.play(Transform(vec2, vec3), 
vec2_name.animate.next_to(vec3, UP, buff=0.1), 
Write(T3), run_time=2)
self.wait()
self.play(Unwrite(T3))

self.play(LaggedStart(GrowFromPoint(vec4, point=vec4.get_start())),
Write(vec4_name),
Write(T4),
run_time=3, lag_ratio=1)
self.wait(2)
self.play(Unwrite(T4))


self.play(FadeIn(box), Write(T5))
self.wait()
self.play(Unwrite(T5))

self.play(stuff.animate.move_to(box.get_center()).set(width=1.2), run_time=3)
self.wait(3)