import datetime
from os import path

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

def generate_name():
    hostname = run("hostname")
    date = datetime.datetime.now().isoformat('_')
    return "%s_%s" % (hostname, date)

def archive_dir(source_path, target_path, archive_name):
    file_name = path.join(target_path, "%s.tar" % archive_name)
    run('cd %s; tar c * > "%s"' % (source_path, file_name))
    return file_name

def compress(file_name):
    run('bzip2 -9 "%s"' % file_name)
    return "%s.bz2" % file_name
