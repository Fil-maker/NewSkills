from django.db import models


class Direction(models.Model):
    name = models.CharField("Направление", max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Направление"
        verbose_name_plural = "Направления"


class Professions(models.Model):
    name = models.CharField("Профессия", max_length=200)
    direction = models.ForeignKey(Direction, on_delete=models.CASCADE, verbose_name="Направление")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Профессиональный стандарт"
        verbose_name_plural = "Профессиональные стандарты"


class Competence(models.Model):
    name = models.CharField("Компетенция", max_length=200)
    profession = models.ManyToManyField(Professions, verbose_name="Профессии")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["id", "name"]
        verbose_name = "Компетенция"
        verbose_name_plural = "Компетенции"


class Standards(models.Model):
    name = models.CharField("Должность с hh.ru", max_length=200)
    profession = models.ManyToManyField(Professions, verbose_name="Профессии")
    competences = models.ManyToManyField(Competence, verbose_name="Компетенции")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Действие"
        verbose_name_plural = "Действия"


class Jobs(models.Model):
    name = models.CharField("Конкретика", max_length=200)
    profession = models.ManyToManyField(Professions, verbose_name="Профессии")
    standards = models.ManyToManyField(Standards, verbose_name="Действия")
    competences = models.ManyToManyField(Competence, verbose_name="Компетенции")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Конкретика"
        verbose_name_plural = "Конкретики"


class International(models.Model):
    name = models.CharField("Общепрофессиональные компетенции", max_length=200)
    profession = models.ManyToManyField(Professions, verbose_name='Профессиональные стандарты')
    standards = models.ManyToManyField(Standards, verbose_name="Действия")
    competences = models.ManyToManyField(Competence, verbose_name="Компетенции")
    jobs = models.ManyToManyField(Jobs, verbose_name="Конкретика")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Общепрофессиональная компетенция"
        verbose_name_plural = "Общепрофессиональные компетенции"
