from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


class CustomUserManager(BaseUserManager):
    """
    Assignee : 고희석

    User 모델을 커스텀 하기 위한 CustomUserManager입니다.
    create_user, create_superuser 메소드를 정의하고 있습니다.

    email을 ID로 사용합니다. (unique)
    """

    def create_user(self, email, password, nickname, **extra_fields):
        """
        Assignee : 고희석
        """
        if not email:
            raise ValueError("Users must have an email")
        user = self.model(email=email, nickname=nickname, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, nickname, **extra_fields):
        """
        Assignee : 고희석

        python manage.py createsuperuser 커멘드 실행 시 사용되는 함수입니다.
        관리자 계정을 생성하기 위해 extra_fields를 지정해줍니다.
        """
        extra_fields.setdefault("username", "관리자")
        extra_fields.setdefault("introduce", "관리자 계정입니다.")
        extra_fields.setdefault("mobile_number", "010-0000-0000")
        extra_fields.setdefault("date_of_birth", "1993-08-12")
        extra_fields.setdefault("is_admin", True)
        super_user = self.create_user(
            email=email, password=password, nickname=nickname, **extra_fields
        )
        # user.is_admin = True
        # super_user .save(using=self._db)
        return super_user


class User(AbstractBaseUser):
    """
    Assignee : 고희석

    AbstractBaseUser를 상속받은 Custom User 모델입니다.
    email 필드를 Id로 사용하며 email, nickname 필드는 unique key입니다.

    이름, 프로필 사진, 소개, 휴대폰 번호, 생년월일 등
    간단한 사용자 정보를 받습니다.
    """

    email = models.EmailField("이메일 주소", max_length=100, unique=True)
    password = models.CharField("비밀번호", max_length=128)
    nickname = models.CharField("닉네임", max_length=20, unique=True)

    username = models.CharField("이름", max_length=20)
    profile_image = models.ImageField(
        "프로필 사진",
        upload_to="user/static/profile/",
        max_length=None,
        default="user/static/profile/default_profile_image.jpg",
    )
    introduce = models.CharField("소개", max_length=200, default="안녕하세요~")
    mobile_number = models.CharField("휴대폰 번호", max_length=20)
    date_of_birth = models.DateField("생년월일")

    is_active = models.BooleanField("활성여부", default=True)
    is_admin = models.BooleanField("관리자", default=False)

    join_date = models.DateTimeField("가입일", auto_now_add=True)

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = [
        "email",
        "nickname",
    ]

    objects = CustomUserManager()  # custom user 생성 시 필요

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    # admin 권한 설정
    @property
    def is_staff(self):
        return self.is_admin
