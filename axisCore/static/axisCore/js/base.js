$(document).ready(function(){
    var prevScrollpos = window.pageYOffset;
    window.onscroll = function() {
    var currentScrollPos = window.pageYOffset;
      if (prevScrollpos > currentScrollPos) {
        document.getElementById("axisNavbar").style.top = "0";
      } else {
        document.getElementById("axisNavbar").style.top = "-50px";
      }
      prevScrollpos = currentScrollPos;
    }


    $(document).on('click','.uploadPostButton',function(){
      document.getElementById('overlapContentPage').style.display='block';
      document.getElementById('uploadPostForm').style.display='block';
      document.getElementById('axisMenu').style.display='none';
      document.body.style.overflow = "hidden";
      document.getElementById("axisNavbar").style.top = "0";
      console.log("Button Pressed ");
      //alert("Button Pressed");

        //$.ajax({
        //    type:'POST',
        //    url:'',
        //    data: {postId:postId,reaction:1,buttonValue:buttonValue,aStatus:aStatus},
        //    success:function(response){
        //    }
        //});
     });
     $(document).on('click','.uploadPostFormCloseButton',function(){
       document.getElementById('overlapContentPage').style.display='none';
       document.getElementById('uploadPostForm').style.display='none';
       document.getElementById('axisMenu').style.display='block';
       document.body.style.overflow = "scroll";
       //document.getElementById("leoNavbar").style.top = "0";
       //alert("Button Pressed");
       //console.log("Button Pressed");

         //$.ajax({
         //    type:'POST',
         //    url:'',
         //    data: {postId:postId,reaction:1,buttonValue:buttonValue,aStatus:aStatus},
         //    success:function(response){
         //    }
         //});
      });


});
