"""
1. Спортивный результат

2. Спортивный отбор - CHOISES
    Предварительный
    1-ий
    2-ий
    3-ий
вид спорта > Этап > Спортсмены

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

STAGE = (
    #('первичный', 'первичный'), > UMO
    ('1 этап', '1 этап'),
    ('2 этап', '2 этап'),
    ('3 этап', '3 этап'),
)

class Coach(models.Model):
    name = models.CharField(max_length=150,
    verbose_name="Имя")
    surname = models.CharField(max_length=150,
    verbose_name="Фамилия")
    patronymic = models.CharField(max_length=150,
    verbose_name="Отчество")
    telephone = models.CharField(max_length=12, blank=True, null=True,
    verbose_name="Контактный номер")
    sport_type = models.ForeignKey(Sport_type, on_delete=models.CASCADE,
    verbose_name="Вид спорта")

    def __str__(self):
        return "%s %s. %s." % (self.surname, self.name[0], self.patronymic[0])

    def get_absolute_url(self, *args, **kwargs):
        return reverse('coach-detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ("surname",)
        verbose_name = "Тренер"
        verbose_name_plural = "Тренера"


class Parent(models.Model):
    name = models.CharField(max_length=150,
    verbose_name="Имя")
    surname = models.CharField(max_length=150,
    verbose_name="Фамилия")
    patronymic = models.CharField(max_length=150,
    verbose_name="Отчество")
    status = models.CharField(max_length=15, choices=PARENT_STATUS,
    verbose_name="Статус представителя")
    telephone = models.CharField(max_length=12,
    verbose_name="Контактный номер")
    email = models.EmailField(max_length=254,
    verbose_name="Электронная почта", blank=True)

    def __str__(self):
        return "%s %s %s" % (self.surname, self.name, self.patronymic)

    def get_absolute_url(self, *args, **kwargs):
        return reverse('parent-detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ("surname",)
        verbose_name = "Представитель"
        verbose_name_plural = "Представители"


# Где null=True -> то пустые данные, которых не было в исходнике
# Мед.показатели могут остаться null, а к примеру, фио остаться null не должны

class Sportsman(models.Model):
    name = models.CharField(max_length=150, blank=True, null=True,
    verbose_name="Имя")
    surname = models.CharField(max_length=150, blank=True, null=True,
    verbose_name="Фамилия")
    patronymic = models.CharField(max_length=150, blank=True, null=True,
    verbose_name="Отчество")
    date_of_birth = models.DateField(
    verbose_name="Дата рождения")
    gender = models.CharField(max_length=10, choices=GENDER, blank=True, null=True,
    verbose_name="Пол")
    location = models.TextField(blank=True, null=True,
    verbose_name="Место жительства")
    telephone = models.CharField(max_length=12, verbose_name="Контактный номер", blank=True, null=True)
    sports_facility = models.CharField(max_length=250, verbose_name="Спортивное учреждение", blank=True, null=True)
    swimming_skills = models.BooleanField(blank=True, verbose_name="Умение плавать")
    school_progress = models.CharField(max_length=4, choices=SCHOOL_PROGRESS, verbose_name="Успеваемость в школе", blank=True, null=True)
    sport_desire = models.BooleanField(blank=True, verbose_name="Желание заниматься спортом")
    coach = models.ForeignKey(Coach, on_delete=models.CASCADE, verbose_name="Тренер")
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE, verbose_name="Представитель", blank=True, null=True)
    sport_type = models.ForeignKey(Sport_type, on_delete=models.CASCADE, verbose_name="Вид спорта")
    rank = models.ForeignKey(Rank, on_delete=models.CASCADE, verbose_name='Разряд', blank=True, null=True)

    def __str__(self):
        return "%s %s %s" % (self.surname, self.name, self.patronymic)

    def get_absolute_url(self, *args, **kwargs):
        return reverse('sportsman-detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ("surname",)
        verbose_name = "Спортсмен"
        verbose_name_plural = "Спортсмены"
"""
Общая информация
    Год рождения
    пол
    Место жительства
    Контактные данные
    Вид спорта
    Стаж занятий
    разряд
    умение плавать
    успеваемость
    телосложение родителей
    желание заниматься спортом

