# Generated by Django 2.2.2 on 2021-07-01 08:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ticket', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticketcomment',
            name='commenter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='ticketcomment',
            name='ticket',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ticket.Ticket'),
        ),
        migrations.AddField(
            model_name='ticket',
            name='assigned_to',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tickets_assigned', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='ticket',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tickets_created', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='ticket',
            name='priority',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ticket.Priority'),
        ),
        migrations.AddField(
            model_name='ticket',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ticket.Project'),
        ),
        migrations.AddField(
            model_name='ticket',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ticket.Status'),
        ),
    ]