import time
from time import strftime,gmtime
from fabric.api import *
from fabric.contrib.console import confirm
from fabric.colors import *
import sys, os, re

env.warn_only = True
env.disable_known_hosts = True
env.key_filename = 'id_rsa'
env.user = 'root'


repo_server = '192.168.100.55'
big_k4 = '192.168.100.192'
work = '192.168.3.57'
iter = ''
svn_import_source_path = ''
svn_repos='/opt/svnrepos/repos/'

def init(para_iter, para_svn_path):
    global iter, svn_import_source_path,strftime,endtime
    #iter = prompt('what iteration?', default='1')
    #svn_import_source_path = prompt('what source path svn repository import?', default='/adddata/cycle1')
    iter=para_iter
    svn_import_source_path=para_svn_path
    local('date > spend_time.log')
    local('echo cycle %s' % iter)
    local('echo start time is %s' % strftime('%Y-%m-%d %H:%M:%S',time.gmtime()))


@hosts(repo_server)
def s1():
#def update_repo():
    local('echo "start scm repository update at " >> spend_time.log')
    starttime=strftime('%Y-%m-%d %H:%M:%S',time.gmtime())
    local('echo %s >> spend_time.log' % starttime)
    global iter, svn_import_source_path
    with cd("/junhui/scripts/repos_scripts/"):
#    with cd("/opt/svnrepos/sync_repos/"):
        result1=run("bash scm_sync.sh")
        print "scm result result failed status is %s" % result1.failed
        print "scm result is %s " % result1.return_code
        if result1.failed:
            print result1.failed
            local('echo "end scm repository update at " >> spend_time.log')
            endtime=strftime('%Y-%m-%d %H:%M:%S',time.gmtime())
            local('echo %s >> spend_time.log' % endtime)
            local("mail -s 'cycle %s has error in script running' liujunhui@cn-acg.com < spend_time.log" % iter)
            abort("some erorors in update cycle in scm sync %s" % iter)

        result2=run("bash svn_import.sh %s %s" % (svn_import_source_path, iter))
        print "scm import  result is %s " % result2.return_code
        print "scm import status is %s" % result2.failed
        if result2.failed:
            local('echo "end scm repository update, svn import  at " >> spend_time.log')
            endtime=strftime('%Y-%m-%d %H:%M:%S',time.gmtime())
            local('echo %s >> spend_time.log' % endtime)
            local("mail -s 'cycle %s has error in script running' liujunhui@cn-acg.com < spend_time.log" % iter)
            abort("some erorors in update cycle in svn import %s" % iter)
        result3=run("bash calculate_version_of_repos.sh %s %s" % (iter, svn_repos))
        print "calculate repos versions  result is %s " % result3.return_code
        print "calculate repos versions status is %s" % result3.failed
        if result3.failed:
            local('echo "end calculate scm repository version at " >> spend_time.log')
            endtime=strftime('%Y-%m-%d %H:%M:%S',time.gmtime())
            local('echo %s >> spend_time.log' % endtime)
            local("mail -s 'cycle %s has error in script running in calculate versions' liujunhui@cn-acg.com < spend_time.log" % iter)
            abort("some erorors in update cycle %s in calculate" % iter)
    pass

    endtime=strftime('%Y-%m-%d %H:%M:%S',time.gmtime())
    local('echo "end scm repository update at " >> spend_time.log')
    local('echo %s >> spend_time' % endtime)

@hosts(big_k4)
def s2():
#def moniter_k4():

    with cd("/root/i44moniter"):
        result4=run("bash du_partition.sh %s begin" % iter )
        if result4.failed:
            local('echo "end du krugle appliance at " >> spend_time.log')
            endtime=strftime('%Y-%m-%d %H:%M:%S',time.gmtime())
            local('echo %s >> spend_time.log' % endtime)
            local("mail -s 'cycle %s has error in script running in du krugle appliance ' liujunhui@cn-acg.com < spend_time.log" % iter)
            abort("some erorors in update cycle  %s in s2 task du partitions" % iter)
    pass

@hosts(work)
def s3():
#def update_hub():
    local('echo "begin update hub" >> spend_time.log')

    starttime=strftime('%Y-%m-%d %H:%M:%S',time.gmtime())
    local('echo %s >> spend_time.log' % starttime)
    global iter
    env.user = 'huangkun'
    with cd("/home/huangkun/i44test/junhui/automated_script"):
        run("whoami")
        #run("python krugle_junhui.py %s" % iter)
        update_result=run("python krugle_junhui.py %s" % iter)
        if update_result.failed:
            local("mail -s 'cycle %s has error in script running' liujunhui@cn-acg.com" % iter)
            abort("some erorors in update cycle %s" % iter)
    pass

    local('echo "end update at " >> spend_time.log')

    endtime=strftime('%Y-%m-%d %H:%M:%S',time.gmtime())
    local('echo %s >> spend_time.log' % endtime)

@hosts(big_k4)
def s4():
#def moniter_k4():
    env.user = 'root'
    global iter
    with cd("/root/i44moniter"):
        run("bash du_partition.sh %s end" % iter)
        get("/root/i44moniter/du_log", "./monitor_result/du_log_%s.log" % iter)
    pass
