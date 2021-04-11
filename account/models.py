from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='profile')
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='user/%Y/%m/%d', blank=True)

    def __str__(self):
        return f"Profile de {self.user.username}"


class Contact(models.Model):
    user_from = models.ForeignKey(get_user_model(), related_name='rel_from_set',
                                  on_delete=models.CASCADE)
    user_to = models.ForeignKey(get_user_model(), related_name='rel_to_set',
                                  on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)

    def __str_(self):
        return f"{self.user_from} follows {self.user_to}"

user_model = get_user_model()
user_model.add_to_class('following', models.ManyToManyField('self', 
                                        through=Contact,
                                        related_name='followers',
                                        symmetrical=False)
                                )