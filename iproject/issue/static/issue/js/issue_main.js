//{
//  name: 'creator',
//  index: 'creator',
//  editable: true,
//  edittype: 'select',
//  editoptions: {
//      value: creatordata, dataEvents: [
//          {
//              type: 'change',
//              fn: function (e) {
//                  var str = "";
//                  var selectitem = $(e.target).val();
//                  var updata={'creator':selectitem};
//                  $.ajax({
//                      type:'post',
//                      url: '/iproject/issue/getselect',
//                      async: false,
//                      cache: false,
//                      datatype: 'json',
//                      data: updata,
//                      success: function (json) {
//                          if (json != null) {
//                              str = eval(json);
//                          }
//                      }
//                  });
//                  $("#jqgrid").jqGrid('setCell', "1", "owner", str)
//              }
//          }
//      ]
//  }
//    }


$('#taskall').on('click', '', function () {
    $('#taskopen').removeClass('active ');
    $('#taskall').addClass('active ');

});

$('#taskopen').on('click', '', function () {
    $('#taskall').removeClass('active ');
    $('#taskopen').addClass('active ');

});




