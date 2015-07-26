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

////在restoreGrid之后执行，successfuc在之前执行，编辑后保存页面值未变为编辑后的值，可以用来判断是否保存成功再决定是否显示
//saveparameters = {
//    "successfunc": null,
//    "url": '/iproject/issue/dummy',
//    "extraparam": {},
//    "aftersavefunc": function (response) {
//        alert('saved');
//    },
//    "errorfunc": null,
//    "afterrestorefunc": null,
//    "restoreAfterError": true,
//    "mtype": "POST"
//};



