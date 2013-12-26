#! /bin/bash

### BEGIN INIT INFO
# Provides:          selenium-server
# Required-Start:    $local_fs $remote_fs $network $named $time
# Required-Stop:     $local_fs $remote_fs $network $named $time
# Should-Start:      $syslog
# Should-Stop:       $syslog
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: Starts selenium server for testing
# Description:       Selenium server for functional testing
### END INIT INFO

. /lib/lsb/init-functions

JAVA=java
SELENIUM=/junhui/automated_script/selenium-server-standalone-2.25.0.jar
BMODE=firefoxchrome
PORT=4444
LOG=selenium.log
PIDFILE=selenium.pid
DISPLAY=:0.0

pidof_server() {
    if [ -e "$PIDFILE" ]; then
        if pidofproc java | tr ' ' '\n' | grep -w $(cat $PIDFILE); then
            return 0
        fi
    fi
    return 1
}


case $1 in
    start)
        DISPLAY=$DISPLAY $JAVA -jar $SELENIUM \
            -timeout 180 -port $PORT -forcedBrowserModeRestOfLine $BMODE > $LOG &
        log_success_msg "Starting Selenium server!" "selenium-server"
        echo $! > $PIDFILE
    ;;
    stop)
        SELPID=`cat $PIDFILE` && kill $SELPID
        log_success_msg "Stopping Selenium server!" "selenium-server"
    ;;
    status)
        PID=$(pidof_server) || true
        if [ -n "$PID" ]; then
            echo "Selenium Server is running (pid $PID)."
            exit 0
        else
            echo "Selenium Server is NOT running."
            exit 1
        fi
    ;;
    *)
        echo "Usage: selenium-server.sh {start|stop|status}"
        exit 1
    ;;
esac
