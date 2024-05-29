# Generated by Django 4.2.13 on 2024-05-28 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("course_work_app", "0006_alter_profilepicture_profile_picture"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="invitation",
            name="video",
        ),
        migrations.AlterField(
            model_name="invitation",
            name="invitation_id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="invitation",
            name="photo",
            field=models.TextField(default="1"),
            preserve_default=False,
        ),
    ]