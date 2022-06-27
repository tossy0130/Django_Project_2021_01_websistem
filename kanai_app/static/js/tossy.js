$(document).ready(function() {

   //*********** */ ドロップダウンメニュー ************

   $(window).resize(function(){
       if ($(window).width() >= 980){	
   
        
         $(".navbar .dropdown-toggle").hover(function () {
            $(this).parent().toggleClass("show");
            $(this).parent().find(".dropdown-menu").toggleClass("show"); 
          });
   
        
        
         $( ".navbar .dropdown-menu" ).mouseleave(function() {
           $(this).removeClass("show");  
         });
     
    
       }	
   });  
     
});



