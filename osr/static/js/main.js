$(document).ready(function() {
  var controller = new slidebars();
  controller.init();

  $( '.hamburger' ).on( 'click', function ( event ) {

    if($(this).hasClass('is-active'))
		{
			$(this).removeClass('is-active');
		} else {
			$(this).addClass('is-active');
    }

    event.stopPropagation();
    event.preventDefault();

    controller.toggle( 'left-menu' );
  });



  $('.full-screen-tabele').click(function(e){
    $('.table').fullScreen();
    e.preventDefault();
  });

});
