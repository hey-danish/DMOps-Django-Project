

$(document).ready(function() {

  var r_columns, r_data;

  // Data retrieval Via Generic callAJAX Function
  callAJAX( "/kpt/hcpc/",
    {"X-CSRFToken": getCookie("csrftoken") },
    parameters={},
    'post',
    function(data){
      console.log(data)
      r_columns = data["columns"];
      r_data = data["data"];
  }, null, null );

   initializeDatatable ( r_columns )

   function initializeDatatable( r_columns ) {
     var markups = [{
      "mRender": function( data, type, row ){
          return '<a href="https://www.youtube.com/watch?v='+row[0]+'"' + 'id="'+ data + '">'+data+'</a>'+
  	  '<br><br><a href="https://img.youtube.com/vi/'+ row[0] +'/0.jpg" target="_blank"><h6>Thumbnail</h6></a>';
      },"aTargets":[1] ,
     }];
     var resp = createDataTable("#tbl_hcpc", r_columns );
     resp.create( "/kpt/hcpc/", "POST", [] );
     resp.action()
   }



});
