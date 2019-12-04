
var elementTop = $('.nav').offset().top;
$(window).scroll(function(){
	if ($(window).scrollTop() >= elementTop) {
		$('body').addClass('nav-fixed');
	}else{
		$('body').removeClass('nav-fixed');
	}
});

$('.btn-menu').on('click', function(){
	$('.nav').toggleClass('nav-menuR');
});