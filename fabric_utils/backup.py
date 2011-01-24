from fabric.api import env, run, sudo

def postgresql(database, file):
    owner = sudo("stat -c %%U `dirname %s`" % file)
    sudo("chown postgres `dirname %s`" % file)
    sudo("pg_dump %s > %s" % (database, file), user='postgres')
    sudo("chown %s `dirname %s` %s" % (owner, file, file))
