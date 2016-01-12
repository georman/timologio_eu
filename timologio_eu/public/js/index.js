(function($){

	$.fn.rotate = function(){

		return this.each(function(){

			var el = $(this);
			var array = [];

			$.each(el.text().split(','), function(key, value) {
				array.push(value);
			});

			el.text(array[0]);

			var rotate = function(){
				if(el.find(".back").length > 0) {
	              el.html(el.find(".back").html())
	            }
	          
	            var initial = el.text()
	            var index = $.inArray(initial, array)
	            if((index + 1) == array.length) index = -1
   
	            el.html("");
	            $("<span class='front'>" + initial + "</span>").appendTo(el);
	            $("<span class='back'>" + array[index + 1] + "</span>").appendTo(el);
	            el.wrapInner("<span class='rotating' />").find(".rotating").hide().addClass("flip up").show().css({
	              "-webkit-transform": " rotateX(180deg)",
	              "-moz-transform": " rotateX(180deg)",
	              "-o-transform": " rotateX(180deg)",
	              "transform": " rotateX(180deg)"
	            });
			};

		setInterval(rotate, 2000);
		});

	};

})(window.jQuery);

$('.rotate').rotate();