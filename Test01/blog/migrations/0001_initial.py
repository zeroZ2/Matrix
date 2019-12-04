# Generated by Django 2.2.6 on 2019-12-04 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id_cliente', models.AutoField(db_column='Id_Cliente', primary_key=True, serialize=False)),
                ('contrasenha', models.CharField(blank=True, db_column='Contrasenha', max_length=10, null=True)),
                ('nombre', models.CharField(blank=True, db_column='Nombre', max_length=100, null=True)),
                ('apellido', models.CharField(blank=True, db_column='Apellido', max_length=100, null=True)),
                ('correo', models.CharField(blank=True, db_column='Correo', max_length=100, null=True)),
                ('direccion', models.CharField(blank=True, db_column='Direccion', max_length=100, null=True)),
                ('telefono', models.IntegerField(blank=True, db_column='Telefono', null=True)),
            ],
            options={
                'db_table': 'clientes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DescuentoP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descuento', models.IntegerField(blank=True, db_column='Descuento', null=True)),
            ],
            options={
                'db_table': 'descuento_p',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DetallesPedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(blank=True, db_column='Cantidad', null=True)),
            ],
            options={
                'db_table': 'detalles_pedido',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Empleados',
            fields=[
                ('id_empleado', models.AutoField(db_column='Id_Empleado', primary_key=True, serialize=False)),
                ('contrasenha', models.CharField(blank=True, db_column='Contrasenha', max_length=10, null=True)),
                ('nombre', models.CharField(blank=True, db_column='Nombre', max_length=100, null=True)),
                ('apellido', models.CharField(blank=True, db_column='Apellido', max_length=100, null=True)),
                ('cargo', models.CharField(blank=True, db_column='Cargo', max_length=20, null=True)),
                ('telefono', models.IntegerField(blank=True, db_column='Telefono', null=True)),
                ('correo', models.CharField(blank=True, db_column='Correo', max_length=100, null=True)),
                ('fecha_contratacion', models.DateField(blank=True, db_column='Fecha_Contratacion', null=True)),
                ('fecha_nacimiento', models.DateField(blank=True, db_column='Fecha_Nacimiento', null=True)),
            ],
            options={
                'db_table': 'empleados',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Pedidos',
            fields=[
                ('id_pedido', models.AutoField(db_column='Id_Pedido', primary_key=True, serialize=False)),
                ('fecha_pedido', models.DateTimeField(blank=True, db_column='Fecha_Pedido', null=True)),
            ],
            options={
                'db_table': 'pedidos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id_productos', models.AutoField(db_column='Id_Productos', primary_key=True, serialize=False)),
                ('nombre_prod', models.CharField(blank=True, db_column='Nombre_Prod', max_length=100, null=True)),
                ('precio_unitario', models.FloatField(blank=True, db_column='Precio_Unitario', null=True)),
                ('descripcion', models.CharField(blank=True, db_column='Descripcion', max_length=500, null=True)),
                ('tipo', models.CharField(blank=True, db_column='Tipo', max_length=100, null=True)),
                ('image_url', models.CharField(blank=True, db_column='Image_url', max_length=100, null=True)),
            ],
            options={
                'db_table': 'productos',
                'managed': False,
            },
        ),
    ]
