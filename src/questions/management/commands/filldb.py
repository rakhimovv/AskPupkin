from django.core.management.base import BaseCommand
from questions.models import Question, Response
from users.models import User
from tags_likes.models import Tag, QuestionLike, ResponseLike
from django.contrib.auth.models import BaseUserManager
from django.conf import settings


class Command(BaseCommand):
    def _create_db(self):
        # Create tags
        t1 = Tag.objects.create(title="python")
        t2 = Tag.objects.create(title="build")
        t3 = Tag.objects.create(title="mail")
        t4 = Tag.objects.create(title="moon")
        t5 = Tag.objects.create(title="world")

        # Create users
        # u1 = settings.AUTH_USER_MODEL.objects.create_user()

        # Create questions


        # Create responses

        # Create question likes

        # Create response likes

    def handle(self, *args, **options):
        self._create_db()
