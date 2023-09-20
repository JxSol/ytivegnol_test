from django.core.mail import send_mail

from config.celery import app


@app.task
def send_otp(email: str, otp: str, host: str) -> None:
    """Send an email with OTP."""
    send_mail(
        subject=f"Account authentication on {host}",
        message=f"Your authentication code:\n{otp}",
        from_email=None,
        recipient_list=email,
    )
