from django.core.management.base import BaseCommand
from questions.models import Question, Response
from users.models import User
from tags_likes.models import Tag, QuestionLike, ResponseLike
from django.contrib.auth.models import BaseUserManager
from django.conf import settings


class Command(BaseCommand):
    def _create_db(self):
        cap = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore."

        # Create tags
        t1 = Tag.objects.create(title="python")
        t2 = Tag.objects.create(title="build")
        t3 = Tag.objects.create(title="mail")
        t4 = Tag.objects.create(title="moon")
        t5 = Tag.objects.create(title="world")

        # Create users
        u0 = User.objects.create_superuser(username='retina', password='123', email='risonyo@gmail.com')
        u1 = User.objects.create_user(username='ruslan', password='123')
        u2 = User.objects.create_user(username='oleg', password='123')
        u3 = User.objects.create_user(username='nastya', password='123')

        # Create questions
        q1 = Question(title='How to build a moon park?', content=cap, author=u1)
        q1.save()
        q1.tags.add(t1, t2, t3)

        q2 = Question(title='How to build a moon park?', content=cap, author=u2)
        q2.save()
        q2.tags.add(t1, t4, t5)

        q3 = Question(title='How to build a moon park?', content=cap, author=u3)
        q3.save()
        q3.tags.add(t2, t4)

        # Create responses
        r1 = Response.objects.create(content=cap, question=q1, author=u2)
        r2 = Response.objects.create(content=cap, question=q1, author=u3, is_right=True)

        r3 = Response.objects.create(content=cap, question=q2, author=u3)
        r4 = Response.objects.create(content=cap, question=q2, author=u1, is_right=True)

        r5 = Response.objects.create(content=cap, question=q3, author=u1)
        r6 = Response.objects.create(content=cap, question=q3, author=u2, is_right=True)

        # Create question likes
        ql1 = QuestionLike.objects.create(user=u2, question=q1)
        ql2 = QuestionLike.objects.create(user=u3, question=q1)
        ql3 = QuestionLike.objects.create(user=u1, question=q2)

        # Create response likes
        rl1 = ResponseLike.objects.create(user=u1, response=r5)
        rl2 = ResponseLike.objects.create(user=u1, response=r6)

    def handle(self, *args, **options):
        self._create_db()
