# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-04-17 12:36
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Algorithm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('in_use', models.BooleanField()),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('is_update_of', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='GUIManager.Algorithm')),
            ],
        ),
        migrations.CreateModel(
            name='EvaluationMetric',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_at_10', models.FloatField()),
                ('p_at_20', models.FloatField(null=True)),
                ('p_at_30', models.FloatField(null=True)),
                ('p_at_40', models.FloatField(null=True)),
                ('p_at_50', models.FloatField(null=True)),
                ('ndcg_at_10', models.FloatField()),
                ('ndcg_at_20', models.FloatField(null=True)),
                ('ndcg_at_30', models.FloatField(null=True)),
                ('mrr_at_10', models.FloatField()),
                ('mrr_at_20', models.FloatField(null=True)),
                ('mrr_at_30', models.FloatField(null=True)),
                ('ctr', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MyCatalog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_id', models.IntegerField(default=-1)),
                ('url', models.CharField(max_length=255)),
                ('external_id', models.IntegerField(null=True)),
                ('published_date', models.DateField(null=True)),
                ('journal_name', models.CharField(max_length=255, null=True)),
                ('title', models.CharField(max_length=200, unique=True)),
                ('abstract', models.CharField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='PaperAuthor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='PaperKeyword',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='PaperLDATheta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic_id', models.IntegerField()),
                ('value', models.FloatField()),
                ('paper', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='GUIManager.Paper')),
            ],
        ),
        migrations.CreateModel(
            name='PaperTerm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('term', models.CharField(max_length=200, unique=True)),
                ('relevance_score', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='RatingMatrix',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.SmallIntegerField()),
                ('paper', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GUIManager.Paper')),
                ('timestamp', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Recommendation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('input_rating_count', models.BigIntegerField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('algorithm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GUIManager.Algorithm')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RecommendationResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('predicted_score', models.FloatField()),
                ('predicted_rank', models.SmallIntegerField()),
                ('prediction_type', models.CharField(max_length=200, null=True)),
                ('is_clicked', models.NullBooleanField()),
                ('Refit_cycle', models.IntegerField(null=True)),
                ('paper', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GUIManager.Paper')),
                ('recommendation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GUIManager.Recommendation')),
            ],
        ),
        migrations.CreateModel(
            name='SystemRecommendations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modified_on', models.DateField(auto_now_add=True)),
                ('comments', models.CharField(max_length=500)),
                ('isactive', models.BooleanField(default=True)),
                ('algorithm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GUIManager.Algorithm')),
                ('modified_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserFeedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_rating', models.SmallIntegerField()),
                ('feedback_type', models.CharField(max_length=10)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('recommendationresult_detail', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='GUIManager.RecommendationResult')),
            ],
        ),
        migrations.CreateModel(
            name='UserMapping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('external_hash', models.CharField(max_length=200, null=True)),
                ('external_user_id', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Vocabulary',
            fields=[
                ('term_id', models.IntegerField(primary_key=True, serialize=False)),
                ('term', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='ratingmatrix',
            name='user_map',
            field=models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, to='GUIManager.UserMapping'),
        ),
        migrations.AddField(
            model_name='paper',
            name='authors',
            field=models.ManyToManyField(to='GUIManager.PaperAuthor'),
        ),
        migrations.AddField(
            model_name='paper',
            name='keywords',
            field=models.ManyToManyField(to='GUIManager.PaperKeyword'),
        ),
        migrations.AddField(
            model_name='paper',
            name='terms',
            field=models.ManyToManyField(to='GUIManager.PaperTerm'),
        ),
        migrations.AddField(
            model_name='mycatalog',
            name='papers',
            field=models.ManyToManyField(to='GUIManager.Paper'),
        ),
        migrations.AddField(
            model_name='mycatalog',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='evaluationmetric',
            name='recommendation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GUIManager.Recommendation'),
        ),
    ]