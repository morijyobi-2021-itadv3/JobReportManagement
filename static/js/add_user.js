document.addEventListener('DOMContentLoaded',() => {
  const file_input = document.querySelector('#file-input')
  const table = document.querySelector('.add-user-table')
  const thead = document.querySelector('.add-user-table thead')
  const thead_line = document.querySelector('.add-user-table thead tr')
  const tbody = document.querySelector('.add-user-table tbody')
  const selectbox = document.querySelector('#department-selector')
  const user_type_radioBtn = document.getElementsByName('user-type')
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

  selectbox.addEventListener('change', () => {
    selected_value = selectbox.value
    if(user_type === '学生' && selectbox.value === '学科・コースを選択'){
      file_input.setAttribute('disabled',true)
    }else {
      file_input.removeAttribute('disabled')
    }
  })

  file_input.addEventListener('change', () => {
    const file =  file_input.files[0]
    fileReader.readAsText(file,'Shift-JIS')
  })

  fileReader.addEventListener('load',() => {
    const file_result = fileReader.result.split('\r\n')
    const header = file_result[0].split(',')
    file_result.shift()

    // CSVから情報を取得し二次元配列を生成
    const csvDatas = file_result.map(item => item.split(','))
    const items = file_result.map(item => {
      let datas = item.split(',');
      let result = {}
      for (const index in datas) {
        let key = header[index];
        result[key] = datas[index];
      }
      return result
    })

    if(items) {

      
      table.style.display = 'table'
      thead_line.innerHTML = `<th></th>`
      header.map(item => thead_line.innerHTML += `<th>${item}</th>`)

      if(user_type === '学生'){
        const second_th = document.querySelector('thead tr th:nth-child(3)')
        second_th.insertAdjacentHTML('afterend','<th>学科コース</th>')
      }
      
      //二次元配列からテーブルを作成
      items.map((csvData,index) => {
        tbody.innerHTML += `<tr class="user-data-${index}"></tr>`
        const data_line = document.querySelector(`.user-data-${index}`)
        let checkTdHtml = ''
        allCheck = true

        //プレビューとしては
        /*
        学籍番号、氏名、学科コース、メアド、卒業年次、担任名
        を表示させたい
        プログラム側で追加するのは
        セレクトボックスで選ばれた学科コース
        と
        メールアドレスから取得する担任名
        */

        for(const type in csvData){
          let td = document.createElement('td')
          if(!checkTest(csvData[type],type)){
            allCheck = false
            td.classList.add('error')
          }

          td.innerText = csvData[type]
          data_line.appendChild(td)
        }

        if(user_type === '学生') {
          const second_td = document.querySelector(`.user-data-${index} td:nth-child(2)`)
          second_td.insertAdjacentHTML('afterend',`<td>${selected_value}</td>`)
        }

        checkTdHtml = allCheck ? 
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
        
        // if(check(csvData).length !== 0) {
        //   console.log('Error項目があります')
        //   checkTdHtml = `
        //   <td>
        //     <span class="material-icons-outlined error">error_outline</span>
        //   </td>
        //   `
        // }else{
        //   checkTdHtml = `
        //   <td>
        //     <span class="material-icons-outlined success">check</span>
        //   </td>
        //   `
        // }
        
        // for(const type in csvData){
        //   data_line.innerHTML += `
        //     <td>${csvData[type]}</td>
        //   `
        // }
      })
    }

    // if(csvDatas) {
    //   table.style.display = 'table'
    //   header.map(item => thead_line.innerHTML += `<th>${item}</th>`)

    //   csvDatas.map((csvData,index) => {
    //     tbody.innerHTML += `<tr class="user-data-${index}"></tr>`
    //     const data_line = document.querySelector(`.user-data-${index}`)
    //     csvData.map((data) => {
    //       data_line.innerHTML += `
    //         <td>${data.replace(/\s/,'')}</td>
    //       `
    //     })
        
    //   })
    // }
  })

  //バリデーションチェック用関数
  // const check = (datas) => {
  //   let errorMessages = []
  //   for(const type in datas) {
  //     switch(type) {
  //       case '学籍番号':
  //         checkStudentNumber(datas[type],errorMessages)
  //         break
  //       case '氏名':
  //         checkName(datas[type],errorMessages)
  //         break
  //       case 'メールアドレス':
  //         checkMail(datas[type],errorMessages)
  //         break
  //     }
  //   }
  //   return errorMessages
  // }

  const checkTest = (data,type) => {
    let check
    switch(type) {
      case '学籍番号':
        check = checkStudentNumberTest(data)
        break
      case '氏名':
        check = checkNameTest(data)
        break
      case 'メールアドレス':
        check = checkMailTest(data)
        break
      default:
        check = true
        break
    }

    return check
  }

  const checkStudentNumber = (number,errorMessages) => {
    const regex = new RegExp(/^[0-9]{6}$/)
    if(!regex.test(number)) errorMessages.push('学籍番号が適切ではありません')
  }

  const checkName = (name,errorMessages) => {
    if(name.length >= 64) errorMessages.push('氏名の文字数が多すぎます')
  }

  const checkMail = (mail,errorMessages) => {
    const regex = new RegExp(/^[a-z]+\.[a-z]+\.sys[0-9]{2}@morijyobi\.ac\.jp$/)
    if(!regex.test(mail)) errorMessages.push('メールアドレスが適切ではありません。')
  }

  const checkStudentNumberTest = number => new RegExp(/^[0-9]{7}$/).test(number)

  const checkNameTest = name => name.length <= 64

  const checkMailTest = mail => new RegExp(/^[a-z]+\.[a-z]+\.sys[0-9]{2}@morijyobi\.ac\.jp$/).test(mail)
})
