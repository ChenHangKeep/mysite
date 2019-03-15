var searchvisible = 0;

$("#search-menu").click(function(e){ 
    //This stops the page scrolling to the top on a # link.
    e.preventDefault();

    var val = $('#search-icon');
    if(val.hasClass('ion-ios-search-strong')){
        val.addClass('ion-ios-close-empty');
        val.removeClass('ion-ios-search-strong');
    }
    else{
         val.removeClass('ion-ios-close-empty');
        val.addClass('ion-ios-search-strong');
    }
    