Физическое развитие ВК = 0.7
    рост
    вес
    длинна ног
    размах рук
    обхват груди (вдох)
    обхват груди (выдох)
    экскурсия
    спирометрия
    размер стопы
    форма груди
    форма спины

Здоровье ВК = 1.5
    Перенесенные заболевания
    ЭКГ
    УЗИ
    Артериальное давление
    ЧСС
    Заключение врача

Функцион. Состоян. ВК=1.0
    Проба PWC150
    Проба Ромберга
    Проба штанге
    Проба генче

Психика ВК=1.0
    Темперамент
    Мотивация
    Умственное развитие
    Волевые качества
    Уровень притязаний

уровень физических способностей
    Быстора Бег 30м
    Взрывная Сила Прыжок сместа
    Силовая выносливость Подтягив
    Выносливост
"""

class Survey(models.Model):
    date = models.DateField(auto_now_add=False, blank=True, null=True,
    verbose_name="Дата обследования")
    stage = models.CharField(max_length=15, choices=STAGE, blank=True, null=True,
    verbose_name="Этап")
    sportsman = models.ForeignKey(Sportsman, on_delete=models.CASCADE,
    verbose_name="Спортсмен")
    weight = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True,
    verbose_name="Вес тела (кг)")
    length = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True,
    verbose_name="Длина тела(см)")
    spit_leg_length = models.PositiveIntegerField(blank=True, null=True,
    verbose_name="Длина ног от вертела(см)")
    foot_length = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True,
    verbose_name="Длина стопы (см)")
    torso_length_7 = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True,
    verbose_name="Длина туловища от 7-го шейного позвонка(см)")
    arm_span = models.PositiveIntegerField(blank=True, null=True,
    verbose_name="Размах рук(см)")
    chest_girth_inspiration = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True,
    verbose_name="Обхват грудной клетки на вдохе(см)")
    exhaling_chest = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True,
    verbose_name="Обхват грудной клетки на выдохе(см)")
    excursion_difference = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True,
    verbose_name="Экскурсия(разница)")
    spirometry_yellow = models.PositiveIntegerField(blank=True, null=True,
    verbose_name="Спирометрия(ЖЕЛ)мл")
    breath_hold_stange = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True,
    verbose_name="Проба с задер.дых.на вдохе(проба Штанге)сек")
    deadweight_dynamometry = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True,
    verbose_name="Становая динамометрия")
    dynamometry_right = models.PositiveIntegerField(blank=True, null=True,
    verbose_name="Динамометрия правой кисти(кг)")
    dynamometry_left = models.PositiveIntegerField( blank=True, null=True,
    verbose_name="Динамометрия левой кисти(кг)")
    tallow_mass = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True,
    verbose_name="% жировой массы")
    muscle_mass = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True,
    verbose_name="% мышечной массы")
    open_eyes = models.DecimalField(max_digits=4, decimal_places=1,  blank=True, null=True,
    verbose_name="Открытые глаза (фон)")
    close_eyes = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True,
    verbose_name="Закрытые глаза")
    target = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True,
    verbose_name="Мишень")##############
    kg = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True,
    verbose_name="PWC Кг мм")#
    chss = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True,
    verbose_name="PWC ЧСС")#
    arterial_pressure_f = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True,
    verbose_name="Артериальное давление(верхнее)")
    arterial_pressure_s = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True,
    verbose_name="Артериальное давление(нижнее)")
    mpc = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True,
    verbose_name="МПК мл/мин/кг")

    def __str__(self):
        return "%s %s" % (self.date, self.sportsman)

    class Meta:
        ordering = ("date",)
        verbose_name = "Обследование"
        verbose_name_plural = "Обследование"


class Primary(Survey):
    past_diseases = models.CharField(max_length=250, blank=True, null=True,
    verbose_name="Перенесенные заболевания(травмы)")#
    height_father = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True,
    verbose_name="Рост отца")#
    weight_father = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True,
    verbose_name="Вес отца")#
    body_type_father = models.CharField(max_length=10, choices=BODY_TYPE, blank=True, null=True,
    verbose_name="Тип тела отца")#
    height_mother = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True,
    verbose_name="Рост матери")#
    weight_mother = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True,
    verbose_name="Вес матери")#
    body_type_mother = models.CharField(max_length=10, choices=BODY_TYPE, blank=True, null=True,
    verbose_name="Тип тела матери")#
    chest_shape = models.CharField(max_length=15, choices=CHEST_SHAPE, blank=True, null=True,
    verbose_name="Форма грудной клетки")#
    back_shape = models.CharField(max_length=20, choices=BACK_SHAPE, blank=True, null=True,
    verbose_name="Форма спины")#
    speed = models.PositiveIntegerField(blank=True, null=True,
    verbose_name="Быстрота")#
    strength = models.PositiveIntegerField( blank=True, null=True,
    verbose_name="Сила%")#
    stamina = models.PositiveIntegerField( blank=True, null=True,
    verbose_name="Выносливость%")#
    coordination = models.PositiveIntegerField(blank=True, null=True,
    verbose_name="Координация%")#
    nervous_system_potential = models.CharField(max_length=15, choices=NERVOUS_SYSTEM_POTENTIAL, default='Средняя', blank=True, null=True,
    verbose_name="Потенциал нервной системы")# псих тест
    run_30 = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True,
    verbose_name="Бег 30м")#
    jump_place = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True,
    verbose_name="Прыжок в длину с места")#
    pull_ups = models.PositiveIntegerField(blank=True, null=True,
    verbose_name="Подтягивания на перекладине")#
    concept = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True,
    verbose_name="Концепт(техническая гребля)")#
    run_1500 = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True,
    verbose_name="Бег 1500м")#
    concept_500 = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True,
    verbose_name="Концепт 500м")#
    motivation = models.CharField(max_length=15, choices=MOTIVATION, blank=True, null=True,
    verbose_name="Мотивация к тренеровочному процессу")  # псих тест
    willed_qualities = models.CharField(max_length=15, choices=WILLED_QUALITIES, blank=True, null=True,
    verbose_name="Развитие волевых качеств")  # псих тест
    recommendations = models.ManyToManyField(Sport_type, blank=True, null=True,
    verbose_name="Рекомендации")#####

    def __str__(self):
        return "%s %s" % (self.date_of_test, self.sportsman)

    class Meta:
        ordering = ("date",)
        verbose_name = "Первичное"
        verbose_name_plural = "Первичные"


class UMO(Survey):
    rest = models.PositiveIntegerField(blank=True, null=True,
    verbose_name="ЭКГ в покое")
    load = models.PositiveIntegerField(blank=True, null=True,
    verbose_name="ЭКГ с нагрузкой")
    ultrasound_heart = models.PositiveIntegerField(blank=True, null=True,
    verbose_name="Узи сердца")
    plantometry = models.PositiveIntegerField(blank=True, null=True,
    verbose_name="Плантометрия")
    cns_functional = models.PositiveIntegerField(blank=True, null=True,
    verbose_name="Фукц.возможности ЦНС")
    cns_level = models.PositiveIntegerField(blank=True, null=True,
    verbose_name="Уров.работоспособности ЦНС")
    grv = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True,
    verbose_name="ГРВ")
    golden_ratio = models.PositiveIntegerField(blank=True, null=True,
    verbose_name="Золотое сечение(0,16-0,62)")
    voltage_index = models.PositiveIntegerField(blank=True, null=True,
    verbose_name="Индекс напряжения")
    spectral_analysis = models.PositiveIntegerField(blank=True, null=True,
    verbose_name="Спектральный анализ")
    integral_indicator = models.PositiveIntegerField(blank=True, null=True,
    verbose_name="Интегральный показатель")
    adaptive_capabilities = models.PositiveIntegerField(blank=True, null=True,
    verbose_name="Адаптационные возм.организма")
    functional_reserves = models.PositiveIntegerField(blank=True, null=True,
    verbose_name="Функциональные резервы")

    def __str__(self):
        return "%s" % self.date_of_pass

    class Meta:
        ordering = ("date",)
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
