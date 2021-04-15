from django.db import models


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
    #  min_value=100000, max_value=999999,
    index = models.PositiveIntegerField(blank=True)

    def __str__(self):
        return (self.country + self.city + self.street + self.house_number)

    class Meta:
        verbose_name = 'Address'
        verbose_name_plural = 'Addresses'


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'


class Event(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    short_description = models.CharField(max_length=300)
    # event_date = models.DateTimeField()
    link = models.URLField(max_length=200, unique=True)
    # , on_delete=models.CASCADE
    tag = models.ManyToManyField(Tag)
    organizers = models.CharField(max_length=100)
    # TODO: change to html document probably
    additional_information = models.CharField(max_length=500, blank=True)
    main_image = models.ImageField(
        default="img_not_found", upload_to="events/")
    background_image = models.ImageField(
        default="img_not_found_bg", upload_to="events/")
    # TODO: implement array of photos

    class Meta:
        abstract = True

    def __str__(self):
        return self.title

    def get_image(self):
        # if not self.img:
        #     return f'{settings.STATIC_URL}NOT_FOUND.png'
        return self.main_image.ur


class OnlineEvent(Event):
    # ? is it the right thing to do?
    list_of_dates = models.JSONField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Online Event'
        verbose_name_plural = 'Online Events'


class Place(Event):
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Place'
        verbose_name_plural = 'Places'


class RealLifeEvent(Place):
    # ? is it the right thing to do?
    list_of_dates = models.JSONField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Real Life Event'
        verbose_name_plural = 'Real Life Events'
