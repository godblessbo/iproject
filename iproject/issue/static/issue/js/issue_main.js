
$('#taskall').on('click', '', function () {
    $('#taskopen').removeClass('active ');
    $('#taskall').addClass('active ');

});

$('#taskopen').on('click', '', function () {
    $('#taskall').removeClass('active ');
    $('#taskopen').addClass('active ');
});

//在restoreGrid之后执行，successfuc在之前执行，编辑后保存页面值未变为编辑后的值，可以用来判断是否保存成功再决定是否显示
saveparameters = {
    "successfunc": null,

    "extraparam": {},
    "aftersavefunc": function (response) {
        $.ajax({
                      type:'post',
                      url: '/iproject/issue/aftersave',
                      async: false,
                      cache: false,
                      datatype: 'json',
                      data: "",
                      success: function (json) {
                          if (json != null) {
                              str = eval(json);
                          }
                      }
                  });
    },
    "errorfunc": null,
    "afterrestorefunc": null,
    "restoreAfterError": true,
    "mtype": "POST"
};

addparameters={
    rowID : "0",
    initdata : {oper:"add"},
    position :"first",
    useDefValues : false,
    useFormatter : false,
    addRowParams : {extraparam:{}}
};


