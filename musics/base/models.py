from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class User(AbstractBaseUser, PermissionsMixin):
    """
    App music collection user class
    Full name, username, password and role (user/admin) are required.
    """

    full_name = models.CharField(_("full name"), max_length=150, blank=False)
    username = models.CharField(_("user name"), max_length=32, blank=False, unique=True)
    password = models.EmailField(_("email address"), blank=False)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    # objects = UserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["full_name", "password"]

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def clean(self):
        super().clean()
        self.username = self.__class__.objects.normalize_email(self.username)

    def get_full_name(self):
        """
        Return the full name.
        """
        full_name = "%s" % self.full_name
        return full_name.strip()
