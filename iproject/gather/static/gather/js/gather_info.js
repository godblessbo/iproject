var GatherInfo = function () {

    jQuery("#gather_info").jqGrid({
        url: '/iproject/gather/getgrid?grid=getGatherInfo',
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
        colNames: ['id', 'creator', 'name', 'desp', 'notes', 'startTime', 'endTime', 'place', 'eat', 'sleep', 'budget', 'summary', 'Actions'],
        colModel: [
            {
                name: 'id',
                index: 'id',
                sortable: true,
                searchable: true,
                hidden: true
            },
            {
                name: 'creator',
                index: 'creator',
                align: 'left',
                sortable: true,
                searchable: true
            },
            {
                name: 'name',
                index: 'name',
                align: 'left',
                formatter: "showlink",
                formatoptions: {
                    baseLinkUrl: "/iproject/gather/linkurl?link=getGatherJoinInfo",
                    target: "_blank",
                    idName: 'id'
                },
                sortable: true,
                searchable: true
            },
            {
                name: 'desp',
                index: 'desp',
                sortable: true,
                editable: true,
                align: 'left',
                edittype: 'select',
                editoptions: {value: {'unknown': 'unknown', 'true': 'true', 'false': 'false'}},
                searchable: true
            },
            {
                name: 'notes',
                index: 'notes',
                align: 'left',
                sortable: true,
                searchable: true
            },
            {
                name: 'startTime',
                index: 'startTime',
                align: 'left',
                sortable: true,
                searchable: true
            },
            {
                name: 'endTime',
                index: 'endTime',
                align: 'left',
                sortable: true,
                searchable: true
            },
            {
                name: 'place',
                index: 'place',
                align: 'left',
                sortable: true,
                searchable: true
            },
            {
                name: 'eat',
                index: 'eat',
                align: 'left',
                sortable: true,
                searchable: true
            },
            {
                name: 'sleep',
                index: 'sleep',
                align: 'left',
                sortable: true,
                searchable: true
            },
            {
                name: 'budget',
                index: 'budget',
                editable: true,
                align: 'left',
                edittype: 'textarea',
                sortable: true,
                searchable: true
            },
            {
                name: 'summary',
                index: 'summary',
                editable: true,
                align: 'left',
                edittype: 'textarea',
                sortable: true,
                searchable: true
            },
            {
                name: 'act',
                index: 'act',
                sortable: false,
                searchable: false
            }
        ],

        rowNum: 10,
        rowList: [10, 20, 30],
        pager: '#page_gather_info',
        sortname: "id",
        toolbarfilter: true,
        viewrecords: true,
        sortorder: "asc",
        gridComplete: function () {
            var ids = jQuery("#gather_info").jqGrid('getDataIDs');
            for (var i = 0; i < ids.length; i++) {
                var cl = ids[i];
                em = "<button class='btn btn-xs btn-default' data-original-title='Email' onclick=\"email(" + cl + ");\"><i class='fa fa-envelope'></i></button>";
                jQuery("#gather_info").jqGrid('setRowData', ids[i], {
                    act: em
                });
            }
        },
        editurl: "/iproject/gather/dummygrid?grid=dumm",
        multiselect: false,
        autowidth: true
    });

    jQuery("#gather_info").jqGrid('navGrid', "#page_gather_info", {
        edit: false,
        add: false,
        del: false,
        refresh: false,
        search: false
    });

    //jQuery("#gathergrid").jqGrid('inlineNav', "#pjqgrid");
    /* Add tooltips */
    $('.navtable .ui-pg-button').tooltip({
        container: 'body'
    });

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

};

$(window).on('resize.jqGrid', function () {
    $("#gather_info").jqGrid('setGridWidth', $("#content").width());
});

$(function () {
    GatherInfo();
});