from statistics import mode

from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from base.models import BaseModel


class Product(BaseModel):
    code = models.SlugField(_("Code"), unique=True)
    name = models.CharField(_("Name"), max_length=32)
    country = models.ManyToManyField(to="address.Country", verbose_name=_("Country"))
    seller = models.ForeignKey(User, verbose_name=_("Seller"), on_delete=models.CASCADE)
    is_active = models.BooleanField(_("Is active"), default=True)

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def __str__(self) -> str:
        return f"{self.name} <{self.code}>"

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = slugify(self.name)
        super().save(*args, **kwargs)
