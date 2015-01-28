# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mande', '0002_auto_20150128_1113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classroom',
            name='cohort',
            field=models.IntegerField(default=2014, max_length=8, verbose_name=b'Cohort', choices=[(2014, b'2014-2015'), (2015, b'2015-2016'), (2016, b'2016-2017'), (2017, b'2017-2018'), (2018, b'2018-2019'), (2019, b'2019-2020'), (2020, b'2020-2021'), (2021, b'2021-2022'), (2022, b'2022-2023'), (2023, b'2023-2024'), (2024, b'2024-2025')]),
            preserve_default=True,
        ),
    ]
