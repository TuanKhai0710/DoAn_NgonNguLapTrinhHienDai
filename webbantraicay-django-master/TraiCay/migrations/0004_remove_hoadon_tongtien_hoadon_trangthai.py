# Generated by Django 4.2.11 on 2024-06-03 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TraiCay', '0003_khachhang_user_giohang'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hoadon',
            name='TongTien',
        ),
        migrations.AddField(
            model_name='hoadon',
            name='TrangThai',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
