from django.db import models
from django.db.models import Q, F

GENDERS = [
    ("M", "Male"),
    ("F", "Female"),
]

RELATIONSHIP_TYPE = [
    ("father", "Father"),
    ("mother", "Mother"),
]


class Person(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200, blank=True)
    birth_date = models.DateField()
    death_date = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDERS)

    def __str__(self):
        return f"{self.first_name} {self.last_name}".strip()

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=(Q(death_date__isnull=True) | Q(death_date__gt=F("birth_date"))),
                name="death_date_is_after_birth_date",
            )
        ]


class Relationship(models.Model):
    parent = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name="children",
    )
    child = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name="parents",
    )
    type = models.CharField(max_length=20, choices=RELATIONSHIP_TYPE)

    def __str__(self):
        return f"{self.parent} is {self.child}'s {self.type}".strip()
