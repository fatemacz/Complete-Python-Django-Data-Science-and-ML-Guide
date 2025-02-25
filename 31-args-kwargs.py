def send_email(to, subject, *args, **kwargs):
    """
    Sends email to different recipients

    :param str to: Recipient address
    :param str subject: Email subject
    :param str args: Additional recipients
    :param str kwargs: Additional details
    :return None:
    """
    print(f"Sending an email to: {to}")
    print(f"Email subject: {subject}")

    if args:
        print("Additional recipients:")
        for recipient in args:
            print(recipient)

    if kwargs:
        print("Additional details for the email:")
        for key in list(kwargs):
            print(f"{key}: {kwargs[key]}")


send_email("test@test.com", "Hello there!")
print("_______")
send_email("test@test.com", "Hello there!", "other@test.com", "someone@gmail.com")
print("_______")
send_email("test@test.com", "Hello there!", bcc="bogdan@gmail.com", img="test.png")
print("_______")
send_email(
    "test@test.com",
    "Hello there!",
    "other@test.com",
    "someone@gmail.com",
    bcc="bogdan@gmail.com",
    img="test.png",
)
print("_______")
send_email(True, 100, 1000)
