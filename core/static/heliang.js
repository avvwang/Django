$(document).ready(function () {
    module()
    // $('#example').DataTable({
    // serverSide: true,  //���÷������˷�ҳ
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
        //��ʾ��Ϣ
    var lang = {
        "sProcessing": "������...",
        "sLengthMenu": "ÿҳ _MENU_ ��",
        "sZeroRecords": "û��ƥ����",
        "sInfo": "��ǰ��ʾ�� _START_ �� _END_ ��� _TOTAL_ �",
        "sInfoEmpty": "��ǰ��ʾ�� 0 �� 0 ��� 0 ��",
        "sInfoFiltered": "(�� _MAX_ ��������)",
        "sInfoPostFix": "",
        "sSearch": "����:",
        "sUrl": "",
        "sEmptyTable": "��������Ϊ��",
        "sLoadingRecords": "������...",
        "sInfoThousands": ",",
        "oPaginate": {
            "sFirst": "��ҳ",
            "sPrevious": "��ҳ",
            "sNext": "��ҳ",
            "sLast": "ĩҳ",
            "sJump": "��ת"
        },
        "oAria": {
            "sSortAscending": ": ���������д���",
            "sSortDescending": ": �Խ������д���"
        }
    };

        //��ʼ�����
        var table = $("#example").dataTable({
            // language: lang,  //��ʾ��Ϣ
            autoWidth: false,  //�����Զ������п�
            // stripeClasses: ["odd", "even"],  //Ϊ��ż�м�����ʽ�����ݲ�֧��CSSα��ĳ���
            processing: true,  //���ؼ�����ʾ,���д���
            serverSide: true,  //���÷������˷�ҳ
            // searching: false,  //����ԭ������
            // orderMulti: false,  //���ö�������
            order: [],  //ȡ��Ĭ�������ѯ,����ѡ��һ�л����С��ͷ
            renderer: "bootstrap",  //��Ⱦ��ʽ��Bootstrap��jquery-ui
            pagingType: "simple_numbers",  //��ҳ��ʽ��simple,simple_numbers,full,full_numbers
            columnDefs: [{
                "targets": 'title',  //�е���ʽ��
                "orderable": false    //��������ʽ����nosort���Ľ�ֹ����
            }],
            "ajax": function (data, callback, settings) {
                //��װ�������
                var param = {};
                param.limit = data.length;//ҳ����ʾ��¼��������ҳ����ʾÿҳ��ʾ�������ʱ��
                param.start = data.start;//��ʼ�ļ�¼���
                param.page = (data.start / data.length) + 1;//��ǰҳ��
                param.search = data.search.value
                console.log(param);
                //ajax��������
                $.ajax({
                    type: "post",
                    // datasrc:"",
                    url: "http://127.0.0.1:8000/core/movies",
                    cache: false,  //���û���
                    data: param,
                    dataType: "json",
                    success: function (result) {
                        //console.log(result);
                        //setTimeout��Ϊ�����ӳ�Ч��
                        setTimeout(function () {
                            //��װ��������
                            var returnData = {};
                            // returnData.draw = data.draw;//����ֱ�����з�����draw������,Ӧ���ɺ�̨����
                            // returnData.recordsTotal = result.total;//��������ȫ����¼
                            returnData.recordsFiltered = result.totals;//��̨��ʵ�ֹ��˹��ܣ�ÿ�β�ѯ������ȫ�����
                            returnData.data = result.data;//���ص������б�
                            console.log(returnData);
                            //����DataTables�ṩ��callback���������������ѷ�װ��ɲ�����DataTables������Ⱦ
                            //��ʱ��������ȷ����ȷ�����쳣�ж�Ӧ��ִ�д˻ص�ǰ���д������
                            callback(returnData);
                        }, 200);
                    },
                    error:function (result) {
                        alert("ʧ��")
                    }
                });
            },
            // �б��ͷ�ֶ�
            columns: [
                {"data": "id"},
                {
                    "data": "title",

                    "render": function (data, type, row, meta) {
                        return '<textarea rows=2  name=11 readonly="readonly">' + row.title + '</textarea>';
                    }
                },
                {"data": "recommend"},
                {"data": "like"},
                {"data": "comment"}

            ]
        }).api();
        //�˴������api()����,���򷵻ص���JQuery���������DataTables��API����

}

function click11(result) {
    console.log(result)
}