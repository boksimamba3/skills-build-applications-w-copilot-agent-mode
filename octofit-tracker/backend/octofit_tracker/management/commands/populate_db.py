from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()
        Workout.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='DC', description='DC Superheroes')

        # Create Users
        users = [
            User(name='Spider-Man', email='spiderman@marvel.com', team=marvel.name),
            User(name='Iron Man', email='ironman@marvel.com', team=marvel.name),
            User(name='Wonder Woman', email='wonderwoman@dc.com', team=dc.name),
            User(name='Batman', email='batman@dc.com', team=dc.name),
        ]
        for user in users:
            user.save()

        # Create Activities
        Activity.objects.create(user=users[0], activity_type='Running', duration_minutes=30, date=timezone.now().date())
        Activity.objects.create(user=users[1], activity_type='Cycling', duration_minutes=45, date=timezone.now().date())
        Activity.objects.create(user=users[2], activity_type='Swimming', duration_minutes=25, date=timezone.now().date())
        Activity.objects.create(user=users[3], activity_type='Yoga', duration_minutes=60, date=timezone.now().date())

        # Create Leaderboard
        Leaderboard.objects.create(team=marvel, points=100)
        Leaderboard.objects.create(team=dc, points=90)

        # Create Workouts
        Workout.objects.create(name='Hero HIIT', description='High intensity workout for heroes', suggested_for_team='Marvel')
        Workout.objects.create(name='Power Yoga', description='Yoga for strength and flexibility', suggested_for_team='DC')

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data!'))
