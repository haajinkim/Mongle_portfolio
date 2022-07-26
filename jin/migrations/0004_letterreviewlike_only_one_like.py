# Generated by Django 4.0.6 on 2022-07-26 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("jin", "0003_rename_review_id_letterreviewlike_letter_review_and_more"),
    ]

    operations = [
        migrations.AddConstraint(
            model_name="letterreviewlike",
            constraint=models.UniqueConstraint(
                fields=("letter_review", "user"), name="only_one_like"
            ),
        ),
    ]
