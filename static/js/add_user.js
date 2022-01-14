document.addEventListener('DOMContentLoaded',() => {
  const file_input = document.querySelector('#file-input')
  const table = document.querySelector('.add-user-table')
  const thead = document.querySelector('.add-user-table thead')
  const thead_line = document.querySelector('.add-user-table thead tr')
  const tbody = document.querySelector('.add-user-table tbody')
  const selectbox = document.querySelector('#department-selector')
  const user_type_radioBtn = document.querySelectorAll('input[type="radio"]')
  const submitButton = document.querySelector('.btn.submit')
  const form = document.querySelector('form.add-user')
  const fileReader = new FileReader()

  let user_type = user_type_radioBtn[0].value
  let selected_value = selectbox.value

  user_type_radioBtn.forEach(item => {
    item.addEventListener('change',() => {
      if(item.checked) user_type = item.value

      if(user_type === '学生') {
        selectbox.removeAttribute('disabled')
        file_input.setAttribute('disabled',true)
        if(selectbox.value === '学科・コースを選択') {
          selectbox.removeAttribute('disabled')
        }else{
          file_input.removeAttribute('disabled')
        }
      }else {
        selectbox.setAttribute('disabled',true)
        file_input.removeAttribute('disabled')
      }
    })
  })

  //セレクトボックスの値が変わった時の処理
  selectbox.addEventListener('change', () => {
    selected_value = selectbox.value
    if(user_type === '学生' && selectbox.value === '学科・コースを選択'){
      file_input.setAttribute('disabled',true)
    }else {
      file_input.removeAttribute('disabled')
    }
  })

  file_input.addEventListener('change', () => {
    //CSVデータのヘッダーデータの取得と削除
    const file =  file_input.files[0]
    fileReader.readAsText(file,'Shift-JIS')
  })

  //アップロードされたファイルが読み込まれた時の処理
  fileReader.addEventListener('load',() => {
    user_type_radioBtn.forEach((el) => {
      el.setAttribute('disabled',true)
    })
    selectbox.setAttribute('disabled',true)
    file_input.setAttribute('disabled',true)

    const file_result = fileReader.result.split('\r\n')
    const header = file_result[0].split(',')
    file_result.shift()

    // CSVから情報を取得し二次元配列を生成
    const items = file_result.map(item => {
      let datas = item.split(',');

      /*
      key:ヘッダデータ
      value:個々の情報
      のオブジェクトを生成

      [exmample]
      {
        学籍番号:0000000,
        名前:山田太郎
        ...
      }
      */
      let result = {}
      for (const index in datas) {
        let key = header[index];
        result[key] = datas[index];
      }
      return result
    })

    console.log(items)

    if(items) {
      table.style.display = 'table'
      thead_line.innerHTML = `<th></th>`
      header.map(item => thead_line.innerHTML += `<th>${item}</th>`)

      if(user_type === '学生'){
        const second_th = document.querySelector('thead tr th:nth-child(3)')
        second_th.insertAdjacentHTML('afterend','<th>学科コース</th>')
      }

      let allCheck = []
      
      //二次元配列からテーブルを作成
      items.map((csvData,index) => {
        tbody.innerHTML += `<tr class="user-data-${index}"></tr>`
        const data_line = document.querySelector(`.user-data-${index}`)
        let checkTdHtml = ''
        lineDataCheck = true

        for(const type in csvData){
          let td = document.createElement('td')
          if(!check(csvData[type],type)){
            lineDataCheck = false
            td.classList.add('error')
          }

          td.innerText = csvData[type]
          data_line.appendChild(td)
        }

        allCheck.push(lineDataCheck)

        if(user_type === '学生') {
          const second_td = document.querySelector(`.user-data-${index} td:nth-child(2)`)
          second_td.insertAdjacentHTML('afterend',`<td>${selected_value}</td>`)
        }

        //プレビュー時の成功マークか失敗マークかを判断
        checkTdHtml = lineDataCheck ? 
        `
        <td>
          <span class="material-icons-outlined success">check</span>
        </td>
        `
        :
        `
        <td>
          <span class="material-icons-outlined error">error_outline</span>
        </td>
        `

        data_line.insertAdjacentHTML('afterbegin',checkTdHtml)
      })

      console.log(submitButton)

      if(!allCheck.includes(false)){
        submitButton.removeAttribute('disabled')
      }
    }
  })

  //submitする際にdisabledにした要素の情報が送れないので,submitする前にdisabled属性を取り除く処理
  form.addEventListener('submit',() => {
    file_input.removeAttribute('disabled')
    selectbox.removeAttribute('disabled')
    user_type_radioBtn.forEach(el => {
      el.removeAttribute('disabled')
    })
  })

  const check = (data,type) => {
    let check
    switch(type) {
      case '学籍番号':
        check = checkStudentNumber(data)
        break
      case '氏名':
        check = checkName(data)
        break
      case 'メールアドレス':
        check = checkMail(data)
        break
      default:
        check = true
        break
    }

    return check
  }

  //学籍番号の正規表現チェック
  const checkStudentNumber = number => new RegExp(/^[0-9]{7}$/).test(number)

  //学生氏名の文字数チェック
  const checkName = name => name.length <= 64

  //メールアドレスの正規表現チェック
  const checkMail = mail => new RegExp(/^[a-zA-Z0-9].*@morijyobi\.ac\.jp$/).test(mail)
})
