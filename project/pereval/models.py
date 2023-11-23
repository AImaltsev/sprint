from datetime import timezone

from django.db import models


class Coords(models.Model):
    id = models.AutoField(primary_key=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    height = models.IntegerField()

    def __str__(self):
        return f"Coords {self.id}"

class PerevalImages(models.Model):
    id = models.AutoField(primary_key=True)
    date_added = models.DateTimeField(default=timezone.now)
    img = models.BinaryField()

    def __str__(self):
        return f"PerevalImages {self.id}"


class PerevalAdded(models.Model):
    STATUS_CHOICES = [
        ('new', 'New'),
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ]

    id = models.AutoField(primary_key=True)
    date_added = models.DateTimeField()
    beauty_title = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    other_titles = models.CharField(max_length=255)
    connect = models.CharField(max_length=255)
    add_time = models.DateTimeField()

    coord_id = models.ForeignKey(Coords, on_delete=models.CASCADE)

    winter_level = models.CharField(max_length=255, blank=True, null=True)
    summer_level = models.CharField(max_length=255, blank=True, null=True)
    autumn_level = models.CharField(max_length=255, blank=True, null=True)
    spring_level = models.CharField(max_length=255, blank=True, null=True)

    raw_data = models.JSONField()

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')

    def __str__(self):
        return f"PerevalAdded {self.id}"


class PerevalImagesLink(models.Model):
    id = models.AutoField(primary_key=True)
    pereval = models.ForeignKey(PerevalAdded, on_delete=models.CASCADE)
    image = models.ForeignKey(PerevalImages, on_delete=models.CASCADE)

    def __str__(self):
        return f"PerevalImagesLink {self.id}"

class PerevalAreas(models.Model):
    id = models.BigAutoField(primary_key=True)
    id_parent = models.ForeignKey('self', on_delete=models.CASCADE)
    title = models.TextField()

    def __str__(self):
        return f"PerevalAreas {self.id}"


class SprActivitiesTypes(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField()

    def __str__(self):
        return f"SprActivitiesTypes {self.id}"


class Users(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"Users {self.id}"


