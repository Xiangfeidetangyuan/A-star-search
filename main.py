import pygame
from pygame import locals
from screen import Screen
from search import A_star, BFS
from tkinter import*


# 实现了鼠标点击选择开始、障碍、结束点
def main():
    pygame.init()
    screen = Screen()

    step = 1  
    exit = False
    pygame.display.set_caption('A* click block to set starting block')
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and step == 1:
                click_x, click_y = pygame.mouse.get_pos()
                screen.set_start(click_x, click_y)
                step = 2
                pygame.display.set_caption(
                    'click block to set obstacle blocks, press space to next step')
            elif event.type == pygame.MOUSEBUTTONDOWN and step == 2:
                click_x, click_y = pygame.mouse.get_pos()
                screen.set_obstacle(click_x, click_y)
            elif event.type == pygame.MOUSEBUTTONDOWN and step == 3:
                click_x, click_y = pygame.mouse.get_pos()
                exit = screen.set_end(click_x, click_y)
                # exit = True
            elif event.type == locals.KEYUP and event.key == locals.K_SPACE and step == 2:
                step = 3
                pygame.display.set_caption(
                    'click block to set finishing block')
            elif event.type == locals.QUIT or (event.type == locals.KEYUP and event.key == locals.K_ESCAPE):
                pygame.quit()
                sys.exit()
        screen.draw()
        pygame.display.flip()
        if exit:
            break

    pygame.display.set_caption('press space to step the search')

    search = A_star(screen)
    while True:
        for event in pygame.event.get():
            if event.type == locals.QUIT or (event.type == locals.KEYUP and event.key == locals.K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == locals.KEYUP and event.key == locals.K_SPACE and not search.over:
                search.step()

        screen.draw()
        pygame.display.flip()

# 写死了开始、障碍、结束点
def main2():
    # 初始化Tk()
    myWindow = Tk()

    myWindow.minsize(200, 250)
    myWindow.title('人工智能')

    l = Label(myWindow, text='请选择你想使用的算法', font=('Helvetica 20 bold'), width=20, height=2)
    l.grid(row=1, column=1, columnspan=2, padx=15, pady=5)
    b1 = Button(myWindow, text='A*算法', font=('Helvetica 20 bold'), width=10, height=3, command=lambda: A(myWindow))
    b1.grid(row=2, column=1, padx=0, pady=10)
    b2 = Button(myWindow, text='宽度优先算法', font=('Helvetica 20 bold'), width=10, height=3, command=lambda: B(myWindow))
    b2.grid(row=2, column=2, padx=0, pady=10)

    # 进入消息循环
    myWindow.mainloop()


def Astar1():

    pygame.init()
    screen = Screen()

    screen.set_start(126, 276)
    screen.set_obstacle(200, 191)
    screen.set_obstacle(201, 270)
    screen.set_obstacle(194, 357)
    screen.set_obstacle(195, 459)
    screen.set_obstacle(118, 363)
    screen.set_obstacle(267, 196)
    screen.set_obstacle(354, 192)
    screen.set_obstacle(432, 193)
    screen.set_obstacle(508, 194)
    screen.set_obstacle(270, 447)
    screen.set_end(272, 286)
    screen.draw()
    pygame.display.flip()
    pygame.display.set_caption(' A* ：press space to step the search')

    search = A_star(screen)  # A*搜索
    while True:
        for event in pygame.event.get():
            if event.type == locals.QUIT or (event.type == locals.KEYUP and event.key == locals.K_ESCAPE):
                pygame.quit()
                return 1
            elif event.type == locals.KEYUP and event.key == locals.K_SPACE and not search.over:
                search.step()
                screen.draw()
                pygame.display.flip()
            elif (event.type == locals.KEYUP and event.key == locals.K_SPACE) and search.over:
                search.setroad()
                screen.draw()
                pygame.display.flip()
                search.displaystep()





def BFS1():
    pygame.init()
    screen = Screen()

    screen.set_start(126, 276)
    screen.set_obstacle(200, 191)
    screen.set_obstacle(201, 270)
    screen.set_obstacle(194, 357)
    screen.set_obstacle(195, 459)
    screen.set_obstacle(118, 363)
    screen.set_obstacle(267, 196)
    screen.set_obstacle(354, 192)
    screen.set_obstacle(432, 193)
    screen.set_obstacle(508, 194)
    screen.set_obstacle(270, 447)
    screen.set_end(272, 286)
    screen.draw()
    pygame.display.flip()
    pygame.display.set_caption('BFS：press space to step the search')
    search = BFS(screen)  # BFS

    while True:
        for event in pygame.event.get():

            if event.type == locals.QUIT or ( event.type == locals.KEYUP and event.key == locals.K_ESCAPE) :
                pygame.quit()
                return 1
            elif event.type == locals.KEYUP and event.key == locals.K_SPACE and not search.over:
                search.step()
                screen.draw_BFS()
                pygame.display.flip()

            elif (event.type == locals.KEYUP and event.key == locals.K_SPACE) and search.over:
                search.setroad()
                screen.draw_BFS()
                pygame.display.flip()
                search.displaystep()

# A*算法展示界面的调用及生成
def A(myWindow):
    myWindow.withdraw()
    if (Astar1() == 1):
        myWindow.wm_deiconify()

# BFS算法展示界面的调用及生成
def B(myWindow):
    myWindow.withdraw()
    if (BFS1() == 1):
        myWindow.wm_deiconify()






if __name__ == '__main__':
    main2()
