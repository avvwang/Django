$(document).ready(function () {
    module()
    // $('#example').DataTable({
    // serverSide: true,  //启用服务器端分页
    // "serverSide": true,
    // ajax: {
    //     "type": "POST",
    //     "contentType": 'application/json; charset=UTF-8',
    //     "url": "http://127.0.0.1:8000/core/movies",
    //     "dataSrc": function (json) {
    //         for (var i = 0, ien = json.data.length; i < ien; i++) {
    //             console.log(json.data)
    //             json.data[i][1] = '<input value=' + json.data[i][1] + ">";
    //         }
    //         return json.data;
    //     },
    //     // ajax: function (data, callback, settings) {
    //
    //     data: function (d) {
    //         var str = {
    //             "draw": d.draw,
    //             "start": d.start,
    //             "length": d.length,
    //             "search": d.search.value
    //         };
    //         return JSON.stringify(str);
    //     },
    // }
    // })
})
;

function main() {
    $.ajax({
        url: "movies",
        typr: "post",
        data: {"code": 200},
        success: function (data) {

        },
        error: function () {

        }

    })

}

function module() {
    //提示信息
    var lang = {
        "sProcessing": "处理中...",
        "sLengthMenu": "每页 _MENU_ 项",
        "sZeroRecords": "没有匹配结果",
        "sInfo": "当前显示第 _START_ 至 _END_ 项，共 _TOTAL_ 项。",
        "sInfoEmpty": "当前显示第 0 至 0 项，共 0 项",
        "sInfoFiltered": "(由 _MAX_ 项结果过滤)",
        "sInfoPostFix": "",
        "sSearch": "搜索:",
        "sUrl": "",
        "sEmptyTable": "表中数据为空",
        "sLoadingRecords": "载入中...",
        "sInfoThousands": ",",
        "oPaginate": {
            "sFirst": "首页",
            "sPrevious": "上页",
            "sNext": "下页",
            "sLast": "末页",
            "sJump": "跳转"
        },
        "oAria": {
            "sSortAscending": ": 以升序排列此列",
            "sSortDescending": ": 以降序排列此列"
        }
    };

    //初始化表格
    var table = $("#example").dataTable({
        // language: lang,  //提示信息
        // autoWidth: false,  //禁用自动调整列宽
        // stripeClasses: ["odd", "even"],  //为奇偶行加上样式，兼容不支持CSS伪类的场合
        processing: true,  //隐藏加载提示,自行处理
        serverSide: true,  //启用服务器端分页
        // searching: false,  //禁用原生搜索
        // orderMulti: false,  //启用多列排序
        order: [],  //取消默认排序查询,否则复选框一列会出现小箭头
        renderer: "bootstrap",  //渲染样式：Bootstrap和jquery-ui
        pagingType: "simple_numbers",  //分页样式：simple,simple_numbers,full,full_numbers
        columnDefs: [{
            "targets": [1, 2, 3],  //列的样式名
            "orderable": false    //包含上样式名‘nosort’的禁止排序
        }],
        "ajax": function (data, callback, settings) {
            //封装请求参数
            var param = {};
            param.limit = data.length;//页面显示记录条数，在页面显示每页显示多少项的时候
            param.start = data.start;//开始的记录序号
            param.page = (data.start / data.length) + 1;//当前页码
            param.search = data.search.value
            console.log(param);
            //ajax请求数据
            $.ajax({
                type: "post",
                // datasrc:"",
                url: "http://127.0.0.1:8000/core/movies",
                cache: false,  //禁用缓存
                data: param,
                dataType: "json",
                success: function (result) {
                    //console.log(result);
                    //setTimeout仅为测试延迟效果
                    setTimeout(function () {
                        //封装返回数据
                        var returnData = {};
                        // returnData.draw = data.draw;//这里直接自行返回了draw计数器,应该由后台返回
                        // returnData.recordsTotal = result.total;//返回数据全部记录
                        returnData.recordsFiltered = result.totals;//后台不实现过滤功能，每次查询均视作全部结果
                        returnData.data = result.data;//返回的数据列表
                        console.log(returnData);
                        //调用DataTables提供的callback方法，代表数据已封装完成并传回DataTables进行渲染
                        //此时的数据需确保正确无误，异常判断应在执行此回调前自行处理完毕
                        callback(returnData);
                    }, 200);
                },
                error: function (result) {
                    alert("失败")
                }
            });
        },
        // 列表表头字段
        columns: [{
            "class": 'details-control',
            "orderable": false,
            "data": null,
            "defaultContent": ''
        },
            {"data": "id"},
            {
                "data": "title",
                "render": function (data, type, row, meta) {
                    return '<textarea rows=1  cols="40" name=11 >' + row.title + '</textarea>';
                }
            },
            {"data": "recommend"},
            {"data": "like"},
            {"data": "comment"}

        ]
    }).api();
    //此处需调用api()方法,否则返回的是JQuery对象而不是DataTables的API对象

    function format(d) {
        // `d` is the original data object for the row
        return '<table cellpadding="5" cellspacing="0" border="0" style="padding-left:50px;">' +
            '<tr>' +
            '<td>name</td>' +
            '<td>' + d.id + '</td>' +
            '<td>name</td>' +
            '<td>' + d.id + '</td>' +
            '<td>name</td>' +
            '<td>' + d.id + '</td>' +
            '</tr>' +

            '<tr>' +
            '<td>Extension number:</td>' +
            '<td>' + d.title + '</td>' +
            '</tr>' +
            '<tr>' +
            '<td>Extra info:</td>' +
            '<td><button value="点击查询更多">点击查看</button></td>' +
            '</tr>' +
            '</table>';
    }

    $('#example tbody').on('click', 'td.details-control', function () {
        var tr = $(this).closest('tr');
        var row = table.row(tr);
        if (row.child.isShown()) {
            row.child.hide();
            tr.removeClass('shown');
        }
        else {
            // Open this row
            row.child(format(row.data())).show();
            tr.addClass('shown');
        }
    });
}

