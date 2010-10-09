

(function($){
    var fakeAtSign = / \[at\] /,
        realAtSign = "@";
  
    function fixProtectedEmail (index, oldValue) {
        return oldValue.replace(fakeAtSign, realAtSign);
    }
  
    $(function(){
        
        // PNGs
        if ($("body").is(".lt7")) {
            DD_belatedPNG.fix("img");
        }
    
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

  