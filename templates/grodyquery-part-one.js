// from the fexcellent winpots of Awesomatorius III...
(function (global) {
    function getStyle(el, name){
        if (el.currentStyle) {
            return el.currentStyle[name];
        }
        else if (window.getComputedStyle) {
            return document.defaultView.getComputedStyle(el,null).
                getPropertyValue(name);
        }
    }
    
    
    var i, link, allLinks, links, grodyQuery,
        html = document.getElementsByTagName("html")[0],
        htmlBg = getStyle(html, "background-color") ||
            getStyle(html, "backgroundColor");

    grodyQuery = {
        linkClass: "totally-grody",
        nativeSupport: htmlBg === "rgb(0, 128, 0)" || htmlBg === "green",
        refreshTimeout: 100, // ms, that is
        // totally grody media query "parser" which only understands
        // width/min-width/max-width, and assumes everything is in pixels, and all
        // conditions are "and"-ed.
        testMediaQuery: function (query) {
            var results, i,
                rules = [],
                answer = true,
                width = document.documentElement.clientWidth,
                re = /\(\s*(?:(m(?:in|ax))-)?width\s*:\s*(\d+)([a-z]+)\s*\)/g;
            while ((results = re.exec(query)) != null) {
                rules.push({
                    minMax: results[1],
                    scale: results[2],
                    units: results[3]
                });
            }
            for (i=0; i<rules.length; i++) {
                answer = answer &&
                    (rules[i].minMax == "min" && rules[i].scale <= width) ||
                    (rules[i].minMax == "max" && rules[i].scale >= width) ||
                    (rules[i].minMax == ""    && rules[i].scale === width);
            }
            return answer;
        },
        getLinkHtml: function () {
            var link, allLinks, links, linkHtml = "";
            if (grodyQuery.nativeSupport) { return ""; }
            allLinks = document.getElementsByTagName("link");
            links = [];
            for (i=0; i < allLinks.length; i++) {
                link = allLinks[i];
                if (link.rel && /\bstylesheet\b/i.test(link.rel) &&
                        link.media && /^only screen and/.test(link.media)) {
                    links.push({
                        media: link.media,
                        href: link.href
                    });
                }
            }
            for (i=0; i < links.length; i++) {
                if (grodyQuery.testMediaQuery(links[i].media)) {
                    linkHtml += '<link class="' + grodyQuery.linkClass +
                                '" rel="stylesheet" media="screen" href="' +
                                links[i].href + '" type="text/css" />\n';
                }
            }            
            return linkHtml;
        }
    };
    
    document.write(grodyQuery.getLinkHtml());

    
    global.grodyQuery = grodyQuery;

}(this));




if (typeof console != "undefined") {
    clog = function (msg) {console.log(msg);}
}
else {
    clog = function (msg) {
        $("body").append(msg + "\n");
    }
}






