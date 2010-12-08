

(function($){
    var kaboom,
        fakeAtSign = / \[at\] /,
        realAtSign = "@";
  
    function fixProtectedEmail (index, oldValue) {
        return oldValue.replace(fakeAtSign, realAtSign);
    }
    
    function alignKaboom() {
        var activeA = $(".kaboom"),
            target = activeA.offset();
        kaboom.offset({
            top: target.top - kaboom.height()/2 + activeA.height()/2,
            left: target.left - kaboom.width()/2 + activeA.width()/2
        });        
    }
  
    $(function(){
        
        // PNGs
        // using twinhelix iepngfix for now
        //if ($("body").is(".lt7")) {
        //    DD_belatedPNG.fix("img, div.nav-block, div.aura");
        //}
    
        // Email addresses
        $(".protected-email")
            .attr("href", fixProtectedEmail)
            .html(fixProtectedEmail);
      
        // Header rollovers
        $("#super-links").delegate("a", "mouseenter", function (event) {
            $(this).find("img").attr("src", "/static/images/external_o.png");
        }).
        delegate("a", "mouseleave", function (event) {
            $(this).find("img").attr("src", "/static/images/external.png");
        });
        
        // fancyboxes
        $("div.linkette a").map(function(){
            return $(this).attr("href").match(/\.(?:png|gif|jpg)$/)?
                this : undefined;
        }).fancybox();
        
        // align kaboom graphic with selected nav item
        kaboom = $("#kaboom");
        alignKaboom();
        kaboom.css("visibility", "visible");
        $(window).resize(alignKaboom);
        
    
    });
})(window.jQuery);



window.log = function(){
    log.history = log.history || []; 
    log.history.push(arguments);
    if(this.console){
        console.log( Array.prototype.slice.call(arguments) );
    }
};

/* This is part of Paul Irish's boilerplate, but I'm unconvinced.
(function(doc){
  var write = doc.write;
  doc.write = function(q){ 
    log('document.write(): ',arguments); 
    if (/docwriteregexwhitelist/.test(q)) write.apply(doc,arguments);  
  };
})(document);
//*/

  