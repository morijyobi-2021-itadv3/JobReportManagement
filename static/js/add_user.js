document.addEventListener('DOMContentLoaded',() => {
  const file_input = document.querySelector('#file-input')
  const table = document.querySelector('.add-user-table')
  const thead = document.querySelector('.add-user-table thead')
  const thead_line = document.querySelector('.add-user-table thead tr')
  const tbody = document.querySelector('.add-user-table tbody')
  const selectbox = document.getElementById('department-selector')
  const fileReader = new FileReader()

  selectbox.addEventListener('change', () => {
    if(selectbox.value === '学科・コースを選択'){
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
      header.map(item => thead_line.innerHTML += `<th>${item}</th>`)

      items.map((csvData,index) => {
        tbody.innerHTML += `<tr class="user-data-${index}"></tr>`
        const data_line = document.querySelector(`.user-data-${index}`)
        check(csvData)
        
        for(const type in csvData){
          data_line.innerHTML += `
            <td>${csvData[type]}</td>
          `
        }
        
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
  const check = (datas) => {
    let errorMessages = []
    for(const type in datas) {
      switch(type) {
        case '学籍番号':
          checkStudentNumber(datas[type],errorMessages)
          break
        case '氏名':
          checkName(datas,errorMessages)
      }
    }

    console.log(errorMessages)
  }

  const checkStudentNumber = (number,errorMessages) => {
    const regex = new RegExp(/^[0-9]{6}$/)
    if(!regex.test(number)) errorMessages.push('学籍番号が適切ではありません')
  }

  const checkName = (name,errorMessages) => {
    if(name.length >= 64) errorMessages.push('氏名の文字数が多すぎます')
  }

  const checkMail = (meil,errorMessages) => {
    const regex = new RegExp(/^$/)
  }
})