# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Clientes(models.Model):
    id_cliente = models.AutoField(db_column='Id_Cliente', primary_key=True)  # Field name made lowercase.
    contrasenha = models.CharField(db_column='Contrasenha', max_length=10, blank=True, null=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=100, blank=True, null=True)  # Field name made lowercase.
    apellido = models.CharField(db_column='Apellido', max_length=100, blank=True, null=True)  # Field name made lowercase.
    correo = models.CharField(db_column='Correo', max_length=100, blank=True, null=True)  # Field name made lowercase.
    direccion = models.CharField(db_column='Direccion', max_length=100, blank=True, null=True)  # Field name made lowercase.
    telefono = models.IntegerField(db_column='Telefono', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'clientes'


class DescuentoP(models.Model):
    id_productos = models.ForeignKey('Productos', models.DO_NOTHING, db_column='Id_Productos', blank=True, null=True)  # Field name made lowercase.
    descuento = models.IntegerField(db_column='Descuento', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'descuento_p'


class DetallesPedido(models.Model):
    id_pedido = models.ForeignKey('Pedidos', models.DO_NOTHING, db_column='Id_Pedido', blank=True, null=True)  # Field name made lowercase.
    id_productos = models.ForeignKey('Productos', models.DO_NOTHING, db_column='Id_Productos', blank=True, null=True)  # Field name made lowercase.
    cantidad = models.IntegerField(db_column='Cantidad', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'detalles_pedido'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Empleados(models.Model):
    id_empleado = models.AutoField(db_column='Id_Empleado', primary_key=True)  # Field name made lowercase.
    contrasenha = models.CharField(db_column='Contrasenha', max_length=10, blank=True, null=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=100, blank=True, null=True)  # Field name made lowercase.
    apellido = models.CharField(db_column='Apellido', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cargo = models.CharField(db_column='Cargo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    telefono = models.IntegerField(db_column='Telefono', blank=True, null=True)  # Field name made lowercase.
    correo = models.CharField(db_column='Correo', max_length=100, blank=True, null=True)  # Field name made lowercase.
    fecha_contratacion = models.DateField(db_column='Fecha_Contratacion', blank=True, null=True)  # Field name made lowercase.
    fecha_nacimiento = models.DateField(db_column='Fecha_Nacimiento', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'empleados'


class Pedidos(models.Model):
    id_pedido = models.AutoField(db_column='Id_Pedido', primary_key=True)  # Field name made lowercase.
    id_cliente = models.ForeignKey(Clientes, models.DO_NOTHING, db_column='Id_Cliente', blank=True, null=True)  # Field name made lowercase.
    id_empleado = models.ForeignKey(Empleados, models.DO_NOTHING, db_column='Id_Empleado', blank=True, null=True)  # Field name made lowercase.
    fecha_pedido = models.DateTimeField(db_column='Fecha_Pedido', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pedidos'


class Productos(models.Model):
    id_productos = models.AutoField(db_column='Id_Productos', primary_key=True)  # Field name made lowercase.
    nombre_prod = models.CharField(db_column='Nombre_Prod', max_length=100, blank=True, null=True)  # Field name made lowercase.
    precio_unitario = models.FloatField(db_column='Precio_Unitario', blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=500, blank=True, null=True)  # Field name made lowercase.
    tipo = models.CharField(db_column='Tipo', max_length=100, blank=True, null=True)  # Field name made lowercase.
    image_url = models.CharField(db_column='Image_url', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'productos'
