<?php
        $query = $_GET['q'];
        $cmd = '/usr/bin/python -W ignore /var/www/search.py -q '.$query;
        $resp = shell_exec($cmd);
        echo $resp;
?>
