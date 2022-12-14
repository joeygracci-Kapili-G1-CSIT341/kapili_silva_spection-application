# Generated by Django 4.0.5 on 2022-07-19 11:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0006_alter_product_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=200, null=True)),
                ('last_name', models.CharField(blank=True, max_length=200, null=True)),
                ('phone', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.CharField(blank=True, max_length=200, null=True)),
                ('purpose', models.CharField(blank=True, max_length=200, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('time', models.TimeField(blank=True, null=True)),
                ('status', models.CharField(blank=True, default='Not Arrived', max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('desc', models.CharField(blank=True, max_length=200, null=True)),
                ('profile_pic', models.ImageField(blank=True, default='pexels-misael-garcia-1707828.jpg', null=True, upload_to='')),
                ('headline', models.BooleanField(blank=True, default=False, max_length=200, null=True)),
                ('date_created', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('badge', models.CharField(blank=True, max_length=200, null=True)),
                ('date', models.CharField(blank=True, max_length=200, null=True)),
                ('type', models.CharField(blank=True, max_length=200, null=True)),
                ('everyYear', models.BooleanField(blank=True, default=False, null=True)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('color', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='patient',
            name='email',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='name',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='phone',
        ),
        migrations.AddField(
            model_name='patient',
            name='pd',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Signs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('signs_details', models.CharField(blank=True, max_length=200, null=True)),
                ('activity_details', models.CharField(blank=True, max_length=200, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.case')),
            ],
        ),
        migrations.CreateModel(
            name='Rx',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('od_old_rx', models.CharField(blank=True, max_length=200, null=True)),
                ('od_dist_vasc', models.CharField(blank=True, max_length=200, null=True)),
                ('od_dist_vacc', models.CharField(blank=True, max_length=200, null=True)),
                ('od_near_vasc', models.CharField(blank=True, max_length=200, null=True)),
                ('od_near_vacc', models.CharField(blank=True, max_length=200, null=True)),
                ('od_phv', models.CharField(blank=True, max_length=200, null=True)),
                ('os_old_rx', models.CharField(blank=True, max_length=200, null=True)),
                ('os_dist_vasc', models.CharField(blank=True, max_length=200, null=True)),
                ('os_dist_vacc', models.CharField(blank=True, max_length=200, null=True)),
                ('os_near_vasc', models.CharField(blank=True, max_length=200, null=True)),
                ('os_near_vacc', models.CharField(blank=True, max_length=200, null=True)),
                ('os_phv', models.CharField(blank=True, max_length=200, null=True)),
                ('ou_old_rx', models.CharField(blank=True, max_length=200, null=True)),
                ('ou_dist_vasc', models.CharField(blank=True, max_length=200, null=True)),
                ('ou_dist_vacc', models.CharField(blank=True, max_length=200, null=True)),
                ('ou_near_vasc', models.CharField(blank=True, max_length=200, null=True)),
                ('ou_near_vacc', models.CharField(blank=True, max_length=200, null=True)),
                ('ou_phv', models.CharField(blank=True, max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Refraction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('od_auto_refraction', models.CharField(blank=True, max_length=200, null=True)),
                ('os_auto_refraction', models.CharField(blank=True, max_length=200, null=True)),
                ('os_retinoscopy', models.CharField(blank=True, max_length=200, null=True)),
                ('od_retinoscopy', models.CharField(blank=True, max_length=200, null=True)),
                ('od_cycoplastic', models.CharField(blank=True, max_length=200, null=True)),
                ('os_cycoplastic', models.CharField(blank=True, max_length=200, null=True)),
                ('od_subjective', models.CharField(blank=True, max_length=200, null=True)),
                ('os_subjective', models.CharField(blank=True, max_length=200, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.case')),
            ],
        ),
        migrations.CreateModel(
            name='PupilReflex',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('od_direct', models.CharField(blank=True, max_length=200, null=True)),
                ('od_consensual', models.CharField(blank=True, max_length=200, null=True)),
                ('od_swing', models.CharField(blank=True, max_length=200, null=True)),
                ('os_direct', models.CharField(blank=True, max_length=200, null=True)),
                ('os_consensual', models.CharField(blank=True, max_length=200, null=True)),
                ('os_swing', models.CharField(blank=True, max_length=200, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.case')),
            ],
        ),
        migrations.CreateModel(
            name='PupilMeasurement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('od_horizontal', models.CharField(blank=True, max_length=200, null=True)),
                ('od_vertical', models.CharField(blank=True, max_length=200, null=True)),
                ('os_horizontal', models.CharField(blank=True, max_length=200, null=True)),
                ('os_vertical', models.CharField(blank=True, max_length=200, null=True)),
                ('maddox_rod', models.CharField(blank=True, max_length=200, null=True)),
                ('maddox_wing', models.CharField(blank=True, max_length=200, null=True)),
                ('vergence', models.CharField(blank=True, max_length=200, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.case')),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('description', models.CharField(max_length=200, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('statement', models.CharField(blank=True, max_length=200, null=True)),
                ('dm', models.BooleanField(blank=True, default=False, null=True)),
                ('hpn', models.BooleanField(blank=True, default=False, null=True)),
                ('allergies', models.BooleanField(blank=True, default=False, null=True)),
                ('medical_history', models.CharField(blank=True, max_length=200, null=True)),
                ('treatments', models.CharField(blank=True, max_length=200, null=True)),
                ('ocular_history', models.CharField(blank=True, max_length=200, null=True)),
                ('physical_condition', models.CharField(blank=True, max_length=200, null=True)),
                ('dominant_hand', models.CharField(blank=True, default='Left', max_length=200, null=True)),
                ('dominant_eye', models.CharField(blank=True, max_length=200, null=True)),
                ('ipd', models.CharField(blank=True, max_length=200, null=True)),
                ('bp', models.CharField(blank=True, max_length=200, null=True)),
                ('od', models.CharField(blank=True, max_length=200, null=True)),
                ('os', models.CharField(blank=True, max_length=200, null=True)),
                ('anatomical', models.BooleanField(blank=True, default=False, null=True)),
                ('catopric', models.BooleanField(blank=True, default=False, null=True)),
                ('tentative_diag', models.CharField(blank=True, max_length=200, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.case')),
            ],
        ),
        migrations.CreateModel(
            name='CoverTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('od_far_unilateral', models.CharField(blank=True, max_length=200, null=True)),
                ('os_far_unilateral', models.CharField(blank=True, max_length=200, null=True)),
                ('od_far_alternating', models.CharField(blank=True, max_length=200, null=True)),
                ('os_far_alternating', models.CharField(blank=True, max_length=200, null=True)),
                ('od_near_unilateral', models.CharField(blank=True, max_length=200, null=True)),
                ('os_near_unilateral', models.CharField(blank=True, max_length=200, null=True)),
                ('od_near_alternating', models.CharField(blank=True, max_length=200, null=True)),
                ('os_near_alternating', models.CharField(blank=True, max_length=200, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.case')),
            ],
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=200, null=True)),
                ('middle_name', models.CharField(blank=True, max_length=200, null=True)),
                ('last_name', models.CharField(blank=True, max_length=200, null=True)),
                ('occupation', models.CharField(blank=True, max_length=200, null=True)),
                ('phone', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.CharField(blank=True, max_length=200, null=True)),
                ('profile_pic', models.ImageField(blank=True, default='pexels-misael-garcia-1707828.jpg', null=True, upload_to='')),
                ('birthday', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, max_length=200, null=True)),
                ('street', models.CharField(blank=True, max_length=200, null=True)),
                ('barangay', models.CharField(blank=True, max_length=200, null=True)),
                ('city', models.CharField(blank=True, max_length=200, null=True)),
                ('zip', models.CharField(blank=True, max_length=200, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
