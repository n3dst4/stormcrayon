(function (global, $) {
    $(function(){
        var timer;
        
        if ((typeof grodyQuery == "undefined") || grodyQuery.nativeSupport) return;
       
        $(window).resize(function(){
            //clog("resized");
            if (timer) clearTimeout(timer);
            timer = setTimeout(diddleLinks, grodyQuery.refreshTimeout);
        });
        
    });
}(this, jQuery));

        function diddleLinks () {
            var grodyLinks;
            clog("diddled");
            grodyLinks = $("." + grodyQuery.linkClass);
            $("head").append(grodyQuery.getLinkHtml());
            grodyLinks.remove();
        }


