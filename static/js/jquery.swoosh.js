(function ($){
    
//$.fx.interval = 5;

$.fn.swoosh = function (opts) {
    var animatedCoordinate, fixedCoordinate;
    opts = $.extend({}, $.fn.swoosh.defaults, opts);
    this.each(function(){
    
        var positions, innerWidth,
            i = 0,
            container = $(this),
            chips = container.find(opts.selector);
            
        if (chips.length > 0) {
            
            chips.css({
                opacity: 0
            });

            function floopy () {
                chips.eq(i)
                    .animate({opacity: 1.0}, 2000, "swing")
                    .delay(5000)
                    .queue(
                        function () {                                
                             i = (i + 1) % chips.length;
                             floopy();
                             $(this).dequeue();
                         }
                    )
                    .animate({opacity: 0.0}, 2000, "swing");
            }
            
            floopy();
            
            
            
            
        }
        
    });
}

$.fn.swoosh.defaults = {
    selector: ".swoosh",
    enterExitSpeed: 300,
    driftDistance: 200,
    driftSpeed: 4000
}
    
}(jQuery));