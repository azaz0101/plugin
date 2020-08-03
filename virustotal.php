<!DOCTYPE html>
<html>
<head>
	<title>PTT</title>
</head>
<body>
<p>
<?php
$url = $_GET["q"];
echo shell_exec("python3 analyze.py $url");
?>
</p>
</body>
</html>