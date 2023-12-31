# Generated by Django 4.2.7 on 2024-01-03 14:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_finals'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ranking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opponent', models.CharField(blank=True, max_length=100, null=True)),
                ('team_score', models.IntegerField(default=0)),
                ('opponent_score', models.IntegerField(default=0)),
                ('score_modified', models.BooleanField(default=False)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.team')),
                ('tournament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.tournament')),
            ],
        ),
    ]
