# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-04-30 21:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salary', '0002_auto_20170430_1516'),
    ]

    operations = [
        migrations.AddField(
            model_name='preyearendperformanceappraisa',
            name='amount',
            field=models.FloatField(default=0.0, verbose_name='\u91d1\u989d'),
        ),
        migrations.AddField(
            model_name='specialbenefitaward',
            name='amount',
            field=models.FloatField(default=0.0, verbose_name='\u91d1\u989d'),
        ),
        migrations.AlterField(
            model_name='cadredutyaward',
            name='index',
            field=models.FloatField(default=0.0, verbose_name='\u6570\u91cf'),
        ),
        migrations.AlterField(
            model_name='cadredutyaward',
            name='other',
            field=models.FloatField(default=0.0, verbose_name='\u5176\u5b83\u8865\u8d34'),
        ),
        migrations.AlterField(
            model_name='cadredutyaward',
            name='standard',
            field=models.FloatField(default=0.0, verbose_name='\u6807\u51c6'),
        ),
        migrations.AlterField(
            model_name='cadredutyaward',
            name='subsidy',
            field=models.FloatField(default=0.0, verbose_name='\u8865\u8d34'),
        ),
        migrations.AlterField(
            model_name='cadredutyaward',
            name='tax',
            field=models.FloatField(default=0.0, verbose_name='\u6240\u5f97\u7a0e'),
        ),
        migrations.AlterField(
            model_name='food',
            name='amount',
            field=models.FloatField(default=0.0, verbose_name='\u91d1\u989d'),
        ),
        migrations.AlterField(
            model_name='food',
            name='index',
            field=models.IntegerField(default=1, verbose_name='\u6570\u91cf'),
        ),
        migrations.AlterField(
            model_name='food',
            name='standard',
            field=models.FloatField(default=0.0, verbose_name='\u6807\u51c6'),
        ),
        migrations.AlterField(
            model_name='food',
            name='tax',
            field=models.FloatField(default=0.0, verbose_name='\u6240\u5f97\u7a0e'),
        ),
        migrations.AlterField(
            model_name='govperformanceappraisa',
            name='amount',
            field=models.FloatField(default=0.0, verbose_name='\u91d1\u989d'),
        ),
        migrations.AlterField(
            model_name='govperformanceappraisa',
            name='other',
            field=models.FloatField(default=0.0, verbose_name='\u6263\u9664\u5176\u5b83'),
        ),
        migrations.AlterField(
            model_name='govperformanceappraisa',
            name='ratio',
            field=models.FloatField(default=0.0, verbose_name='\u7cfb\u6570'),
        ),
        migrations.AlterField(
            model_name='govperformanceappraisa',
            name='standard',
            field=models.FloatField(default=0.0, verbose_name='\u6807\u51c6'),
        ),
        migrations.AlterField(
            model_name='govperformanceappraisa',
            name='tax',
            field=models.FloatField(default=0.0, verbose_name='\u6240\u5f97\u7a0e'),
        ),
        migrations.AlterField(
            model_name='preyearendperformanceappraisa',
            name='index',
            field=models.FloatField(default=0.0, verbose_name='\u6570\u91cf'),
        ),
        migrations.AlterField(
            model_name='preyearendperformanceappraisa',
            name='other',
            field=models.FloatField(default=0.0, verbose_name='\u5176\u5b83\u8865\u8d34'),
        ),
        migrations.AlterField(
            model_name='preyearendperformanceappraisa',
            name='standard',
            field=models.FloatField(default=0.0, verbose_name='\u6807\u51c6'),
        ),
        migrations.AlterField(
            model_name='preyearendperformanceappraisa',
            name='tax',
            field=models.FloatField(default=0.0, verbose_name='\u6240\u5f97\u7a0e'),
        ),
        migrations.AlterField(
            model_name='reallysalary',
            name='area_allowance',
            field=models.FloatField(default=0.0, verbose_name='\u7279\u533a\u6d25\u8d34'),
        ),
        migrations.AlterField(
            model_name='reallysalary',
            name='base_allowance',
            field=models.FloatField(default=0.0, verbose_name='\u57fa\u7840\u6d25\u8d34'),
        ),
        migrations.AlterField(
            model_name='reallysalary',
            name='housing_fund',
            field=models.FloatField(default=0.0, verbose_name='\u4f4f\u623f\u516c\u79ef\u91d1'),
        ),
        migrations.AlterField(
            model_name='reallysalary',
            name='housing_fund2',
            field=models.FloatField(default=0.0, verbose_name='\u4f4f\u623f\u516c\u79ef\u91d12'),
        ),
        migrations.AlterField(
            model_name='reallysalary',
            name='level_wage',
            field=models.FloatField(default=0.0, verbose_name='\u85aa\u7ea7\u5de5\u8d44'),
        ),
        migrations.AlterField(
            model_name='reallysalary',
            name='nursing_age',
            field=models.IntegerField(default=0, verbose_name='\u62a4\u9f84'),
        ),
        migrations.AlterField(
            model_name='reallysalary',
            name='other',
            field=models.FloatField(default=0.0, verbose_name='\u5176\u5b83'),
        ),
        migrations.AlterField(
            model_name='reallysalary',
            name='post_wage',
            field=models.FloatField(default=0.0, verbose_name='\u5c97\u4f4d\u5de5\u8d44'),
        ),
        migrations.AlterField(
            model_name='reallysalary',
            name='rent',
            field=models.FloatField(default=0.0, verbose_name='\u623f\u79df'),
        ),
        migrations.AlterField(
            model_name='reallysalary',
            name='shortage_post',
            field=models.FloatField(default=0.0, verbose_name='\u7d27\u7f3a\u5c97\u4f4d'),
        ),
        migrations.AlterField(
            model_name='reallysalary',
            name='special_post_allowance',
            field=models.FloatField(default=0.0, verbose_name='\u7279\u6b8a\u5c97\u4f4d\u6d25\u8d34'),
        ),
        migrations.AlterField(
            model_name='reallysalary',
            name='tax',
            field=models.FloatField(default=0.0, verbose_name='\u6240\u5f97\u7a0e'),
        ),
        migrations.AlterField(
            model_name='reallysalary',
            name='urance_benefit',
            field=models.FloatField(default=0.0, verbose_name='\u4fdd\u9669\u91d1'),
        ),
        migrations.AlterField(
            model_name='reallysalary',
            name='utilities',
            field=models.FloatField(default=0.0, verbose_name='\u6c34\u7535'),
        ),
        migrations.AlterField(
            model_name='specialbenefitaward',
            name='index',
            field=models.FloatField(default=0.0, verbose_name='\u6570\u91cf'),
        ),
        migrations.AlterField(
            model_name='specialbenefitaward',
            name='other',
            field=models.FloatField(default=0.0, verbose_name='\u5176\u5b83\u8865\u8d34'),
        ),
        migrations.AlterField(
            model_name='specialbenefitaward',
            name='standard',
            field=models.FloatField(default=0.0, verbose_name='\u6807\u51c6'),
        ),
        migrations.AlterField(
            model_name='specialbenefitaward',
            name='tax',
            field=models.FloatField(default=0.0, verbose_name='\u6240\u5f97\u7a0e'),
        ),
    ]