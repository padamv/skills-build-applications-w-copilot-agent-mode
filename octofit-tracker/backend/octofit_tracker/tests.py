from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name="Test Team", description="A test team")
        self.assertEqual(team.name, "Test Team")

class UserModelTest(TestCase):
    def test_create_user(self):
        team = Team.objects.create(name="Team1")
        user = User.objects.create(name="Alice", email="alice@example.com", team=team)
        self.assertEqual(user.name, "Alice")

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        team = Team.objects.create(name="Team2")
        user = User.objects.create(name="Bob", email="bob@example.com", team=team)
        activity = Activity.objects.create(user=user, type="Run", duration=30, date="2024-01-01")
        self.assertEqual(activity.type, "Run")

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(name="Pushups", description="Do 20 pushups")
        self.assertEqual(workout.name, "Pushups")

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        team = Team.objects.create(name="Team3")
        leaderboard = Leaderboard.objects.create(team=team, total_points=100, week="2024-W01")
        self.assertEqual(leaderboard.total_points, 100)
