"""
1. Спортивный результат

2. Спортивный отбор - CHOISES
    Предварительный
    1-ий
    2-ий
    3-ий

"""

from django.db import models
from .directories import *

GENDER = (
    ('М', 'М'),
    ('Ж', 'Ж'),
)

SCHOOL_PROGRESS = (
    ('Отл.', 'Отл.'),
    ('Хор.', 'Хор.'),
    ('Удов', 'Удов'),
)

PARENT_STATUS = (
    ('Родитель', 'Родитель'),
    ('Опекун', 'Опекун'),
    ('Иное', 'Иное'),
)

NERVOUS_SYSTEM_POTENTIAL = (
    ('Слабая', 'Слабая'),
    ('Средне-слабая', 'Средне-слабая'),
    ('Средняя', 'Средняя'),
    ('Средне-сильная', 'Средне-сильная'),
    ('Сильная', 'Сильная'),
)

MOTIVATION = (
    ('Низкая', 'Низкая'),
    ('Средняя', 'Средняя'),
    ('Высокая', 'Высокая'),
)

WILLED_QUALITIES = (
    ('Не развитый', 'Не развитый'),
    ('Низкий', 'Низкий'),
    ('Высокий', 'Высокий'),
)

CHEST_SHAPE = (
    ('Уплощенная', 'Уплощенная'),
    ('Цилиндрическая', 'Цилиндрическая'),
    ('Коническая', 'Коническая'),
    ('Нормальная', 'Нормальная'),
)

BACK_SHAPE = (
    ('Нормальная', 'Нормальная'),
    ('Плоская', 'Плоская'),
    ('Плоско-выгнутая', 'Плоско-выгнутая'),
    ('Сутуловатость', 'Сутуловатость'),
    ('Круглая', 'Круглая'),
    ('Кругло-вогнутая', 'Кругло-вогнутая'),
)

BODY_TYPE = (
    ('Эктоморф', 'Эктоморф'),
    ('Эндоморф', 'Эндоморф'),
    ('Мезоморф', 'Мезоморф'),
)


class Coach(models.Model):
    name = models.CharField(max_length=150, verbose_name="Имя")
    surname = models.CharField(max_length=150, verbose_name="Фамилия")
    patronymic = models.CharField(max_length=150, verbose_name="Отчество")
    telephone = models.CharField(max_length=12, verbose_name="Контактный номер")
    sport_type = models.ForeignKey(Sport_type, on_delete=models.CASCADE, verbose_name="Вид спорта")

    def __str__(self):
        return "%s %s %s" % (self.surname, self.name, self.patronymic)

    def get_absolute_url(self,*args,**kwargs):
        return reverse('coach-detail', kwargs={'pk': self.pk})
    class Meta:
        ordering = ("surname",)
        verbose_name = "Тренер"
        verbose_name_plural = "Тренера"


class Parent(models.Model):
    name = models.CharField(max_length=150, verbose_name="Имя")
    surname = models.CharField(max_length=150, verbose_name="Фамилия")
    patronymic = models.CharField(max_length=150, verbose_name="Отчество")
    status = models.CharField(max_length=15, choices=PARENT_STATUS, verbose_name="Статус представителя")
    telephone = models.CharField(max_length=12, verbose_name="Контактный номер")
    email = models.EmailField(max_length=254, blank=True, verbose_name="Электронная почта")

    def __str__(self):
        return "%s %s" % (self.id, self.surname)
    def get_absolute_url(self,*args,**kwargs):
        return reverse('parent-detail', kwargs={'pk': self.pk})
    class Meta:
        ordering = ("surname",)
        verbose_name = "Представитель"
        verbose_name_plural = "Представители"


