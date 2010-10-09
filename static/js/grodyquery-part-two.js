(function (global, $) {
    $(function(){
        var timer, savedWidth, savedHeight, win = $(window);
        
        if ((typeof grodyQuery == "undefined") || grodyQuery.nativeSupport)
            return;
        
        function diddleLinks () {
            clog("DIDDLED");
            $("." + grodyQuery.linkClass).remove();
            $("head").append(grodyQuery.getLinkHtml());
            if (timer) clearTimeout(timer);
        }
        
        win.resize(function(event){
            clog("resized");
            var width = win.width(), height = win.height();
            if (savedWidth !== width || savedHeight !== height) {
                if (timer) clearTimeout(timer);
                timer = setTimeout(diddleLinks, grodyQuery.refreshTimeout);
                savedWidth = width;
                savedHeight = height;
            }
        });
    });
}(this, jQuery));



