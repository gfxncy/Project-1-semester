import pygame, random


all_sprites = pygame.sprite.Group()
horizontal_borders = pygame.sprite.Group()
vertical_borders = pygame.sprite.Group()



class Border(pygame.sprite.Sprite):
    # строго вертикальный или строго горизонтальный отрезок

    def __init__(self, x1, y1, x2, y2, level_param_param_purum_purum):
        self.parametres = level_param_param_purum_purum
        if self.parametres.IsCorrect(x1, y1) and self.parametres.IsCorrect(x2, y2):
            super().__init__(all_sprites)
            if x1 == x2:  # вертикальная стенка
                self.add(vertical_borders)
                y2, y1 = max(y2, y1), min(y2, y1)
                self.image = pygame.Surface([self.parametres.BORDERWIDTH, y2 - y1])
                self.rect = pygame.Rect(x1, y1, self.parametres.BORDERWIDTH, y2 - y1)
                self.mask = pygame.mask.from_surface(self.image)
                if y2 - y1 != self.parametres.BORDERWIDTH - 4:
                    Border(x1 + 2, y1 + 2, x1 + self.parametres.BORDERWIDTH - 2, y1 + 2, self.parametres)
                    Border(x2 + 2, y2 - self.parametres.BORDERWIDTH - 2, x2 + self.parametres.BORDERWIDTH - 2, y2 - self.parametres.BORDERWIDTH - 2, self.parametres)
            else:  # горизонтальная стенка
                self.add(horizontal_borders)
                x2, x1 = max(x2, x1), min(x2, x1)
                self.image = pygame.Surface([x2 - x1, self.parametres.BORDERWIDTH])
                self.rect = pygame.Rect(x1, y1, x2 - x1, self.parametres.BORDERWIDTH)
                self.mask = pygame.mask.from_surface(self.image)
                if x2 - x1 != self.parametres.BORDERWIDTH - 4:
                    Border(x1 + 2, y1 + 2, x1 + 2, y1 + self.parametres.BORDERWIDTH - 2, self.parametres)
                    Border(x2 - self.parametres.BORDERWIDTH - 2, y2 + 2, x2 - self.parametres.BORDERWIDTH - 2, y2 + self.parametres.BORDERWIDTH - 2, self.parametres)


class level_param_param_purum_purum():

    def __init__(self, width, height, BORDERWIDTH, BOARDSDENSITY, N, M):
        self.width = width
        self.height = height
        self.BORDERWIDTH = BORDERWIDTH
        self.BOARDSDENSITY = BOARDSDENSITY
        self.N = N
        self.M = M

    def IsCorrect(self, x, y):
        return 0 <= x <= self.width and 0 <= y <= self.height


class level_generator():
    def __init__(self, level_param_param_purum_purum):
        self.parametres = level_param_param_purum_purum
        

    def make_perimetr(self):
        Border(5, 5, self.parametres.width - 5, 5, self.parametres)
        Border(5, self.parametres.height - 5, self.parametres.width - 5, self.parametres.height - 5, self.parametres)
        Border(5, 5, 5, self.parametres.height - 5, self.parametres)
        Border(self.parametres.width - 5, 5, self.parametres.width - 5, self.parametres.height - 5, self.parametres)


    # "двумерный" массив превращается в.... стеночки! ура!
    def generate_level(self, level):
        for i in range(len(level)):
            Border(*level[i], self.parametres)


    # выдаёт true в среднем где-то probability раз из единицы
    def decision(self, probability):
        return random.random() < probability


    # эта функция для массивов размера (M-1)x(N-1), cгегерированных в new_level(), эта фкнция создаёт связи между элементами этого массива
    # связь между элементами массива означает наличие стенки между координатами элементов этих массивов
    # на выходе фунции "двумерный" массив, каждый элемент которого показывает с какими другими элементами он связан
    def dfs(self, x, y):
        global color
        color[x][y][0] = 1
        m = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        for i in range(len(m)):
            a = x + m[i][0]
            b = y + m[i][1]
            if 0 <= a <= self.parametres.N - 2 and 0 <= b <= self.parametres.M - 2:
                if color[a][b][0] == 0:
                    if self.decision(self.parametres.BOARDSDENSITY):
                        color[x][y].append([a, b])
                        self.dfs(a, b)


    # приобразование условных размеров, в которых генерируется карта, в размер экрана
    def convert(self, x, y):
        return int(15 + (x + 1) * (self.parametres.width - 10) / self.parametres.N), int(5 + (y + 1) * (self.parametres.height - 10) / self.parametres.M)


    # делаем новый уровень
    def new_lewel(self):
        global color
        level = []

        # создаём список из пустых массивов размера (M-1)x(N-1)
        color = [[[0] for i in range( self.parametres.M - 1)] for j in range( self.parametres.N - 1)]

        # определяем с чем соединяем каждый элемент
        for i in range(len(color)):
            for j in range(len(color[i])):
                if color[i][j][0] == 0:
                    self.dfs(i, j)

        # транформиркем структуру массива color и координаты
        for i in range(len(color)):
            for j in range(len(color[i])):
                for x in range(1, len(color[i][j])):
                    a = self.convert(i, j)
                    b = self.convert(color[i][j][x][0], color[i][j][x][1])
                    level.append([a[0], a[1], b[0], b[1]])
        return level
    
    def get_borders(self):
        level = self.new_lewel()
        self.make_perimetr()
        self.generate_level(level)
        return(horizontal_borders, vertical_borders)
        for i in range(len(level)): print(level[i])
