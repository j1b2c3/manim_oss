from manim import *

class TreeLogo(Scene):
    def construct(self):
        # 배경 원의 색
        dark_blue = "#1B1052"
        
        # 배경 원
        background_circle = Circle(radius=2.5, color=dark_blue, fill_opacity=0.5)
        background_circle.shift(UP * 0.3)  
        self.add(background_circle)
        
        # 투명한 원(이 원의 테두리의 글자를 위치시킴)
        transparent_circle = Circle(radius=2.2, fill_opacity=0.5)
        transparent_circle.shift(UP * 0.3)
        
        # 텍스트
        EngText = Text("MYONGJI UNIVERSITY").scale(0.7)  
        EngText.set_stroke(width=0) 
        
        KorText = Text("명지대학교").scale(0.7)  
        KorText.set_stroke(width=0) 

        # 원의 둘레를 따라 텍스트 이동시키기 (시계 방향)
        anims = []
        # 영어 텍스트 추가
        for i, char_obj in enumerate(reversed(EngText)): 
            
            angle = 270 + i *11.2 
            char_obj.rotate_about_origin(angle * DEGREES, axis=OUT)
            char_obj.next_to(
                transparent_circle.point_from_proportion(i / 18 * 0.56),
                direction=IN,
                buff=-1
            )
            anims.append(Write(char_obj))
        # 한글 텍스트 추가
        for i, char_obj in enumerate(KorText):  
            
            angle = 316.8 + (i*21.6) 
            char_obj.rotate_about_origin(angle * DEGREES, axis=OUT)
            char_obj.next_to(
                transparent_circle.point_from_proportion(0.6 + i * 0.075),
                direction=IN,
                buff=-1
            )
            anims.append(Write(char_obj))

        for anim in reversed(anims):
            self.play(anim, run_time = 0.0)
        
        # 양 옆에 있는 점
        dot1 = Dot(np.array([-2.1, -0.3, 0]), color=WHITE)
        dot2 = Dot(np.array([2.1, -0.3, 0]), color=WHITE)
        self.add(dot1)
        self.add(dot2)
        
        # 나무 줄기
        triangle = Polygon(
            np.array([-0.1, -1, 0]), 
            np.array([0.1, -1, 0]),  
            np.array([0, 0.7, 0]),    
            fill_color=WHITE,
            fill_opacity=1,
            stroke_width=0,
        )
        
        self.play(Create(triangle), run_time=0.5)

        triangle2 = Polygon(
            np.array([0, 0.1, 0]), 
            np.array([0, 0, 0]),   
            np.array([0.8, 0.3, 0]),    
            fill_color=WHITE,
            fill_opacity=1,
            stroke_width=0,
        )

        self.play(Create(triangle2), run_time=0.5)

        triangle3 = Polygon(
            np.array([0, 0.1, 0]),  
            np.array([0, 0, 0]), 
            np.array([-0.8, 0.3, 0]),     
            fill_color=WHITE,
            fill_opacity=1,
            stroke_width=0,
        )
        self.play(Create(triangle3), run_time=0.5)

        # 나뭇잎
        center1 = [0, 1, 0]  
        ellipse1 = Ellipse(width=0.2, height=0.4, fill_color=WHITE, fill_opacity=1,stroke_width=0)
        ellipse1.move_to(center1)
        self.play(Create(ellipse1), run_time=0.05)

        center2 = [-0.3, 0.8, 0]
        ellipse2 = Ellipse(width=0.2, height=0.4, fill_color=WHITE, fill_opacity=1,stroke_width=0)
        ellipse2.move_to(center2)
        ellipse2.rotate(75 * DEGREES)
        self.play(Create(ellipse2), run_time=0.05)
        
        center3 = [-0.3, 0.45, 0]
        ellipse3 = Ellipse(width=0.2, height=0.4, fill_color=BLUE, fill_opacity=1,stroke_width=0)
        ellipse3.move_to(center3)
        ellipse3.rotate(140 * DEGREES)
        self.play(Create(ellipse3), run_time=0.05)
        
        center4 = [-0.6, 0.5, 0]  
        ellipse4 = Ellipse(width=0.2, height=0.4, fill_color=WHITE, fill_opacity=1,stroke_width=0)
        ellipse4.move_to(center4)
        self.play(Create(ellipse4), run_time=0.05)

        center5 = [-0.5, -0.07, 0]  
        ellipse5 = Ellipse(width=0.2, height=0.4, fill_color=WHITE, fill_opacity=1,stroke_width=0)
        ellipse5.move_to(center5)
        ellipse5.rotate(10 * DEGREES)
        self.play(Create(ellipse5), run_time=0.05)

        center6 = [-0.78, 0, 0]  
        ellipse6 = Ellipse(width=0.2, height=0.4, fill_color=BLUE, fill_opacity=1,stroke_width=0)
        ellipse6.move_to(center6)
        ellipse6.rotate(160 * DEGREES)
        self.play(Create(ellipse6), run_time=0.05)

        center7 = [0.3, -0.15, 0]  
        ellipse7 = Ellipse(width=0.2, height=0.4, fill_color=WHITE, fill_opacity=1,stroke_width=0)
        ellipse7.move_to(center7)
        ellipse7.rotate(160 * DEGREES)
        self.play(Create(ellipse7), run_time=0.05)

        center8 = [0.6, -0.1, 0]  
        ellipse8 = Ellipse(width=0.2, height=0.4, fill_color=BLUE, fill_opacity=1,stroke_width=0)
        ellipse8.move_to(center8)
        ellipse8.rotate(25 * DEGREES)
        self.play(Create(ellipse8), run_time=0.05)

        center9 = [0.85, 0, 0]  
        ellipse9 = Ellipse(width=0.2, height=0.4, fill_color=WHITE, fill_opacity=1,stroke_width=0)
        ellipse9.move_to(center9)
        ellipse9.rotate(50 * DEGREES)
        self.play(Create(ellipse9), run_time=0.05)

        center10 = [1, 0.3, 0] 
        ellipse10 = Ellipse(width=0.2, height=0.4, fill_color=BLUE, fill_opacity=1,stroke_width=0)
        ellipse10.move_to(center10)
        ellipse10.rotate(100 * DEGREES)
        self.play(Create(ellipse10), run_time=0.05)

        center11 = [-1, 0.15, 0]  
        ellipse11 = Ellipse(width=0.2, height=0.4, fill_color=WHITE, fill_opacity=1,stroke_width=0)
        ellipse11.move_to(center11)
        ellipse11.rotate(160 * DEGREES)
        self.play(Create(ellipse11), run_time=0.05)

        center12 = [-0.95, 0.52, 0]  
        ellipse12 = Ellipse(width=0.2, height=0.4, fill_color=BLUE, fill_opacity=1,stroke_width=0)
        ellipse12.move_to(center12)
        ellipse12.rotate(50 * DEGREES)
        self.play(Create(ellipse12), run_time=0.05)

        center13 = [-0.85, 0.8, 0]  
        ellipse13 = Ellipse(width=0.2, height=0.4, fill_color=WHITE, fill_opacity=1,stroke_width=0)
        ellipse13.move_to(center13)
        ellipse13.rotate(20 * DEGREES)
        self.play(Create(ellipse13), run_time=0.05)

        center14 = [-0.68, 1.08, 0]
        ellipse14 = Ellipse(width=0.2, height=0.4, fill_color=WHITE, fill_opacity=1,stroke_width=0)
        ellipse14.move_to(center14)
        ellipse14.rotate(65 * DEGREES)
        self.play(Create(ellipse14), run_time=0.05)

        center15 = [-0.4, 1.25, 0]  
        ellipse15 = Ellipse(width=0.2, height=0.4, fill_color=BLUE, fill_opacity=1,stroke_width=0)
        ellipse15.move_to(center15)
        ellipse15.rotate(20 * DEGREES)
        self.play(Create(ellipse15), run_time=0.05)

        center16 = [0.3, 0.45, 0]  
        ellipse16 = Ellipse(width=0.2, height=0.4, fill_color=WHITE, fill_opacity=1,stroke_width=0)
        ellipse16.move_to(center16)
        ellipse16.rotate(50 * DEGREES)
        self.play(Create(ellipse16), run_time=0.05)

        center17 = [0.3, 0.89, 0] 
        ellipse17 = Ellipse(width=0.2, height=0.4, fill_color=WHITE, fill_opacity=1,stroke_width=0)
        ellipse17.move_to(center17)
        ellipse17.rotate(135 * DEGREES)
        self.play(Create(ellipse17), run_time=0.05)

        center18 = [0.6, 0.58, 0] 
        ellipse18 = Ellipse(width=0.2, height=0.4, fill_color=BLUE, fill_opacity=1,stroke_width=0)
        ellipse18.move_to(center18)
        ellipse18.rotate(160 * DEGREES)
        self.play(Create(ellipse18), run_time=0.05)

        center19 = [0.88, 0.6, 0]  
        ellipse19 = Ellipse(width=0.2, height=0.4, fill_color=WHITE, fill_opacity=1,stroke_width=0)
        ellipse19.move_to(center19)
        ellipse19.rotate(170 * DEGREES)
        self.play(Create(ellipse19), run_time=0.05)

        center20 = [0.68, 1, 0]  
        ellipse20 = Ellipse(width=0.2, height=0.4, fill_color=WHITE, fill_opacity=1,stroke_width=0)
        ellipse20.move_to(center20)
        ellipse20.rotate(135 * DEGREES)
        self.play(Create(ellipse20), run_time=0.05)

        center21 = [0.3, 1.23, 0]  
        ellipse21 = Ellipse(width=0.2, height=0.4, fill_color=BLUE, fill_opacity=1,stroke_width=0)
        ellipse21.move_to(center21)
        ellipse21.rotate(135 * DEGREES)
        self.play(Create(ellipse21), run_time=0.05)

        center22 = [-0.19, 1.45, 0] 
        ellipse22 = Ellipse(width=0.2, height=0.4, fill_color=WHITE, fill_opacity=1,stroke_width=0)
        ellipse22.move_to(center22)
        ellipse22.rotate(15 * DEGREES)
        self.play(Create(ellipse22), run_time=0.05)

        center23 = [0.1, 1.45, 0]  
        ellipse23 = Ellipse(width=0.2, height=0.4, fill_color=WHITE, fill_opacity=1,stroke_width=0)
        ellipse23.move_to(center23)
        ellipse23.rotate(150 * DEGREES)
        self.play(Create(ellipse23), run_time=0.05)
        self.wait(10)