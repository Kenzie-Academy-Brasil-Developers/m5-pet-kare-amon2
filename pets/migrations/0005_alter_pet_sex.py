# Generated by Django 4.1.3 on 2022-11-30 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pets", "0004_alter_pet_traits"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pet",
            name="sex",
            field=models.CharField(
                choices=[
                    ("Male", "Male"),
                    ("Female", "Female"),
                    ("Not Informed", "Not Informed"),
                ],
                default="Not Informed",
                max_length=20,
            ),
        ),
    ]