class Sportsman(models.Model):
    name = models.CharField(max_length=150, verbose_name="Имя")
    surname = models.CharField(max_length=150, verbose_name="Фамилия")
    patronymic = models.CharField(max_length=150, verbose_name="Отчество")
    date_of_birth = models.DateField(verbose_name="Дата рождения")
    gender = models.CharField(max_length=10, choices=GENDER, verbose_name="Пол")
    location = models.TextField(verbose_name="Место жительства")
    telephone = models.CharField(max_length=12, verbose_name="Контактный номер")
    sports_facility = models.CharField(max_length=250, verbose_name="Спортивное учреждение")
    swimming_skills = models.BooleanField(blank=True, verbose_name="Умение плавать")
    school_progress = models.CharField(max_length=4, choices=SCHOOL_PROGRESS, verbose_name="Успеваемость в школе")
    sport_desire = models.BooleanField(blank=True, verbose_name="Желание заниматься спортом")
    coach = models.ForeignKey(Coach, on_delete=models.CASCADE, verbose_name="Тренер")
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE, verbose_name="Представитель")
    sport_type = models.ForeignKey(Sport_type, on_delete=models.CASCADE, verbose_name="Вид спорта")
    rank = models.ForeignKey(Rank, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Разряд')

    def __str__(self):
        return "%s %s %s" % (self.id, self.surname, self.name)
    def get_absolute_url(self,*args,**kwargs):
        return reverse('sportsman-detail', kwargs={'pk': self.pk})
    class Meta:
        ordering = ("surname",)
        verbose_name = "Спортсмен"
        verbose_name_plural = "Спортсмены"


class Survey(models.Model):
    date = models.DateField(auto_now_add=True, verbose_name="Дата обследования")
    sportsman = models.ForeignKey(Sportsman, on_delete=models.CASCADE, verbose_name="Спортсмен")
    weight = models.DecimalField(max_digits=4, decimal_places=1, verbose_name="Вес тела (кг)")
    length = models.DecimalField(max_digits=4, decimal_places=1, verbose_name="Длина тела(см)")
    spit_leg_length = models.PositiveIntegerField(verbose_name="Длина ног от вертела(см)")
    foot_length = models.DecimalField(max_digits=4, decimal_places=1, verbose_name="Длина стопы (см)",  blank=True, null=True)
    torso_length_7 = models.DecimalField(max_digits=4, decimal_places=1,
                                         verbose_name="Длина туловища от 7-го шейного позвонка(см)")
    arm_span = models.PositiveIntegerField(verbose_name="Размах рук(см)")
    chest_girth_inspiration = models.DecimalField(max_digits=4, decimal_places=1,
                                                  verbose_name="Обхват грудной клетки на вдохе(см)")
    exhaling_chest = models.DecimalField(max_digits=4, decimal_places=1,
                                         verbose_name="Обхват грудной клетки на выдохе(см)")
    excursion_difference = models.DecimalField(max_digits=4, decimal_places=1, verbose_name="Экскурсия(разница)")
    spirometry_yellow = models.PositiveIntegerField(verbose_name="Спирометрия(ЖЕЛ)мл")
    breath_hold_stange = models.DecimalField(max_digits=4, decimal_places=1,
                                             verbose_name="Проба с задер.дых.на вдохе(проба Штанге)сек")
    deadweight_dynamometry = models.DecimalField(max_digits=4, decimal_places=1, verbose_name="Становая динамометрия")
    dynamometry_right = models.PositiveIntegerField(verbose_name="Динамометрия правой кисти(кг)")
    dynamometry_left = models.PositiveIntegerField(verbose_name="Динамометрия левой кисти(кг)")
    tallow_mass = models.DecimalField(max_digits=4, decimal_places=1, verbose_name="% жировой массы")
    muscle_mass = models.DecimalField(max_digits=4, decimal_places=1, verbose_name="% мышечной массы")
    open_eyes = models.DecimalField(max_digits=4, decimal_places=1, verbose_name="Открытые глаза (фон)")
    close_eyes = models.DecimalField(max_digits=4, decimal_places=1, verbose_name="Закрытые глаза")
    target = models.DecimalField(max_digits=4, decimal_places=1, verbose_name="Мишень")
    kg = models.DecimalField(max_digits=4, decimal_places=1, verbose_name="PWC Кг мм")
    chss = models.DecimalField(max_digits=4, decimal_places=1, verbose_name="PWC ЧСС")
    arterial_pressure_f = models.DecimalField(max_digits=4, decimal_places=1,
                                              verbose_name="Артериальное давление(верхнее число)")  # Вверхнее число
    arterial_pressure_s = models.DecimalField(max_digits=4, decimal_places=1,
                                              verbose_name="Артериальное давление(нижнее число)")  # Нижнее число
    mpc = models.DecimalField(max_digits=4, decimal_places=1, verbose_name="МПК мл/мин/кг")

    def __str__(self):
        return "%s" % self.id

    class Meta:
        ordering = ("date",)
        verbose_name = "Обследование"
        verbose_name_plural = "Обследование"


class Primary(Survey):
    date_of_test = models.DateField(auto_now_add=True, verbose_name="Дата прохождения тестирования")
    # place_of_birth = models.TextField(verbose_name="Место рождения")# удалить
    # place_of_study = models.CharField(max_length=300, verbose_name="Место обучения")# удалить
    past_diseases = models.CharField(max_length=250, verbose_name="Перенесенные заболевания(травмы)")
    height_father = models.DecimalField(max_digits=4, decimal_places=1, verbose_name="Рост отца")
    weight_father = models.DecimalField(max_digits=4, decimal_places=1, verbose_name="Вес отца")
    body_type_father = models.CharField(max_length=10, choices=BODY_TYPE, verbose_name="Тип тела отца")
    height_mather = models.DecimalField(max_digits=4, decimal_places=1, verbose_name="Рост матери")
    weight_mather = models.DecimalField(max_digits=4, decimal_places=1, verbose_name="Вес матери")
    body_type_mather = models.CharField(max_length=10, choices=BODY_TYPE, verbose_name="Тип тела матери")
    chest_shape = models.CharField(max_length=15, choices=CHEST_SHAPE, verbose_name="Форма грудной клетки")
    back_shape = models.CharField(max_length=20, choices=BACK_SHAPE, verbose_name="Форма спины")
    speed = models.PositiveIntegerField(verbose_name="Быстрота")
    strength = models.PositiveIntegerField(verbose_name="Сила%")
    stamina = models.PositiveIntegerField(verbose_name="Выносливость%")
    coordination = models.PositiveIntegerField(verbose_name="Координация%")
    nervous_system_potential = models.CharField(max_length=15, choices=NERVOUS_SYSTEM_POTENTIAL,
                                                verbose_name="Потенциал нервной системы")
    run_30 = models.DecimalField(max_digits=4, decimal_places=1, verbose_name="Бег 30м")
    jump_place = models.DecimalField(max_digits=4, decimal_places=1, verbose_name="Прыжок в длину с места")
    pull_ups = models.PositiveIntegerField(verbose_name="Подтягивания на перекладине")
    concept = models.DecimalField(max_digits=4, decimal_places=2, verbose_name="Концепт(техническая гребля)")
    run_1500 = models.DecimalField(max_digits=4, decimal_places=2, verbose_name="Бег 1500м")
    concept_500 = models.DecimalField(max_digits=4, decimal_places=2, verbose_name="Концепт 500м")
    motivation = models.CharField(max_length=15, choices=MOTIVATION, verbose_name="Мотивация к тренеровочному процессу") # псих тест
    willed_qualities = models.CharField(max_length=15, choices=WILLED_QUALITIES,
                                        verbose_name="Развитие волевых качеств")# псих тест
    recommendations = models.ManyToManyField(Sport_type, verbose_name="Рекомендации")

    def __str__(self):
        return "%s" % self.date_of_test

    class Meta:
        ordering = ("date_of_test",)
        verbose_name = "Первичное"
        verbose_name_plural = "Первичные"


class UMO(Survey):
    date_of_pass = models.DateField(auto_now_add=True, verbose_name="Дата прохождения УМО")
    rest = models.PositiveIntegerField(verbose_name="ЭКГ в покое")
    load = models.PositiveIntegerField(verbose_name="ЭКГ с нагрузкой")
    ultrasound_heart = models.PositiveIntegerField(verbose_name="Узи сердца",blank=True, null=True)
    plantometry = models.PositiveIntegerField(verbose_name="Плантометрия")
    cns_functional = models.PositiveIntegerField(verbose_name="Фукц.возможности ЦНС")
    cns_level = models.PositiveIntegerField(verbose_name="Уров.работоспособности ЦНС")
    grv = models.DecimalField(max_digits=4, decimal_places=1, verbose_name="ГРВ")
    golden_ratio = models.PositiveIntegerField(verbose_name="Золотое сечение(0,16-0,62)")
    voltage_index = models.PositiveIntegerField(verbose_name="Индекс напряжения")
    spectral_analysis = models.PositiveIntegerField(verbose_name="Спектральный анализ")
    integral_indicator = models.PositiveIntegerField(verbose_name="Интегральный показатель")
    adaptive_capabilities = models.PositiveIntegerField(verbose_name="Адаптационные возм.организма")
    functional_reserves = models.PositiveIntegerField(verbose_name="Функциональные резервы")

    def __str__(self):
        return "%s" % self.date_of_pass

    class Meta:
        ordering = ("date_of_pass",)
        verbose_name = "УМО"
        verbose_name_plural = "УМО"


# class Functional_potential(Survey):
#     date_of_fp = models.DateField(auto_now_add=True, verbose_name="Дата")
#     sportsman_fp = models.ForeignKey(Sportsman, on_delete=models.CASCADE, verbose_name="Спортсмен")
#     vt = models.DecimalField(max_digits=4, decimal_places=1, verbose_name="Вт")
#     vt_kg = models.DecimalField(max_digits=4, decimal_places=2, verbose_name="Вт/кг")
#     mpk_lmin = models.DecimalField(max_digits=4, decimal_places=2, verbose_name="МПК,л/мин")
#     la_max = models.DecimalField(max_digits=4, decimal_places=1, verbose_name="La макс, ммоль/л")
#     potential = models.DecimalField(max_digits=4, decimal_places=1, verbose_name="180+120/2 град/с н (потенциал)")
#     realization = models.DecimalField(max_digits=4, decimal_places=2, verbose_name="180+120/2 град/с н./кг(реализация)")
#     speed_power_balance = models.DecimalField(max_digits=4, decimal_places=2,
#                                               verbose_name="Баланс Скорость-сила 360/30 %")
#     romberg_coefficient = models.DecimalField(max_digits=4, decimal_places=1, verbose_name="Коэффициент Ромберга")
#     average = models.DecimalField(max_digits=4, decimal_places=2, verbose_name="Средние(все)")
#     omega = models.DecimalField(max_digits=4, decimal_places=2, verbose_name="Сигма")
#
#     def __str__(self):
#         return "%s %s" % (self.id, self.date)
#
#     class Meta:
#         ordering = ("date",)
#         verbose_name = "Функциональный потенциал"
#         verbose_name_plural = "Функц. потенциал"


