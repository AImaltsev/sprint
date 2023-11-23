from django.utils import timezone

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


class DatabaseHandler:
    def add_pereval(self, beauty_title, title, other_titles, connect, add_time, coords_data, levels, raw_data):
        # Создаем объект координат
        coords = Coords.objects.create(**coords_data)

        # Создаем объект перевала
        pereval = PerevalAdded.objects.create(
            date_added=timezone.now(),
            beauty_title=beauty_title,
            title=title,
            other_titles=other_titles,
            connect=connect,
            add_time=add_time,
            coord_id=coords,
            winter_level=levels.get('winter', ''),
            summer_level=levels.get('summer', ''),
            autumn_level=levels.get('autumn', ''),
            spring_level=levels.get('spring', ''),
            raw_data=raw_data,
            status='new'  # Устанавливаем значение поля status равным new
        )

        return pereval

    def add_area(self, id_parent, title):
        # Создаем объект области
        area = PerevalAreas.objects.create(
            id_parent=id_parent,
            title=title
        )

        return area

    def add_image(self, img_data):
        # Создаем объект изображения
        image = PerevalImages.objects.create(
            date_added=timezone.now(),
            img=img_data
        )

        return image

    def link_image_to_pereval(self, pereval, image):
        # Создаем связь между изображением и перевалом
        link = PerevalImagesLink.objects.create(
            pereval=pereval,
            image=image
        )

        return link

    def add_activity_type(self, title):
        # Создаем тип активности
        activity_type = SprActivitiesTypes.objects.create(
            title=title
        )

        return activity_type