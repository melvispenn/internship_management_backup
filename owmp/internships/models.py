from django.conf import settings
from django.core.mail import send_mail
from django.db import models
from django.utils import timezone


class Invitation(models.Model):
    class Status(models.TextChoices):
        PENDING = "pending", "Pending"
        ACCEPTED = "accepted", "Accepted"

    email = models.EmailField()
    role = models.CharField(max_length=32)
    specialty = models.CharField(max_length=255, blank=True)
    invited_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="sent_invitations",
    )
    status = models.CharField(
        max_length=16, choices=Status.choices, default=Status.PENDING
    )
    accepted_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def accept(self):
        """Mark the invitation accepted and notify the invited address."""
        if self.status == self.Status.ACCEPTED:
            return

        self.status = self.Status.ACCEPTED
        self.accepted_at = timezone.now()
        self.save(update_fields=["status", "accepted_at"])
        send_mail(
            subject="Internship invitation accepted",
            message=f"The invitation for {self.email} has been accepted.",
            from_email=None,
            recipient_list=[self.invited_by.email],
            fail_silently=False,
        )

    def __str__(self):
        return f"{self.email} ({self.status})"
