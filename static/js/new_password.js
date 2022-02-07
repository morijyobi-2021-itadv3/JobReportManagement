window.addEventListener("DOMContentLoaded",function (){
    const pw = document.getElementById("pw")
    const re = document.getElementById("re")
    const errmsg = document.getElementById("err")
    const btndom = '<input id="btn" type="submit" class="button" title="パスワード変更" value="パスワード変更">'
    pw.addEventListener("input",function (){
        if(pw.value.length <= 2){
            errmsg.innerHTML = btndom +
                '<p class="error_msg">三文字以上入力してください。</p>'
            document.getElementById("btn").disabled = true;
        }else {
            errmsg.innerHTML = btndom
            document.getElementById("btn").disabled = false;
        }

    })


    re.addEventListener("input",function () {
        if(!(pw.value === re.value)){
            errmsg.innerHTML = btndom +
                '<p class="error_msg">パスワードが一致しません。</p>'
            document.getElementById("btn").disabled = true;
        }else {
            errmsg.innerHTML = btndom
            document.getElementById("btn").disabled = false;
        }
    })


})