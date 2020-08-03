<!DOCTYPE html>
<html>
<head>
	<title>blabla</title>
</head>
<body>
<?php
$query = $_GET['q'];
// echo $query;
$cmd = "python3 searchtfc.py -q \"$query\"";
//echo $cmd;
echo shell_exec($cmd);
?>
</body>
</html>
