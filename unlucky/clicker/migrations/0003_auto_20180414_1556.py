# Generated by Django 2.0.3 on 2018-04-14 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clicker', '0002_auto_20180414_1543'),
    ]

    operations = [
        migrations.CreateModel(
            name='Obrazki',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('obrazek_nazwa', models.CharField(max_length=60, verbose_name='obrazek_nazwa')),
                ('obrazek_image', models.CharField(max_length=5000, verbose_name='event_image_url')),
                ('stress3', models.IntegerField(default=0, verbose_name='stress1')),
                ('friends3', models.IntegerField(default=0, verbose_name='friends1')),
                ('cigaretes3', models.IntegerField(default=0, verbose_name='cigaretes1')),
                ('alcochol3', models.IntegerField(default=0, verbose_name='alcochol1')),
                ('drugs3', models.IntegerField(default=0, verbose_name='drugs1')),
            ],
        ),
        migrations.RemoveField(
            model_name='event',
            name='alcochol',
        ),
        migrations.RemoveField(
            model_name='event',
            name='cigaretes',
        ),
        migrations.RemoveField(
            model_name='event',
            name='drugs',
        ),
        migrations.RemoveField(
            model_name='event',
            name='friends',
        ),
        migrations.RemoveField(
            model_name='event',
            name='stress',
        ),
        migrations.AddField(
            model_name='event',
            name='alcochol1',
            field=models.IntegerField(default=0, verbose_name='alcochol1'),
        ),
        migrations.AddField(
            model_name='event',
            name='alcochol2',
            field=models.IntegerField(default=0, verbose_name='alcochol2'),
        ),
        migrations.AddField(
            model_name='event',
            name='cigaretes1',
            field=models.IntegerField(default=0, verbose_name='cigaretes1'),
        ),
        migrations.AddField(
            model_name='event',
            name='cigaretes2',
            field=models.IntegerField(default=0, verbose_name='cigaretes2'),
        ),
        migrations.AddField(
            model_name='event',
            name='drugs1',
            field=models.IntegerField(default=0, verbose_name='drugs1'),
        ),
        migrations.AddField(
            model_name='event',
            name='drugs2',
            field=models.IntegerField(default=0, verbose_name='drugs2'),
        ),
        migrations.AddField(
            model_name='event',
            name='friends1',
            field=models.IntegerField(default=0, verbose_name='friends1'),
        ),
        migrations.AddField(
            model_name='event',
            name='friends2',
            field=models.IntegerField(default=0, verbose_name='friends2'),
        ),
        migrations.AddField(
            model_name='event',
            name='stress1',
            field=models.IntegerField(default=0, verbose_name='stress1'),
        ),
        migrations.AddField(
            model_name='event',
            name='stress2',
            field=models.IntegerField(default=0, verbose_name='stress2'),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_image',
            field=models.CharField(max_length=5000, verbose_name='event_image_url'),
        ),
    ]