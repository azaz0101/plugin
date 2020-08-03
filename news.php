<html>
<head>
	<title>News Search</title>
	<style type="text/css">
		html,body{ height:100%; padding: 0; margin: 0 ;}
		div { width: 50%; height: 50%; float: left; }
		iframe { width: 100%; height: 100%; }
	</style>
</head>
<body>
<?php
echo "<div><iframe src='http://google.com/search?q=".$_GET["q"]." site:news.ltn.com.tw/news&igu=1'></iframe></div>";
echo "<div><iframe src='http://google.com/search?q=".$_GET["q"]." site:chinatimes.com&igu=1'></iframe></div>";
echo "<div><iframe src='http://google.com/search?q=".$_GET["q"]." site:udn.com&igu=1'></iframe></div>";
echo "<div><iframe src='http://google.com/search?q=".$_GET["q"]." site:ettoday.net/news&igu=1'></iframe></div>";
?>
</body>
</html>
