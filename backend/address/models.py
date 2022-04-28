from django.db import models
from django.utils.translation import gettext_lazy as _

from base.models import BaseModel


class Country(BaseModel):
    code = models.CharField(_("Code"), unique=True, max_length=2)
    name = models.CharField(_("Name"), max_length=32)
    is_active = models.BooleanField(_("Is active"), default=True)

    class Meta:
        verbose_name = _("Country")
        verbose_name_plural = "Countries"

    def __str__(self) -> str:
        return f"{self.name} <{self.code}>"
