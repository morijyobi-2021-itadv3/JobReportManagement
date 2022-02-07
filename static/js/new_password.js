window.addEventListener("DOMContentLoaded",function (){
    const pw = document.getElementById("pw")
    const re = document.getElementById("re")
    const errmsg = document.getElementById("err")

    pw.addEventListener("input",function (){
        if(pw.value.length <= 2){
            errmsg.innerHTML = '<input type="submit" class="button" title="Sign In" value="サインイン">' +
                '<p class="error_msg">三文字以上入力してください。</p>'
            document.getElementById("btn").disabled = true;
        }else {
            errmsg.innerHTML = '<input type="submit" class="button" title="Sign In" value="サインイン">'
            document.getElementById("btn").disabled = false;
        }

    })


    re.addEventListener("input",function () {
        if(!pw.value == re.value){
            errmsg.innerHTML = '<input type="submit" class="button" title="Sign In" value="サインイン">' +
                '<p class="error_msg">パスワードが一致しません。</p>'
            document.getElementById("btn").disabled = true;
        }else {
            errmsg.innerHTML = '<input type="submit" class="button" title="Sign In" value="サインイン">'
            document.getElementById("btn").disabled = false;
        }
    })


})