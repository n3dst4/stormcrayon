

(function($){

 





 



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

jQuery(function(){
  if ($("body").is(".lt7")) {
    DD_belatedPNG.fix("img");
  }
});
  