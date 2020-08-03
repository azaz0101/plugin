function searchTFC() 
{
q = document.getElementById('query').value;
q = encodeURI(q);
document.getElementById('tfcres').innerHTML = '<iframe width="500" height="500" src="http://localhost:8000/searchtfc.php?q=' + q + '"></iframe>';
}

function searchNews()
{
q = document.getElementById('query').value;
chrome.tabs.create({url:'localhost:8000/news.php?q='+q});
}

function pttAnalyze() {
	var result = "Hmmm....";
	chrome.tabs.query({active: true, lastFocusedWindow: true}, tabs => {
    	let url = tabs[0].url;
    	console.log(url);
    	regex = RegExp('https://www.ptt.cc/bbs/[A-Za-z0-9/.]*.html')
    	if(regex.test(url))
    	{
    		document.getElementById('pttResult').innerHTML = '<iframe src="http://localhost:8000/ptt.php?q='+url.match(regex)[0]+'"></iframe>';
    	}else{
    		document.getElementById('pttResult').innerHTML = "ERROR, you're probably not on ptt, what are you trying to do?"
    	}

	});
}

function virustotalQuery() {
	url = document.getElementById('malurl').value;
	if(url){
		document.getElementById('malResult').innerHTML = '<iframe src="http://localhost:8000/virustotal.php?q='+url+'"></iframe>';
	}else{
		document.getElementById('malResult').innerHTML = "You did not enter the url!"
	}
	
}
document.getElementById('search').onclick = searchTFC;
document.getElementById('searchNews').onclick = searchNews;
document.getElementById('ptt').onclick = pttAnalyze;
document.getElementById('malsearch').onclick = virustotalQuery;