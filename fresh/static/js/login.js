// $(function(){
//     var user_error = false;
//     var  password_error = false;
//     $('.name_input').blur(function () {
//         if ($(this).val()==''){
//             $('.user_error').html('输入用户名').show()
//             user_error=true;
//         }else {
//             // 已经输入 将错误隐藏掉
//             $('.user_error').hide();
//             user_error=false
//         }
//     })
//
//         $('.pass_input').blur(function () {
//         if ($(this).val()==''){
//             $('.pwd_error').html('输入密码').show()
//             password_error=true;
//         }else {
//             // 已经输入 将错误隐藏掉
//             $('.pwd_error').hide();
//             password_error=false
//         }
//     });
//     $('form').submit(function () {
//         name = $('.name_input').val();
//         password = $('.pass_input').val();
//         if (name == ''){
//             user_error=true;
//         }
//         if (password==''){
//             password_error=true;
//         }
//         if(user_error==false && password_error==false){
//             // 只有用户和密码输入框同时输入的时候才不阻止提交
//             return true
//         }else {
//             return false
//         }
//     });
//
// });