from fabric.api import env, run, sudo

def postgresql(database, file):
    owner = sudo("stat -c %%U `dirname %s`" % file)
    sudo("chown postgres `dirname %s`" % file)
    sudo("pg_dump %s > %s" % (database, file), user='postgres')
    sudo("chown %s `dirname %s` %s" % (owner, file, file))

class TmpDir(object):
    def __enter__(self):
        self.dir_name = run("mktemp -d")
        return self.dir_name
    
    def __exit__(self, type, value, traceback):
        sudo("rm -rf %s" % self.dir_name)
