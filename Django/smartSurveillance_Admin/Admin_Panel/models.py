# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Activities(models.Model):
    acid = models.AutoField(db_column='ACID', primary_key=True)  # Field name made lowercase.
    activity_name = models.CharField(db_column='ACTIVITY_NAME', max_length=50)  # Field name made lowercase.
    duty_rostrum = models.ForeignKey('DutyRostrum', models.DO_NOTHING, db_column='DUTY_ROSTRUM_ID')  # Field name made lowercase.
    vioation = models.ForeignKey('Vioation', models.DO_NOTHING, db_column='VIOATION_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ACTIVITIES'
        
    def __str__(self):
        return self.activity_name


class Attendance(models.Model):
    aid = models.AutoField(db_column='AID', primary_key=True)  # Field name made lowercase.
    employee = models.ForeignKey('Employee', models.DO_NOTHING, db_column='EMPLOYEE_ID')  # Field name made lowercase.
    status = models.BooleanField(db_column='STATUS')  # Field name made lowercase.
    attendance_datetime = models.DateTimeField(db_column='ATTENDANCE_DATETIME')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ATTENDANCE'
        
    def __str__(self):
        return self.employee.first_name


class Building(models.Model):
    bid = models.AutoField(db_column='BID', primary_key=True)  # Field name made lowercase.
    bname = models.CharField(db_column='BNAME', max_length=25)  # Field name made lowercase.
    region = models.ForeignKey('Region', models.DO_NOTHING, db_column='REGION_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BUILDING'
        
    def __str__(self):
        return self.bname


class Department(models.Model):
    did = models.AutoField(db_column='DID', primary_key=True)  # Field name made lowercase.
    dname = models.CharField(db_column='DNAME', max_length=25)  # Field name made lowercase.
    building = models.ForeignKey(Building, models.DO_NOTHING, db_column='BUILDING_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DEPARTMENT'
        
    def __str__(self):
        return self.dname


class DutyRostrum(models.Model):
    drid = models.AutoField(db_column='DRID', primary_key=True)  # Field name made lowercase.
    employee = models.ForeignKey('Employee', models.DO_NOTHING, db_column='EMPLOYEE_ID')  # Field name made lowercase.
    title = models.ForeignKey('Title', models.DO_NOTHING, db_column='TITLE_ID')  # Field name made lowercase.
    uniform = models.ForeignKey('Uniform', models.DO_NOTHING, db_column='UNIFORM_ID')  # Field name made lowercase.
    shift = models.ForeignKey('Shift', models.DO_NOTHING, db_column='SHIFT_ID')  # Field name made lowercase.
    wages = models.ForeignKey('Wage', models.DO_NOTHING, db_column='WAGES_ID')  # Field name made lowercase.
    zone = models.ForeignKey('Zone', models.DO_NOTHING, db_column='ZONE_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DUTY_ROSTRUM'
        
    def __str__(self):
        return self.employee.first_name


class Employee(models.Model):
    eid = models.AutoField(db_column='EID', primary_key=True)  # Field name made lowercase.
    first_name = models.CharField(db_column='FIRST_NAME', max_length=20)  # Field name made lowercase.
    last_name = models.CharField(db_column='LAST_NAME', max_length=20)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=50)  # Field name made lowercase.
    phone_number = models.CharField(db_column='PHONE_NUMBER', max_length=15)  # Field name made lowercase.
    dob = models.DateField(db_column='DOB')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EMPLOYEE'
        
    def __str__(self):
        return self.first_name


class Errors(models.Model):
    erid = models.AutoField(db_column='ERID', primary_key=True)  # Field name made lowercase.
    activity = models.ForeignKey(Activities, models.DO_NOTHING, db_column='ACTIVITY_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ERRORS'
        
    def __str__(self):
        return self.activity.activity_name


class Region(models.Model):
    rid = models.AutoField(db_column='RID', primary_key=True)  # Field name made lowercase.
    rname = models.CharField(db_column='RNAME', max_length=25)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'REGION'
        
    def __str__(self):
        return self.rname


class Shift(models.Model):
    sid = models.AutoField(db_column='SID', primary_key=True)  # Field name made lowercase.
    start_time = models.TimeField(db_column='START_TIME')  # Field name made lowercase.
    end_time = models.TimeField(db_column='END_TIME')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SHIFT'
        
    def __str__(self):
        return str(self.start_time) + " to " + str(self.end_time)


class Title(models.Model):
    tid = models.AutoField(db_column='TID', primary_key=True)  # Field name made lowercase.
    tname = models.CharField(db_column='TNAME', max_length=25)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TITLE'
        
    def __str__(self):
        return self.tname


class TitleViolation(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.ForeignKey(Title, models.DO_NOTHING, db_column='TITLE_ID')  # Field name made lowercase.
    vioation = models.ForeignKey('Vioation', models.DO_NOTHING, db_column='VIOATION_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TITLE_VIOLATION'
        
    def __str__(self):
        return self.title.tname


class Uniform(models.Model):
    uid = models.AutoField(db_column='UID', primary_key=True)  # Field name made lowercase.
    type = models.CharField(db_column='TYPE', max_length=25)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UNIFORM'
        
    def __str__(self):
        return self.type


class Vioation(models.Model):
    vid = models.AutoField(db_column='VID', primary_key=True)  # Field name made lowercase.
    vioation_name = models.CharField(db_column='VIOATION_NAME', max_length=50)  # Field name made lowercase.
    vioation_description = models.TextField(db_column='VIOATION_DESCRIPTION')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VIOATION'
        
    def __str__(self):
        return self.vioation_name


class Wage(models.Model):
    wid = models.AutoField(db_column='WID', primary_key=True)  # Field name made lowercase.
    wages_type = models.CharField(db_column='WAGES_TYPE', max_length=25)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WAGE'
        
    def __str__(self):
        return self.wages_type


class Zone(models.Model):
    zid = models.AutoField(db_column='ZID', primary_key=True)  # Field name made lowercase.
    zone_number = models.IntegerField(db_column='ZONE_NUMBER')  # Field name made lowercase.
    department = models.ForeignKey(Department, models.DO_NOTHING, db_column='DEPARTMENT_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ZONE'
        
    def __str__(self):
        return str(self.zone_number)


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
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
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


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
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


class Sysdiagrams(models.Model):
    name = models.CharField(max_length=128)
    principal_id = models.IntegerField()
    diagram_id = models.AutoField(primary_key=True)
    version = models.IntegerField(blank=True, null=True)
    definition = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sysdiagrams'
        unique_together = (('principal_id', 'name'),)
