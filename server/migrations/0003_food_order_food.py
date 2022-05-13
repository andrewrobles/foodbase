# Generated by Django 4.0.4 on 2022-05-13 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0002_order_instructions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='food',
            field=models.ManyToManyField(to='server.food'),
        ),
    ]
