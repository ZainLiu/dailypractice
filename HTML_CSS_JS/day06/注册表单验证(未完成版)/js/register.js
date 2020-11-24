$(function () {
   $("#user_name").blur(function () {
       var username=$(this).val();
       if(!username){
           $(this).next().show().html("用户名不能为空");
           return
       }
       var re=/\w{6,20}/;
       if(!re.test(username)){
          $(this).next().show().html("用户名需在6-20位");
       }else {
          $(this).next().hide();
       }
   });
   $("#allow").click(function () {
       var allow=$("#allow").prop("checked");
   if(!allow){
       $("#allow").next().next().show().html("勾选同意才能注册！");
       return
   }else {
       $("#allow").next().next().hide();
   }
   });

});