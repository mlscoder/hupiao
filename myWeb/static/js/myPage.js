$(function () {
    //总条数
    var myPageCount = parseInt($("#PageCount").val());
    //当前页数
    var currentPage = parseInt($("#currentPage").val());
    //每页大小
    var myPageSize = parseInt($("#PageSize").val());
    //计算总页数
    var countindex = myPageCount % myPageSize > 0 ? (myPageCount / myPageSize) + 1 : (myPageCount / myPageSize);
    $("#countindex").val(countindex);
    //jqPaginator插件初始化，参数配置
    $.jqPaginator('#pagination', {
        totalPages: parseInt(countindex),
        visiblePages: parseInt(myPageSize),
        currentPage: currentPage,
        first: '<li class="first"><a href="javascript:;">首页</a></li>',
        prev: '<li class="prev"><a href="javascript:;"><i class="arrow arrow2"></i>上一页</a></li>',
        next: '<li class="next"><a href="javascript:;">下一页<i class="arrow arrow3"></i></a></li>',
        last: '<li class="last"><a href="javascript:;">末页</a></li>',
        page: '<li class="page"><a href="javascript:;">{{page}}</a></li>',
        onPageChange: function (num, type) {
            //点击页码或者前/后一页，执行的操作
            //1。currentPage 变量赋值 2。表单提交
            if (type == "change") {
                $("#currentPage").val(num)
                $('#submit').click();
            }
        }
    });
});