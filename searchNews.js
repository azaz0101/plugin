function searchNews()
{
// console.log('searchNews');
q = document.getElementById('query').value;
// s = '<!DOCTYPE html> \
// <html>\
// <head>\
// 	<title>News Search</title>\
// 	<style type="text/css">\
// 		html,body{ height:100%; padding: 0; margin: 0 ;}\
// 		div { width: 50%; height: 50%; float: left; }\
// 		iframe { width: 100%; height: 100%; }\
// 	</style>\
// </head>\
// <body>\
// <div><iframe src="http://google.com/search?q='+q+' site:news.ltn.com.tw&igu=1"></iframe></div>\
// <div><iframe src="http://google.com/search?q='+q+' site:chinatimes.com&igu=1"></iframe></div>\
// <div><iframe src="http://google.com/search?q='+q+' site:udn.com&igu=1"></iframe></div>\
// <div><iframe src="http://google.com/search?q='+q+' site:ettoday.net&igu=1"></iframe></div>\
// </body>\
// </html>\
// ';
// writeFile( path = 'news_search_result.html', object = s );
chrome.tabs.create({url:'localhost:8000/?q='+q});
// console.log('should open now');
}
document.getElementById('searchNews').onclick = searchNews;