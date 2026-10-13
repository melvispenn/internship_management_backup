from django.core import mail
from django.test import TestCase

from internship_management.users.models import User
from internship_management.internships.models import Invitation


class InvitationFlowTests(TestCase):
    def setUp(self):
        self.admin = User.objects.create_user(
            email="admin@example.com",
            password="StrongPass123!",
            name="Admin User",
            role="admin",
        )

    def test_invitation_acceptance_updates_status_and_sends_email(self):
        invitation = Invitation.objects.create(
            email="intern@example.com",
            role="intern",
            specialty="Software Development",
            invited_by=self.admin,
        )

        invitation.accept()

        invitation.refresh_from_db()
        self.assertEqual(invitation.status, "accepted")
        self.assertTrue(invitation.accepted_at is not None)
        self.assertEqual(len(mail.outbox), 1)
        self.assertIn("accepted", mail.outbox[0].subject.lower())

    def test_user_role_and_specialty_are_stored(self):
        user = User.objects.create_user(
            email="supervisor@example.com",
            password="StrongPass123!",
            name="Supervisor User",
            role="supervisor",
            specialty="Data Science",
        )

        self.assertEqual(user.role, "supervisor")
        self.assertEqual(user.specialty, "Data Science")
