# Generated by Django 2.0.3 on 2018-04-14 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clicker', '0003_auto_20180414_1556'),
    ]

    operations = [
        migrations.AddField(
            model_name='obrazki',
            name='obrazek_image2',
            field=models.CharField(default='NULL', max_length=5000, verbose_name='event_image_url2'),
        ),
        migrations.AddField(
            model_name='obrazki',
            name='price3',
            field=models.IntegerField(default=0, verbose_name='price3'),
        ),
        migrations.AlterField(
            model_name='obrazki',
            name='alcochol3',
            field=models.IntegerField(default=0, verbose_name='alcochol3'),
        ),
        migrations.AlterField(
            model_name='obrazki',
            name='cigaretes3',
            field=models.IntegerField(default=0, verbose_name='cigaretes3'),
        ),
        migrations.AlterField(
            model_name='obrazki',
            name='drugs3',
            field=models.IntegerField(default=0, verbose_name='drugs3'),
        ),
        migrations.AlterField(
            model_name='obrazki',
            name='friends3',
            field=models.IntegerField(default=0, verbose_name='friends3'),
        ),
        migrations.AlterField(
            model_name='obrazki',
            name='stress3',
            field=models.IntegerField(default=0, verbose_name='stress3'),
        ),
    ]
