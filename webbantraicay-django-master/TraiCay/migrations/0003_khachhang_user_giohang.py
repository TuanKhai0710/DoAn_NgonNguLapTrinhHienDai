# Generated by Django 4.2.11 on 2024-06-02 16:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('TraiCay', '0002_slider'),
    ]

    operations = [
        migrations.AddField(
            model_name='khachhang',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='GioHang',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SoLuong', models.IntegerField(default=0)),
                ('SanPham', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TraiCay.sanpham')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
