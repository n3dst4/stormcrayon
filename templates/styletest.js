// from the fexcellent winpots of Awesomatorius III...

function getStyle(el, name){
    var val;
    if (el.currentStyle) {
        val = el.currentStyle[name];
    }
    else if (window.getComputedStyle) {
        val = document.defaultView.getComputedStyle(el,null).getPropertyValue(name);
    }
    return val;
}

var html = document.getElementsByTagName("html")[0],
    htmlBg = getStyle(html, "background-color") || getStyle(html, "backgroundColor"),
    queriesSupported = htmlBg === "rgb(0, 128, 0)" || htmlBg === "green";

if ( ! queriesSupported) {
    if (document.documentElement.clientWidth > 600) {
        document.write('<link rel="stylesheet" media="screen" href="/static/css/large.css">');
    }
    else {
        document.write('<link rel="stylesheet" media="screen" href="/static/css/small.css">');
    }
}
