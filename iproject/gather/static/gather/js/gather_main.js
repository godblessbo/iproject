$(document).ready(function () {

    jQuery("#gathergrid").jqGrid({
        url: '/iproject/gather/getGatherJoinInfo',
        datatype: "json",
        mtype: "post",
        height: "auto",
        jsonReader: {
            root: "rows", //root这里的值是rows，意味着它会读取json中的rows键的值，这个值就是真实的数据
            page: "page", //root这里的值是page，意味着它会读取json中的page键的值，当前页号     total: "total",//总的页数
            records: "records",//总记录数
            repeatitems: true,//如果设为false，则jqGrid在解析json时，会根据name来搜索对应的数据元素（即可以json中元素可以不按顺序）；而所使用的name是来自于colModel中的name设定。
            cell: "cell",
            id: "id",
            userdata: "userdata"
        },
        colNames: ['relationId', '姓名', '电话', '是否参与', '原因', 'Actions'],
        colModel: [

            {
                name: 'relationId',
                index: 'relationId',
                sortable: true,
                searchable: true,
                hidden: true
            },
            {
                name: 'userName',
                index: 'userName',
                align: 'center',
                sortable: true,
                searchable: true,
                width: 60
            },
            {
                name: 'phoneNumber',
                index: 'phoneNumber',
                align: 'center',
                sortable: true,
                searchable: true,
                width: 60
            },
            {
                name: 'isJoin',
                index: 'isJoin',
                sortable: true,
                editable: true,
                align: 'center',
                edittype: 'select',
                editoptions: {value: {'unknown': 'unknown', 'true': 'true', 'false': 'false'}},
                searchable: true,
                width: 60
            },
            {
                name: 'reason',
                index: 'reason',
                editable: true,
                align: 'left',
                edittype: 'textarea',
                sortable: true,
                searchable: true,
                width: 400
            },
            {
                name: 'act',
                index: 'act',
                sortable: false,
                searchable: false,
                width: 60
            }
        ],

        rowNum: 10,
        rowList: [10, 20, 30],
        pager: '#pjqgrid',
        sortname: "id",
        toolbarfilter: true,
        viewrecords: true,
        sortorder: "asc",
        gridComplete: function () {
            var ids = jQuery("#gathergrid").jqGrid('getDataIDs');
            for (var i = 0; i < ids.length; i++) {
                var cl = ids[i];
                //(" + cl + ",saveparameters)
                em = "<button class='btn btn-xs btn-default' data-original-title='Email' onclick=\"email(" + cl + ");\"><i class='fa fa-envelope'></i></button>";
                jQuery("#gathergrid").jqGrid('setRowData', ids[i], {
                    act: em
                });
            }
        },
        editurl: "/iproject/gather/dummyGatherJoinInfo",
        multiselect: false,
        autowidth: true
    });

    jQuery("#gathergrid").jqGrid('navGrid', "#pjqgrid", {
        edit: false,
        add: false,
        del: false,
        refresh: false,
        search: false
    });

    email = function (id) {
        showdialog()
    };

    //jQuery("#gathergrid").jqGrid('inlineNav', "#pjqgrid");
    /* Add tooltips */
    $('.navtable .ui-pg-button').tooltip({
        container: 'body'
    });


    showdialog = function () {
        $("#EmailModal").modal()
    };
    closedialog = function () {
        $("#EmailModal").modal("hide")
    };


    // remove classes
    $(".ui-jqgrid").removeClass("ui-widget ui-widget-content");
    $(".ui-jqgrid-view").children().removeClass("ui-widget-header ui-state-default");
    $(".ui-jqgrid-labels, .ui-search-toolbar").children().removeClass("ui-state-default ui-th-column ui-th-ltr");
    $(".ui-jqgrid-pager").removeClass("ui-state-default");
    $(".ui-jqgrid").removeClass("ui-widget-content");

    // add classes
    $(".ui-jqgrid-htable").addClass("table table-bordered table-hover");
    $(".ui-jqgrid-btable").addClass("table table-bordered table-striped");

    $(".ui-pg-div").removeClass().addClass("btn btn-sm btn-primary");
    $(".ui-icon.ui-icon-plus").removeClass().addClass("fa fa-plus");
    $(".ui-icon.ui-icon-pencil").removeClass().addClass("fa fa-pencil");
    $(".ui-icon.ui-icon-trash").removeClass().addClass("fa fa-trash-o");
    $(".ui-icon.ui-icon-search").removeClass().addClass("fa fa-search");
    $(".ui-icon.ui-icon-refresh").removeClass().addClass("fa fa-refresh");
    $(".ui-icon.ui-icon-disk").removeClass().addClass("fa fa-save").parent(".btn-primary").removeClass("btn-primary").addClass("btn-success");
    $(".ui-icon.ui-icon-cancel").removeClass().addClass("fa fa-times").parent(".btn-primary").removeClass("btn-primary").addClass("btn-danger");

    $(".ui-icon.ui-icon-seek-prev").wrap("<div class='btn btn-sm btn-default'></div>");
    $(".ui-icon.ui-icon-seek-prev").removeClass().addClass("fa fa-backward");

    $(".ui-icon.ui-icon-seek-first").wrap("<div class='btn btn-sm btn-default'></div>");
    $(".ui-icon.ui-icon-seek-first").removeClass().addClass("fa fa-fast-backward");

    $(".ui-icon.ui-icon-seek-next").wrap("<div class='btn btn-sm btn-default'></div>");
    $(".ui-icon.ui-icon-seek-next").removeClass().addClass("fa fa-forward");

    $(".ui-icon.ui-icon-seek-end").wrap("<div class='btn btn-sm btn-default'></div>");
    $(".ui-icon.ui-icon-seek-end").removeClass().addClass("fa fa-fast-forward");

});

$(window).on('resize.jqGrid', function () {
    $("#gathergrid").jqGrid('setGridWidth', $("#content").width());
});

