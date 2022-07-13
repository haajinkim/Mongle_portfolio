# Generated by Django 4.0.6 on 2022-07-13 00:45

from django.conf import settings
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jin', '0003_rename_category_woory_category_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Letter_Review',
            new_name='LetterReview',
        ),
        migrations.RenameModel(
            old_name='Letter_Review_Like',
            new_name='LetterReviewLike',
        ),
        migrations.RenameModel(
            old_name='User_Letter_Target_User',
            new_name='UserLetterTargetUser',
        ),
        migrations.RenameModel(
            old_name='Woory_Category',
            new_name='WooryCategory',
        ),
        migrations.AddField(
            model_name='letter',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
