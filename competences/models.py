from django.db import models


class Direction(models.Model):
    name = models.CharField("Направление", max_length=30)

    def __str__(self):
        return self.name


class Professions(models.Model):
    name = models.CharField("Профессия", max_length=200)
    direction = models.ForeignKey(Direction, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Competence(models.Model):
    name = models.CharField("Компетенция", max_length=200)
    profession = models.ForeignKey(Professions, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Standards(models.Model):
    name = models.CharField("Стандарт", max_length=200)
    profession = models.ForeignKey(Professions, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Jobs(models.Model):
    name = models.CharField("Конкретика", max_length=200)
    profession = models.ForeignKey(Professions, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
