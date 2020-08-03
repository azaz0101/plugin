<!DOCTYPE html>
<html>
<head>
	<title>PTT</title>
</head>
<body>
<p>
<?php
// echo shell_exec("python analyze.py $_GET["q"]")
$url = $_GET["q"];
echo shell_exec("echo $url");
?>
</p>
</body>
</html>