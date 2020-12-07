from django.db import models

class ApplicationModel(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    moving_from = models.CharField(max_length=255)
    house_size = models.CharField(max_length=255)
    ANSWERS = (('Y', 'Yes'), ('N', 'No'))
    is_moved_up = models.CharField(max_length=1, choices=ANSWERS, 
                                   verbose_name='Need items moved up and down')
    address = models.CharField(max_length=255)
    moving_into = models.CharField(max_length=255)
    next_house_size = models.CharField(max_length=255)
    next_is_moved_up = models.CharField(max_length=1, choices=ANSWERS, 
                                        verbose_name='Next house need items moved up and down')
    next_address = models.CharField(max_length=255)
    extra_items = models.CharField(max_length=1, choices=ANSWERS, 
                                   verbose_name='Any extra heavy/fragile items')
    additional_service = models.TextField(blank=True)
    comments = models.TextField(blank=True)

    def __str__(self):
        return f'Quote id:{self.pk}'

    class Meta:
        verbose_name = 'Quote'
        verbose_name_plural = 'Quotes'