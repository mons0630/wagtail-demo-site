# wagtail-demo-site

This is a demo site for the [Wagtail CMS](https://wagtail.io). It is being used to support experiments with deploying Python web applications to OpenShift.

## Environment variables

By default the Wagtail site is configured to run with a development configuration. If you want to run it in a more production like environment, then you will need to set the following environment variables.

* ``DJANGO_SETTINGS_MODULE`` - Set this to ``demo.settings.production`` for a production system.
* ``DJANGO_SECRET_KEY`` - Set this to a Django secret key value unique to the production environment.
* ``OPENSHIFT_DATABASE_TYPE`` - Set this to the type of SQL database being used. Must be either ``MySQL`` or ``PostgreSQL``. The appropriate environment variables for the database type should then also be set.

If using the MySQL database, the database specific environment variables are as follows. These must match what the MySQL database was set up with.

* ``OPENSHIFT_MYSQL_DB_NAME`` - The name of the MySQL database.
* ``OPENSHIFT_MYSQL_DB_USERNAME`` - The name of the MySQL database user who has access to the named database.
* ``OPENSHIFT_MYSQL_DB_PASSWORD`` - The password for accessing the named database as the specified user.
* ``OPENSHIFT_MYSQL_DB_HOST`` - The name of the host the MySQL database is running on.
* ``OPENSHIFT_MYSQL_DB_PORT`` - The port number on the host that the MySQL database is listening on for connections.

If using the PostgreSQL database, the database specific environment variables are as follows. These must match what the PostgreSQL database was set up with.

* ``OPENSHIFT_POSTGRESQL_DB_NAME`` - The name of the PostgreSQL database.
* ``OPENSHIFT_POSTGRESQL_DB_USERNAME`` - The name of the PostgreSQL database user who has access to the named database.
* ``OPENSHIFT_POSTGRESQL_DB_PASSWORD`` - The password for accessing the named database as the specified user.
* ``OPENSHIFT_POSTGRESQL_DB_HOST`` - The name of the host the PostgreSQL database is running on.
* ``OPENSHIFT_POSTGRESQL_DB_PORT`` - The port number on the host that the PostgreSQL database is listening on for connections.

## Database initialisation

Once you have the Wagtail CMS deployed the first time, you will need to initialise the database and create a super user account for the Django admin.

```
python manage.py migrate
python manage.py createsuperuser
```

If using the ``warpdrive`` based Source to Image (S2I) builder, the commands you should run if launching the commands from outside of the container are:

```
warpdrive exec python manage.py migrate
warpdrive exec python manage.py createsuperuser
```

Use of ``warpdrive exec`` ensures that correct environment as required by the application is set up before executing the commands.

Once initialised, you can access if ``/admin`` URL for the site, log in and start creating pages.



