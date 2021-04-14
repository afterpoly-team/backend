from django.db import models

# Create your models here.


class Address(models.Model):
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=50, blank=True)
    region = models.CharField(max_length=50, blank=True)
    street = models.CharField(max_length=50)
    # корпус
    corps = models.CharField(max_length=50, blank=True)
    house_number = models.PositiveIntegerField()
    # индекс (только русский?)
    index = models.PositiveIntegerField(
        min_value=100000, max_value=999999, blank=True)

    def __str__(self):
        return (self.country + self.city + self.street + self.house_number)


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Event(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    short_description = models.CharField(max_length=300)
    # event_date = models.DateTimeField()
    link = models.URLField(max_length=200, unique=True)
    tag = models.ManyToManyField(Tag, on_delete=models.CASCADE)
    organizers = models.CharField(max_length=100)
    # TODO: change to html document probably
    additional_information = models.CharField(max_length=500)
    main_image = models.ImageField(upload_to="events/")
    background_image = models.ImageField(upload_to="events/")
    # TODO: implement array of photos

    class Meta:
        # db_table = ''
        # managed = True
        # verbose_name = 'ModelName'
        # verbose_name_plural = 'ModelNames'
        abstract = True

    def __str__(self):
        return self.title


class OnlineEvent(Event):
    # ? is it the right thing to do?
    list_of_dates = models.JSONField()

    def __str__(self):
        return self.title


class Place(Event):
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class RealLifeEvent(Place):
    # ? is it the right thing to do?
    list_of_dates = models.JSONField()

    def __str__(self):
        return self.title
