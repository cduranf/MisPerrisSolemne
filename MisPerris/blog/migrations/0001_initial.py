# Generated by Django 2.1.2 on 2018-10-26 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=200)),
                ('Descripcion', models.TextField()),
                ('Estado', models.TextField(choices=[('Espera', 'Espera'), ('Adoptado', 'Adoptado')], default='Espera')),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('picture', models.ImageField(default='default.jpg', upload_to='user_pics')),
            ],
        ),
    ]
