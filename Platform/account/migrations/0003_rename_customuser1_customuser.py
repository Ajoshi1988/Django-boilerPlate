# Generated by Django 4.2 on 2024-08-26 06:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
        ("admin", "0003_logentry_add_action_flag_choices"),
        ("account", "0002_rename_customuser_customuser1"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="CustomUser1",
            new_name="CustomUser",
        ),
    ]
