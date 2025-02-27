from datetime import date


def get_weekday():
    return date.today().strftime("%A")


def create_new_post(post, weekday=get_weekday()):
    post_copy = post.copy()
    post_copy["created_on_weekday"] = weekday
    return post_copy


initial_post = {
    "id": 243,
    "author": "Aye",
}

post_with_weekday = create_new_post(initial_post)

print(post_with_weekday)


# ----------------------------
def send_email(to: str, subject: str, *args, urgency: str = "urgent", **kwargs):
    """
    Sends email to different recipients

    :param str to: Recipient address
    :param str subject: Email subject
    :param str args: Additional recipients
    :param str urgency: Urgency of the email
    :param str kwargs: Additional details
    :return None:
    """
    print(f"Sending an email to: {to}")
    print(f"Email subject: {subject}")

    if args:
        print("Additional recipients:")
        for recipient in args:
            print(recipient)

    print(f"Urgency: {urgency}")

    if kwargs:
        print("Additional details for the email:")
        for key in list(kwargs):
            print(f"{key}: {kwargs[key]}")


send_email(
    "test@test.com",
    "Hello there!",
    "other@test.com",
    "someone@gmail.com",
    "admin@test.com",
    urgency="not urgent",
    bcc="Aye@gmail.com",
    img="test.png",
)
